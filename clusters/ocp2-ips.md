# OCP2 DHCP definition (MAC and IP)

| MAC               | IP             |
| :---------------- | :------------- |
| 52:54:00:17:E8:D2 | 172.23.232.210 |
| 52:54:00:17:E8:D3 | 172.23.232.211 |
| 52:54:00:17:E8:D4 | 172.23.232.212 |
| 52:54:00:17:E8:D5 | 172.23.232.213 |
| 52:54:00:17:E8:D6 | 172.23.232.214 |
| 52:54:00:17:E8:D7 | 172.23.232.215 |
| 52:54:00:17:E8:D8 | 172.23.232.216 |
| 52:54:00:17:E8:D9 | 172.23.232.217 |
| 52:54:00:17:E8:DA | 172.23.232.218 |
| 52:54:00:17:E8:DB | 172.23.232.219 |

## OCP2 DNS setup

| IP              | DNS                        |
| :-------------  | :------------------------- |
| 172.23.232.210  | ocp2-bastion.lnxero1.boe   |
| 172.23.232.211  | control1.ocp2.lnxero1.boe  |
| 172.23.232.212  | control2.ocp2.lnxero1.boe  |
| 172.23.232.213  | control3.ocp2.lnxero1.boe  |
| 172.23.232.214  | bootstrap.ocp2.lnxero1.boe |
| 172.23.232.215  | compute1.ocp2.lnxero1.boe  |
| 172.23.232.216  | compute2.ocp2.lnxero1.boe  |
| 172.23.232.217  | compute3.ocp2.lnxero1.boe  |
| 172.23.232.218  | compute4.ocp2.lnxero1.boe  |
| 172.23.232.219  | compute5.ocp2.lnxero1.boe  |

### OCP2 additional DNS

| IP              | DNS                         |
| :-------------  | :-------------------------- |
| 172.23.232.210  | *.apps.ocp2.lnxero1.boe     |
| 172.23.232.210  | api.ocp2.lnxero1.boe        |
| 172.23.232.210  | api-int.ocp2.lnxero1.boe    |

- [IBM Boe test lab request](https://github.ibm.com/Systems-BOE-TechOps/D3170-HelpDesk/issues/1611)
