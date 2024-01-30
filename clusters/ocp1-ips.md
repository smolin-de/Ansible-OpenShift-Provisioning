# OCP1 DHCP definition (MAC and IP)

| MAC               | IP             |
| :---------------- | :------------- |
| 52:54:00:17:E8:82 | 172.23.232.130 |
| 52:54:00:17:E8:83 | 172.23.232.131 |
| 52:54:00:17:E8:84 | 172.23.232.132 |
| 52:54:00:17:E8:85 | 172.23.232.133 |
| 52:54:00:17:E8:86 | 172.23.232.134 |
| 52:54:00:17:E8:87 | 172.23.232.135 |
| 52:54:00:17:E8:88 | 172.23.232.136 |
| 52:54:00:17:E8:89 | 172.23.232.137 |
| 52:54:00:17:E8:8A | 172.23.232.138 |
| 52:54:00:17:E8:8B | 172.23.232.139 |

## OCP1 DNS setup

| IP              | DNS                         |
| :-------------  | :-------------------------- |
| 172.23.232.130  | ocp1-bastion.lnxero1.boe    |
| 172.23.232.131  | control-1.ocp1.lnxero1.boe  |
| 172.23.232.132  | control-2.ocp1.lnxero1.boe  |
| 172.23.232.133  | control-3.ocp1.lnxero1.boe  |
| 172.23.232.134  | bootstrap.ocp1.lnxero1.boe  |
| 172.23.232.135  | compute-1.ocp1.lnxero1.boe  |
| 172.23.232.136  | compute-2.ocp1.lnxero1.boe  |
| 172.23.232.137  | compute-3.ocp1.lnxero1.boe  |
| 172.23.232.138  | compute-4.ocp1.lnxero1.boe  |
| 172.23.232.139  | compute-5.ocp1.lnxero1.boe  |

### OCP1 additional DNS

| IP              | DNS                         |
| :-------------  | :-------------------------- |
| 172.23.232.130  | *.apps.ocp1.lnxero1.boe     |
| 172.23.232.130  | api.ocp1.lnxero1.boe        |
| 172.23.232.130  | api-int.ocp1.lnxero1.boe    |

- [IBM Boe test lab request](https://github.ibm.com/Systems-BOE-TechOps/D3170-HelpDesk/issues/1622)
