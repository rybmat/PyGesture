from os import listdir
from os.path import isfile, join
import cv2

path = "training_data/obj_img"
onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]

path = "obj_img/"

with open("training_data/palm.dat", "w") as f:
	for s in onlyfiles:
		if s[0] == "p":
			a = cv2.imread("training_data/" + path + s, 1)	
			f.write(path + s + "\t1\t0 0 " +  str(a.shape[0]) + " " + str(a.shape[1]) + "\n")

with open("training_data/fist.dat", "w") as f:
	for s in onlyfiles:
		if s[0] == "f":
			a = cv2.imread("training_data/" + path + s, 1)	
			f.write(path + s + "\t1\t0 0 " +  str(a.shape[0]) + " " + str(a.shape[1]) + "\n")