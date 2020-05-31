
We've found an Acorn Computers machine from the 80's, with **32K of RAM**. It is working and running **BBC Basic**, a fantastic programming language. ButcherCorp was Acorn's owner and this computer is running one of their projects. It is a "**QR Code Shell**". You send a BBC code to it and, if it renders a valid QR code, the QR code's content will be executed in a Linux system shell. There are certain limitations, such as the number of characters. Currently it's only **132** (the code will be truncated at that point). We also know that at read time the colors black and white are swapped, and that the interpreter's background color is black.

**Note:** due to hardware limitations, test your payloads locally before sending them to be executed on the server.

**Server:** nc oldschool.pwn2.win 1337
