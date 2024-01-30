# OCP3 DHCP definition (MAC and IP)

| MAC               | IP             |
| :---------------- | :------------- |
| 52:54:00:17:E8:DC | 172.23.232.220 |
| 52:54:00:17:E8:DD | 172.23.232.221 |
| 52:54:00:17:E8:DE | 172.23.232.222 |
| 52:54:00:17:E8:DF | 172.23.232.223 |
| 52:54:00:17:E8:E0 | 172.23.232.224 |
| 52:54:00:17:E8:E1 | 172.23.232.225 |
| 52:54:00:17:E8:E2 | 172.23.232.226 |
| 52:54:00:17:E8:E3 | 172.23.232.227 |
| 52:54:00:17:E8:E4 | 172.23.232.228 |
| 52:54:00:17:E8:E5 | 172.23.232.229 |

## OCP3 DNS setup

| IP              | DNS                        |
| :-------------  | :------------------------- |
| 172.23.232.220  | ocp3-bastion.lnxero1.boe   |
| 172.23.232.221  | master1.ocp3.lnxero1.boe   |
| 172.23.232.222  | master2.ocp3.lnxero1.boe   |
| 172.23.232.223  | master3.ocp3.lnxero1.boe   |
| 172.23.232.224  | bootstrap.ocp3.lnxero1.boe |
| 172.23.232.225  | worker1.ocp3.lnxero1.boe   |
| 172.23.232.226  | worker2.ocp3.lnxero1.boe   |
| 172.23.232.227  | worker3.ocp3.lnxero1.boe   |
| 172.23.232.228  | worker4.ocp3.lnxero1.boe   |
| 172.23.232.229  | worker5.ocp3.lnxero1.boe   |

### OCP3 additional DNS

| IP              | DNS                         |
| :-------------  | :-------------------------- |
| 172.23.232.220  | apps.ocp3.lnxero1.boe       |
| 172.23.232.220  | test.apps.ocp3.lnxero1.boe  |
| 172.23.232.220  | api.ocp3.lnxero1.boe        |
| 172.23.232.220  | api-int.ocp3.lnxero1.boe    |

- [IBM Boe test lab request](https://github.ibm.com/Systems-BOE-TechOps/D3170-HelpDesk/issues/1513)
