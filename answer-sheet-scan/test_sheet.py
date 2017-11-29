from sheet import get_answer_from_sheet
import cv2,math,os

import time

start = time.clock()

image_name = "0010.jpg"; ##0006 0007 

get_answer_from_sheet("img/new/"+image_name);
end = time.clock()
print "get_answer_from_sheet: %f s" % (end - start)


