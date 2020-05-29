
We discovered that the ButcherCorp has a data center in the city of Boston. Each server of this data center has a custom BMC (Baseboard Management Controller), named 'Butcher BMC' and they manage the servers remotely through an exposed IPMI interface. Luckly, the Rebelious Fingers were able to deploy a backdoor on this data center. Below is the information that they sent to us:

```
root@butcher:~# journalctl -b --no-pager | grep Echo
May 25 00:45:49 butcher ipmid[234]: Registering OEM:[0X003039], Cmd:[0X7E] for Echo Commands
```

**Server:** nc butcherbmc.pwn2.win 1337

[Link](https://static.pwn2win.party/butcher_bmc_3db544e83fc914c09389807f8723d888c40dd4695232567447d8aa6d234e42db.tar.gz)

[Mirror](https://storage.cloud.google.com/pwn2win-files/butcher_bmc_3db544e83fc914c09389807f8723d888c40dd4695232567447d8aa6d234e42db.tar.gz)
