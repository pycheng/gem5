# cpu_model
Create cpu models and run bechmark IntMM

## Reference
- [using gem5 cpu models](https://ucdavis365-my.sharepoint.com/:p:/g/personal/jlowepower_ucdavis_edu/EYRn68yb9nZJk9Puf7dV40YBdQNfhN_EyM2FsiQA4qG2eA?rtime=v4VWtFJ32kg)

## X86 cross compile
- [X86 hello cross compile](https://gem5.googlesource.com/amd/gem5/+/refs/heads/master/tests/test-progs/hello/src?autodive=0%2F/)
- Docker is required
set docker engine permission
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
make
```

## Run test with IntMM as example
download llvm-test-suite
```bash
cd $LLVM_TEST
git clone https://github.com/llvm/llvm-test-suite.git
```
replace tb.c with IntMM.c
```bash
cp $LLVM_Test/SingleSource/Benchmarks/Stanford/IntMM.c ./x86_bin/tb.c
make
```
run x86 sim
```bash
$GEM5_X86/gem5.opt ./cpu.py -n 1 -c atomic
```


## TODO Support M5 library for annotation
### build M5 library
```bash 
cd $GEM5
scons -C util/m5 build/x86/out/m5
```
### Makefile
- link env variable
- libm5.a error 
```
./dockcross-x86 bash -c '$CC -I.tb.c libm5.a -o tb32-static -static'                  
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/10/../../../i386-linux-gnu/crt1.o:
in function `_start':                                                                          
(.text+0x28): undefined reference to `main'                                           
collect2: error: ld returned 1 exit status                                            
make: *** [Makefile:13: tb32-static] Error 1  
```
```
M5_UTIL:=~/gem5/gem5/util/m5/build/x86/out
M5_INCLUDE:=~/gem5/gem5/include

#gcc -static -I${GEM5}/include tb.c ${GEM5}/util/m5/build/x86/out/libm5.a

all: tb32-static

tb32-static: tb.c dockcross-x86 
#	bash -c 'source ../../env.in'
#	TODO link env variable
	cp -r $(M5_INCLUDE)/gem5 .
	cp $(M5_UTIL)/libm5.a .
	./dockcross-x86 bash -c '$$CC -static -I. tb.c libm5.a -o tb32-static'


dockcross-x86:
	docker run --rm dockcross/linux-x86 > ./dockcross-x86
	chmod +x ./dockcross-x86

clean:
	rm -f dockcross-* tb32-static
```

