# cpu_model
Create cpu models and run bechmark IntMM

## Reference
- [using gem5 cpu models](https://ucdavis365-my.sharepoint.com/:p:/g/personal/jlowepower_ucdavis_edu/EYRn68yb9nZJk9Puf7dV40YBdQNfhN_EyM2FsiQA4qG2eA?rtime=v4VWtFJ32kg)

## X86 cross compile
- [X86 hello cross compile](https://gem5.googlesource.com/amd/gem5/+/refs/heads/master/tests/test-progs/hello/src?autodive=0%2F/)
- Docker is required
- TODO remove sudo
```bash
	sudo docker run --rm dockcross/linux-x86 > ./dockcross-x86
        sudo chmod +x ./dockcross-x86
```
