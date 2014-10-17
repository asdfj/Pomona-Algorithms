import sys

cmdargs = str(sys.argv)

fo = open(sys.argv[1], "r+")
dimarray = []

for line in fo:
	nums = [int(n) for n in line.split()]
	dimarray.append(nums)

fo.close()
del dimarray[0]

def getKey(item):
	return item.base_area

class Box(object):
	def __init__(self, h, w, d):
		self.h = h
		self.w = w
		self.d = d
		self.base_area = w * d

	def __str__(self):
		return str([self.h, self.w, self.d])

def create_box(box_array):
	return Box(box_array[0], box_array[1], box_array[2])

def create_all_types_of_box(box):
	a = box
	b = Box(box.w, box.d, box.h)
	c = Box(box.d, box.h, box.w)
	return [a, b, c]

boxes = []
all_boxes = []

for dim in dimarray:	
	boxes.append(create_all_types_of_box(create_box(dim)))

for l in boxes:
	all_boxes = all_boxes + l


sorted_boxes = sorted(all_boxes, key = getKey, reverse = True)

bs_array = []

boxes_used = []


for box in sorted_boxes:
	bs_array.append(box.h)
	boxes_used.append([box])

box_solution_array = []

for i, box_bottom in enumerate(sorted_boxes):
	for j, box_top in enumerate(sorted_boxes):
		if box_bottom.w < box_top.w and box_bottom.d < box_top.d and bs_array[i] < bs_array[j] + box_bottom.h:
			bs_array[i] = bs_array[j] + box_bottom.h

#for i, box_bottom in enumerate(all_boxes):
#	for j, box_top in enumerate(all_boxes):
#		if box_top.base_area > box_bottom.base_area and bs_array[i] < bs_array[j] + box_top.h:
#			bs_array[i] = bs_array[j] + box_top.h

max_height = max(bs_array)

fo = open("outfile.txt", "w")
fo.write("The tallest tower has a height of %d" % max_height)
fo.close

