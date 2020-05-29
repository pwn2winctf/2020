
A Intellectual Property Protection Corp é a empresa líder do mercado em proteção de propriedade intelectual de hardware. O produto deles protege IP cores com "tecnologia de criptografia proprietária de nível militar", de forma que só possam ser instanciados em um projeto de hardware caso fornecida a chave de licença correta.
Nós conseguimos invadir algumas máquinas da ButcherCorp e vazar vários IP cores que eles usaram no projeto rbs. No entanto, esses IP cores estão protegidos com tecnologia da IP Protection Corp, e não fomos capazes de recuperar a chave de licença deles.
Estamos agora recrutando pessoas com talento em engenharia reversa para nos ajudar. Você consegue entender como a tecnologia da IP Protection Corp realmente funciona? Por favor veja uma demonstração simples no arquivo anexo. Se você descobrir a chave de licença correta, o test bench (Tb) obterá a flag do pacote protegido design under test (Dut) e a mostrará na saída.

Você pode usar o Docker para executar o test bench, por exemplo:
```
docker build -t ip-protection .
docker run --rm ip-protection 123
```

[Link](https://static.pwn2win.party/ip_protection_59ea48a7cebd7974d97244d9decf43572e7a6b5573146dcade919ab2d99e1c7a.tar.gz)

[Mirror](https://storage.cloud.google.com/pwn2win-files/ip_protection_59ea48a7cebd7974d97244d9decf43572e7a6b5573146dcade919ab2d99e1c7a.tar.gz)
