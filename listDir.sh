cd /home/pi/Pictures/buildingImages
ls -lrt -d -1 $PWD/Inspection* | awk -F ' ' '{print $9}'
