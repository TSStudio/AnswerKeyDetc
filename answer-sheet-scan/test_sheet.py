from sheet import get_answer_from_sheet
import cv2,math

import time

start = time.clock()
base_img = cv2.imread('img/1001.jpg')
get_answer_from_sheet(base_img)
end = time.clock()
print "get_answer_from_sheet: %f s" % (end - start)


