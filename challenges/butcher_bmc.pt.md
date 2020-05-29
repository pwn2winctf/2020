
Descobrimos que a ButcherCorp tem um data center na cidade de Boston. Cada servidor desse data center possui um BMC (Baseboard Management Controller) personalizado, chamado 'Butcher BMC', e eles gerenciam os servidores remotamente por meio de uma interface IPMI exposta. Felizmente, o Rebelious Fingers conseguiu implantar um backdoor neste data center. Abaixo estão as informações que eles nos enviaram:

```
root@butcher:~# journalctl -b --no-pager | grep Echo
May 25 00:45:49 butcher ipmid[234]: Registering OEM:[0X003039], Cmd:[0X7E] for Echo Commands
```

**Server:** nc butcherbmc.pwn2.win 1337

[Link](https://static.pwn2win.party/butcher_bmc_3db544e83fc914c09389807f8723d888c40dd4695232567447d8aa6d234e42db.tar.gz)

[Mirror](https://storage.cloud.google.com/pwn2win-files/butcher_bmc_3db544e83fc914c09389807f8723d888c40dd4695232567447d8aa6d234e42db.tar.gz)
