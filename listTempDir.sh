cd /home/pi/Pictures/temp
ls -lrt -d -1 $PWD/Inspection* | awk -F ' ' '{print $9}'
