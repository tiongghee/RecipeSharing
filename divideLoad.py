import requests
import os,sys
import shutil
import time

# Create a temporary directory if it does not exist
tempDir = '/home/pi/Pictures/temp'
if not os.path.exists(tempDir):
	os.makedirs(tempDir)

# Loop through the image directory
directory = '/home/pi/Pictures/buildingImages'
count = 0
total = 0
for filename in os.listdir(directory):
	print(os.path.join(directory, filename))
	os.rename(os.path.join(directory, filename), os.path.join(tempDir, filename))
	# Store images to Cloudant
	if count//10 > 0:
		print "Call Loading"
		try:
			response = requests.get('http://localhost:1880/uploadImages', timeout = 5)
		except :
			time.sleep(5)
		shutil.rmtree(tempDir);
		if not os.path.exists(tempDir):
			os.makedirs(tempDir)
		count = 0
	count = count + 1
	total = total + 1

# Check if directory exist. Load remainder files
if count > 0 and  os.path.exists(tempDir):
	print "Call Loading"
	try:
		response = requests.get('http://localhost:1880/uploadImages', timeout = 5)
	except :
		time.sleep(5)
	shutil.rmtree(tempDir);

print "Script End"
