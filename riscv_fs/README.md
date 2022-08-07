# RISC-V FS simulation 
Create a RISC-V gem5 full system simulation
The following references the gem5 default config and resource.

## Pre-requirement 
- build gem5 RISCV binary 
```bash
scons build/RISCV/gem5.opt
```

## UcanLinux example
```bash
$GEM5_RV/gem5.opt configs/example/gem5_library/riscv-fs.py

nc localhost $port
# login to linux with root/root
```

## Reference
- [riscv-fs](http://resources.gem5.org/resources/riscv-fs)
- [gem5-bootcamp full system
  simulation](https://gem5bootcamp.github.io/gem5-bootcamp-env/modules/using%20gem5/full-system/)
