all: tb32-static

tb32-static: tb.c dockcross-x86 
	sudo ./dockcross-x86 bash -c '$$CC tb.c -o tb32-static -static'

dockcross-x86:
	sudo docker run --rm dockcross/linux-x86 > ./dockcross-x86
	sudo chmod +x ./dockcross-x86

clean:
	rm -f dockcross-* tb32-static
