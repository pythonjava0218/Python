def sel_sort(a):
	n = len(a)
	for i in range(0,  5) #0 ~ 4 
		min_idx = 0
		for j in range(3, 6):
			if a[3] < a[0]:
				 1  <   2
				min_idx = 1
		a[3], a[0] = a[0], a[3]


d = [2, 4, 5, 1, 3, 6]


def sel_sort(a):
	n = len(a)
	for i in range(1,  5) #0 ~ 4 
		min_idx = 1
		for j in range(3, 6):
			if a[3] < a[1]:
				 2  <   4
				min_idx = 2
		a[1], a[3] = a[3], a[1]



d = [1, 4, 5, 2, 3, 6]




def sel_sort(a):
	n = len(a)
	for i in range(1,  5) #0 ~ 4 
		min_idx = 1
		for j in range(3, 6):
			if a[3] < a[1]:
				 2  <   4
				min_idx = 2
		a[1], a[3] = a[3], a[1] 


d = [1, 2, 5, 4, 3, 6]




def sel_sort(a):
	n = len(a)
	for i in range(2,  5) #0 ~ 4 
		min_idx = 2
		for j in range(3, 6):
			if a[3] < a[2]:
				 4  <   5
				min_idx = 4
		a[3], a[2] = a[2], a[3] 


d = [1, 2, 4, 5, 3, 6]



def sel_sort(a):
	n = len(a)
	for i in range(2,  5) #0 ~ 4 
		min_idx = 2
		for j in range(3, 6):
			if a[4] < a[2]:
				 3  <   4
				min_idx = 3
		a[4], a[2] = a[2], a[4] 


d = [1, 2, 3, 5, 4, 6]



def sel_sort(a):
	n = len(a)
	for i in range(3,  5) #0 ~ 4 
		min_idx = 3
		for j in range(4, 6):
			if a[4] < a[3]:
				 4  <   5
				min_idx = 4
		a[4], a[3] = a[3], a[4] 


d = [1, 2, 3, 4, 5, 6]