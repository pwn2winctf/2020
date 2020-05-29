
Intellectual Property Protection Corp is the market leader on hardware IP protection. Their product protects IP cores with "proprietary military-strength encryption technology" so that they can only be instantiated in a hardware design by supplying the correct license key.
We were able to break into some ButcherCorp workstations and leak several IP cores they used in the rbs project. However, these IP cores are protected with IP Protection Corp technology, and we were not able to recover their license key.
We are now recruiting talented reverse engineers to help us. Are you able to understand how IP Protection Corp technology really works? Please find attached a simple demo. If you find the correct license key, the test bench (Tb) will retrieve the flag from the protected design under test (Dut) and print it to the output.

You can use Docker to run the test bench, e.g.:
```
docker build -t ip-protection .
docker run --rm ip-protection 123
```

[Link](https://static.pwn2win.party/ip_protection_59ea48a7cebd7974d97244d9decf43572e7a6b5573146dcade919ab2d99e1c7a.tar.gz)

[Mirror](https://storage.cloud.google.com/pwn2win-files/ip_protection_59ea48a7cebd7974d97244d9decf43572e7a6b5573146dcade919ab2d99e1c7a.tar.gz)
