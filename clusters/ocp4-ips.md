# OCP4 DHCP definition (MAC and IP)

| MAC               | IP             |
| :---------------- | :------------- |
| 52:54:00:17:E8:F0 | 172.23.232.240 |
| 52:54:00:17:E8:F1 | 172.23.232.241 |
| 52:54:00:17:E8:F2 | 172.23.232.242 |
| 52:54:00:17:E8:F3 | 172.23.232.243 |
| 52:54:00:17:E8:F4 | 172.23.232.244 |
| 52:54:00:17:E8:F5 | 172.23.232.245 |
| 52:54:00:17:E8:F6 | 172.23.232.246 |
| 52:54:00:17:E8:F7 | 172.23.232.247 |
| 52:54:00:17:E8:F8 | 172.23.232.248 |
| 52:54:00:17:E8:F9 | 172.23.232.249 |

| IP              | DNS                         |
| :-------------  | :-------------------------- |
| 172.23.232.240  | ocp4-bastion.lnxero1.boe    |
| 172.23.232.241  | control-1.ocp4.lnxero1.boe  |
| 172.23.232.242  | control-2.ocp4.lnxero1.boe  |
| 172.23.232.243  | control-3.ocp4.lnxero1.boe  |
| 172.23.232.244  | bootstrap.ocp4.lnxero1.boe  |
| 172.23.232.245  | compute-1.ocp4.lnxero1.boe  |
| 172.23.232.246  | compute-2.ocp4.lnxero1.boe  |
| 172.23.232.247  | compute-3.ocp4.lnxero1.boe  |
| 172.23.232.248  | compute-4.ocp4.lnxero1.boe  |
| 172.23.232.249  | compute-5.ocp4.lnxero1.boe  |

## OCP4 additional DNS

| IP              | DNS                         |
| :-------------  | :-------------------------- |
| 172.23.232.240  | *.apps.ocp4.lnxero1.boe     |
| 172.23.232.240  | api.ocp4.lnxero1.boe        |
| 172.23.232.240  | api-int.ocp4.lnxero1.boe    |

- [IBM Boe test lab request](https://github.ibm.com/Systems-BOE-TechOps/D3170-HelpDesk/issues/1623)
