
We discovered some shadowy organization used to deploy malware able to insert hardware trojans in FPGA designs during the synthesis process. Due to reprogramability requisites, some quite important subsystems of the rbs use FPGAs, so if we manage to understand how the designs are modified, we can turn this into our advantage.

We were able to [replicate](https://github.com/rf-hw-team/fpga-zynq) a design using the Rocket RISC-V core on a Zynq-7020 FPGA and found this core got infected by the synthesis tools!

Help us analyzing the compromised CPU core. We suspect the hardware trojan is triggered by writing a particular string to memory. We attached below the netlist of the SoC infected after synthesis. Find and submit the trigger string (it is already in our flag format).

**Files**

 * [Link](https://static.pwn2win.party/hardware_trojan_v2_pt1_483f0c6587ac5265614c4584b020b40d399d29f645172802cd575f83ab338ad9.tar.gz)
 * [Mirror](https://storage.cloud.google.com/pwn2win-files/hardware_trojan_v2_pt1_483f0c6587ac5265614c4584b020b40d399d29f645172802cd575f83ab338ad9.tar.gz)

**Useful info**

 * [Xilinx cells](https://github.com/YosysHQ/yosys/tree/master/techlibs/xilinx)
 * [Interesting paper](http://www.cse.cuhk.edu.hk/~qxu/zhang-dac13.pdf)

