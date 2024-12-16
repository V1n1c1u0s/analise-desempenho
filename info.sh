#!/bin/bash

arq="info_sistema.txt"

echo "Informações do Sitema" > "$arq"

add_entrada(){
	echo -e "$1" >> "$arq"
}


add_entrada "$(cat /etc/os-release | grep PRETTY_NAME | sed 's/.*"\(.*\)".*/\1/')"
add_entrada "$(uname -r)"
add_entrada "$(cat /proc/cpuinfo | grep 'model name' | uniq | awk -F': ' '{print $2}')"
add_entrada "$(cat /proc/meminfo | grep MemTotal | awk -F':       ' '{print $2}')"
