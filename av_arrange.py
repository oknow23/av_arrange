import os
import sys
import re

VERSION = '0.1.0'
DBG = 0
JPG_TYPE = 0
VIDEO_TYPE = 1
dirName = ''
avid_fix = ''
try_cnt = 1


# Get file name from folder
print("Re-name folder start")
print("---------------------------------------")
for fileNames in os.listdir(os.getcwd()):
	if os.path.isdir(fileNames):
		cleanName = re.sub(r'/\(.*?\)|\[.*?\]| |\【.*?\】|#|最新|~|\d*\/\d*|VIP\d+|\d月\d+日|\.\.\./g', '',fileNames)
		pattern = re.compile(r'[a-zA-Z-0-9]*')
		av_id = pattern.search(cleanName).group()
		if av_id:
			print(fileNames)
			title_fix = re.sub(r'[a-zA-Z0-9]*|-', '',cleanName)
			if not re.search('-',av_id):
				# print(av_id)
				avid_fix = re.search(r'[a-zA-Z]*',av_id).group()+ '-' +re.search(r'[0-9]+',av_id).group()
				# print(avid_fix)
			else:
				avid_fix = av_id
			newName = avid_fix + ' ' + title_fix
			print('New Name:'+newName)
			os.rename(fileNames,newName)

print("---------------------------------------")

# Allocate folder
girl_list = ["三上悠亞", "旬果", "橋本", "桃乃木", "桜空","水卜"];

print("Allocate to folder start")
print("---------------------------------------")
for fileNames in os.listdir(os.getcwd()):
	if os.path.isdir(fileNames) and re.search(r'[a-zA-Z-0-9]*',fileNames).group():
		for girl in girl_list:
			if re.search(girl,fileNames):
				print(fileNames)
				if not os.path.isdir(girl):
					os.makedirs(girl)
				print('Move to:'+girl+'\\'+fileNames)
				os.rename(fileNames,girl+'\\'+fileNames)
print("---------------------------------------")

print('Done!!')

if DBG == 0:
	os.system("pause")