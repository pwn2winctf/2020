
Descobrimos que uma certa organização secreta costumava propagar malware capaz de inserir trojans de hardware em projetos de FPGA durante o processo de síntese. Devido a requisitos de reprogramabilidade, alguns subsistemas importantes dos rbs usam FPGAs, então se conseguirmos entender como os circuitos são modificados, podemos usar isso em nosso benefício.

Conseguimos [replicar](https://github.com/rf-hw-team/fpga-zynq) um projeto usando o Rocket RISC-V em um FPGA Zynq-7020 e percebemos que o núcleo é infectado pelas ferramentas de síntese!

Ajude-nos a analisar o núcleo de CPU comprometido. Suspeitamos que o trojan de hardware é ativado quando uma sequência específica é escrita na memória. Anexamos abaixo a netlist do SoC infectado após a síntese. Descubra a cadeia de caracteres que ativa o trojan e a submeta (ela já está no nosso formato de flag).

**Arquivos**

 * [Link](https://static.pwn2win.party/hardware_trojan_v2_pt1_483f0c6587ac5265614c4584b020b40d399d29f645172802cd575f83ab338ad9.tar.gz)
 * [Mirror](https://storage.cloud.google.com/pwn2win-files/hardware_trojan_v2_pt1_483f0c6587ac5265614c4584b020b40d399d29f645172802cd575f83ab338ad9.tar.gz)


**Informações úteis**

 * [Xilinx cells](https://github.com/YosysHQ/yosys/tree/master/techlibs/xilinx)
 * [Artigo interessante](http://www.cse.cuhk.edu.hk/~qxu/zhang-dac13.pdf)

