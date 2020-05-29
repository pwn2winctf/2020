
Nós encontramos um computador da Acorn Computers da década de 80, com 32K de RAM. Ele está funcional, e roda BBC Basic, uma linguagem de programação fantástica. A ButcherCorp era dona da Acorn, e esse computador está rodando um projeto deles. Consiste em um "QR Code Shell". É enviado um código BBC, que ao renderizar um QR Code válido, o comando do seu conteúdo é executado no sistema. Há algumas limitações, como o número de caracteres possível. Atualmente são 132 apenas (seu código é truncado nesse ponto se for maior que isso). Também sabemos que na hora da leitura, as cores preta e branca se invertem, e a cor de fundo do interpretador é originalmente preta.

Obs: Devido as limitações do seu hardware, teste seus payloads localmente antes de enviar para execução.

**Server:** nc oldschool.pwn2.win 1337
