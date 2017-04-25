cd /home/pi/Pictures/temp
ls -lrt -d -1 $PWD/*.jpg | awk -F ' ' '{print $9}'
