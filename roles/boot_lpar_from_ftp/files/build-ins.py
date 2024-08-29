#!/usr/bin/env python3
# vim: set fileencoding=UTF-8 :
import sys
import os.path
import struct

# This tool can be used to build either a .ins file or a combined image from
# a Linux kernel (plus optional initramfs and kernel command line parameters).
#
# The .ins file is needed to boot that kernel from the SE/HMC from FTP or removable media.
# The combined image can be loaded straight from the SE into LPAR memory and booted from there.


# found in <kernel source>/arch/s390/include/asm/setup.h (INITRD_START and INITRD_SIZE together)
INITRAMFS_ADDR_SIZE_OFFSET = 0x10408

# found in <kernel source>/arch/s390/include/asm/setup.h (COMMAND_LINE)
KERNEL_CMDLINE_OFFSET = 0x10480

# found in <kernel source>/arch/s390/include/uapi/asm/setup.h (ARCH_COMMAND_LINE_SIZE)
KERNEL_CMDLINE_MAX_LENGTH = 895

# found in <kernel source>/arch/s390/include/asm/lowcore.h (lowcore.restart_psw)
KERNEL_RESTART_PSW_OFFSET = 0x1A0

# check if a file with the given name exists, error out if not
def check_file(filename):
  if not os.path.isfile(filename):
    sys.exit("ERROR: '%s' is not a valid file!" % filename)

# get size in bytes of the given file
def get_filesize(filename):
  check_file(filename)
  return os.path.getsize(filename)

# take address and round it up to the next MiB boundary
def round_up_to_mib(address):
  address >>= 20
  address += 1
  address <<= 20
  return address

# takes a 64 bit PSW as a bytes object and transforms it into the equivalent 128 bit PSW
def short_to_long_psw(short_psw):
  assert len(short_psw) == 8
  assert isinstance(short_psw, bytes)

  long_psw = bytearray()

  # copy the first byte straight over
  long_psw.append(short_psw[0])

  # toggle bit 3 of byte 2
  byte2 = short_psw[1]
  byte2 ^= 0x08
  long_psw.append(byte2)

  # copy bytes 3-4
  long_psw.extend(short_psw[2:4])

  # split byte 5 into the leftmost bit and the rest
  byte5 = short_psw[4]
  ba_byte = byte5 & 0x80
  ia_byte = byte5 & 0x7F

  # tack the BA byte onto the long PSW and zero pad
  long_psw.append(ba_byte)
  long_psw.extend(b'\x00' * 3)

  # assemble the full instruction address and tack onto the long PSW
  long_psw.extend(b'\x00' * 4)
  long_psw.append(ia_byte)
  long_psw.extend(short_psw[5:8])

  assert len(long_psw) == 16
  return bytes(long_psw)

# write out the initramfs info (offset / size) into a binary file
def write_out_initramfs_details(filename, address, size):
  addrsize_fd = open(filename, "wb")
  addrsize_fd.write(struct.pack(">QQ", address, size))
  addrsize_fd.close()

# write out the final .ins file
# files should be a list of tuples of the form (filename, offset)
def write_out_ins_file(outfile, files, comment=None):
  buf = ""

  # check / complete output file name (since the extension is important)
  if (outfile[-4:] != ".ins"):
    outfile += ".ins"

  # write out the comment (if one was given)
  if (comment is not None):
    buf += "* "
    buf += comment
    buf += '\n'

  for item in files:
    # unpack the tuple into its elements
    filename, offset = item
    
    # is the filename valid?
    check_file(filename)

    # is the offset of the correct type?
    if not isinstance(offset, int):
      raise TypeError("Offset must be an integer")

    # everything okay? then build the line and append it
    buf += filename
    buf += " "
    buf += "0x%08x\n" % offset

  # if that has all worked out, write the buffer out
  ins_fd = open(outfile, "w")
  ins_fd.write(buf)
  ins_fd.close()

# write out the final image file
# files should be a list of tuples of the form (filename, offset)
def write_out_img_file(outfile, files):
  # how big should our read buffer be?
  bufsize = 0x100000

  # open our .img file for writing
  outfile_fd = open(outfile, "wb")

  for item in files:
    # unpack the tuple into its elements
    filename, offset = item
    
    # is the filename valid?
    check_file(filename)

    # is the offset of the correct type?
    if not isinstance(offset, int):
      raise TypeError("Offset must be an integer")

    # read the input file and place it in the image file
    infile_fd = open(filename, "rb")
    outfile_fd.seek(offset)
    while True:
      infile_buf = infile_fd.read(bufsize)
      if len(infile_buf) > 0:
        outfile_fd.write(infile_buf)
      else:
        break
    infile_fd.close()

  # we're done - clean up
  outfile_fd.close()

# take the S/390 Restart PSW from image offset 0x00, transform it into
# a equivalent z/Arch Restart PSW and patch into the correct location
def patch_image_psw(img_file):
  # is the filename valid?
  check_file(img_file)

  we_patched = False
  imgfile_fd = open(img_file, "r+b")

  # check for existing z/Arch Restart PSW
  imgfile_fd.seek(KERNEL_RESTART_PSW_OFFSET)
  if imgfile_fd.read(16) == (b'\x00' * 16):
    # there's nothing there - patch it

    # get the old Restart PSW
    imgfile_fd.seek(0)
    short_psw = imgfile_fd.read(8)

    # transform into z/Arch PSW
    long_psw = short_to_long_psw(short_psw)

    # write out the patched PSW
    imgfile_fd.seek(KERNEL_RESTART_PSW_OFFSET)
    imgfile_fd.write(long_psw)
    we_patched = True

  # we're done - clean up
  imgfile_fd.close()
  return we_patched


if __name__ == "__main__":
  import argparse

  # Make sure we're running in Python 3.3 or newer
  if sys.version_info < (3,3):
    print("Please run this using Python 3.3 or newer!")
    sys.exit(1)

  # parse command line arguments
  argparser = argparse.ArgumentParser(description="Creates .ins file for FTP load or monolithic image from kernel image, initramfs and kernel parameters")
  argparser.add_argument("-m", "--mode", help="Determines whether a .ins file or a monolithic combined image file is created (defaults to .ins)", choices=("ins", "img"), default="ins")
  argparser.add_argument("-k", "--kernel", metavar="KERNEL_IMAGE", help="File name of the kernel image", required=True)
  argparser.add_argument("-i", "--initramfs", help="File name of the initramfs")
  argparser.add_argument("-p", "--cmdline", metavar="KERNEL_COMMAND_LINE", help="Name of the file containing the kernel command line parameters")
  argparser.add_argument("-c", "--comment", help="Descriptive comment for the .ins file")
  argparser.add_argument("-o", "--outfile", help="Name of the output file to create", required=True)
  args = argparser.parse_args()

  source_files = []

  # the kernel always sits at offset 0x00
  source_files.append((args.kernel, 0))

  # initramfs related processing
  if (args.initramfs is not None):
    # get the size of the kernel and initramfs
    kern_size = get_filesize(args.kernel)
    initramfs_size = get_filesize(args.initramfs)

    # round kernel size up to the next MiB boundary
    offset = round_up_to_mib(kern_size)

    # create the kernel binary patch file holding the initramfs address / size
    patchfile_name = args.initramfs + ".addrsize"
    write_out_initramfs_details(patchfile_name, offset, initramfs_size)

    source_files.append((args.initramfs, offset))
    source_files.append((patchfile_name, INITRAMFS_ADDR_SIZE_OFFSET))

  # kernel command line related processing
  if (args.cmdline is not None):
    # check if the kernel command line is too long
    if (get_filesize(args.cmdline) > KERNEL_CMDLINE_MAX_LENGTH):
      sys.exit("ERROR: '%s' is bigger than the maximum of %d bytes!" % (args.cmdline, KERNEL_CMDLINE_MAX_LENGTH))
    source_files.append((args.cmdline, KERNEL_CMDLINE_OFFSET))

  # .ins file related processing
  if (args.mode == "ins"):
    write_out_ins_file(args.outfile, source_files, args.comment)
    sys.exit(0)

  # image file related processing
  if (args.mode == "img"):
    write_out_img_file(args.outfile, source_files)
    if patch_image_psw(args.outfile):
      print("No z/Arch Restart PSW found in image - patching it in.")
    sys.exit(0)
