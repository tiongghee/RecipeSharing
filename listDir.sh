cd /home/pi/Pictures/buildingImages
ls -lrt -d -1 $PWD/*.jpg | awk -F ' ' '{print $9}'
