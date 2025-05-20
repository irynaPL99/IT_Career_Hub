##!/bin/bash
set -e

echo "# 1.выводить 10 раз дату и кол-во процессов:"
for i in {1..10}
do
	echo "Дата: $(date +%H:%M:%S). Кол-во процессов: $(ps -aux | wc -l) "
	# sleep 5
done
echo "#1. done"


echo "----  ----- -----" >> info_task15.txt
echo " #3. Информация о процессоре: " > info_task15.txt
#lscpu >> info_task15.txt
cat  /proc/cpuinfo >> info_task15.txt
echo "#3. done"


echo "----  ----- -----" >> info_task15.txt
echo "#4. Имя ОС:"  >> info_task15.txt
cat /etc/os-release | head -n 1 >> info_task15.txt
echo "#4. done"


echo "----  ----- -----" >> info_task15.txt
echo "#5. Только имя ОС:" >> info_task15.txt
cat /etc/os-release | head -n 1 | awk -F'"' '{print$2}'  >> info_task15.txt
echo "#5. done"

echo "#6.Создание файлов от 50.txt до 100.txt:"
for  i in $(seq 50 100)
do
	touch "$i.txt"
done
echo "#6. done"

echo "script done"
