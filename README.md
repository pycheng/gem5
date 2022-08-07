# gem5

## TODO
The default cpu takes Intel 80386 instruction set.
I cannot find x86-64 cpu config yet.

```bash
➜  cpu_model git:(m5op) ✗ uname -a
Linux MigiNB 5.15.0-43-generic #46-Ubuntu SMP Tue Jul 12 10:30:17 UTC 2022
x86_64 x86_64 x86_64 GNU/Linux
➜  cpu_model git:(m5op) ✗ file ./x86_bin/tb32-static 
./x86_bin/tb32-static: ELF 32-bit LSB executable, Intel 80386, version
1 (GNU/Linux), statically linked,
BuildID[sha1]=e49d8ef3f302a366f67240af2c4d7f9c3158eed8, for GNU/Linux 3.2.0,
not stripped

```

## Tool
- to show the m5 dot config in m5out folder: install pydot and xdot
```bash
pip install pydot
apt install xdot
```
