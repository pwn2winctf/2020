
After you solved for Part 1, we found a Rocket RISC-V system at `iot.pwn2.win`. We need to own a root shell in this system through SSH. To get this done, it is not enough to know the trigger string. We need to understand how the 64-bit word written just after the trigger string affects the control flow and how this can be employed to compromise the Dropbear server. We are counting on you: get a shell and submit the contents of `/root/flag`.

**Server**: `iot.pwn2.win`

**Files**

 * [Link](https://static.pwn2win.party/hardware_trojan_v2_pt2_eb5534aa1130a891136ae07348a8a27b92f333cf12587f186a7b06c6f3c1cc1b.tar.gz)
 * [Mirror](https://storage.cloud.google.com/pwn2win-files/hardware_trojan_v2_pt2_eb5534aa1130a891136ae07348a8a27b92f333cf12587f186a7b06c6f3c1cc1b.tar.gz)
