import cv2 as cv 
import numpy as np
# 0 indicates empty block in sudoku
sudoku = [[0,0,0,2,6,0,7,0,1],
			[6,8,0,0,7,0,0,9,0],
			[1,9,0,0,0,4,5,0,0],
			[8,2,0,1,0,0,0,4,0],
			[0,0,4,6,0,2,9,0,0],
			[0,5,0,0,0,3,0,2,8],
			[0,0,9,3,0,0,0,7,4],
			[0,4,0,0,5,0,0,3,6],
			[7,0,3,0,1,8,0,0,0]]
def track_callback():
	pass
def drawline():
	for i in range(0,10):
		if i%3 == 0:
			cv.line(img,((i*99)+5, 5), ((i*99)+5,(297*3)+5), (0,255,255), 2 )
			cv.line(img,(5,(i*99)+5), ((297*3)+5,(i*99)+5), (0,255,255), 2 )
		else:
			cv.line(img,((i*99)+5, 5), ((i*99)+5,(297*3)+5), (255,255,0), 1 )
			cv.line(img,(5,(i*99)+5), ((297*3)+5,(i*99)+5), (255,255,0), 1 )
def putnumber():
	for i in range(0,9):
		for j in range(0,9):
			# print(i,j)
			if sudoku[i][j] != 0:
				cv.putText(img, str(sudoku[i][j]),((j*99)+32, (i*99)+80) , cv.FONT_HERSHEY_PLAIN , 5 , (0,255,0), 3)
		cv.putText(img, '--------------------Solving Sudoku ------------------', (10, (297*3)+35), cv.FONT_HERSHEY_TRIPLEX , 0.7, (0, 0, 255), 2)
def isvalid(i,j, num):
	flag = True
	for l in range(0,9):
		if sudoku[i][l] == num or sudoku[l][j] == num :
			return False
			# break
	for a in range(int(i/3)*3, (int(i/3)*3)+3):
		for b in range(int(j/3)*3, (int(j/3)*3)+3):
			if sudoku[a][b] == num :
				return False 
	return True 
def solve(i , j):
		# if i == 8 and j == 8 :
		# 	print("True")
		# 	return True 
		# else:
		for a in range(0, 9):
			for b in range(0,9):
				if a == 8 and b == 8:
					temp = sudoku[a][b]
					sudoku[a][b] = 0
					if isvalid(a, b, temp) == True:
						# cv.rectangle(img, (0,297*3),((297*3)+50,(297*3)+10), (0,0,0))
						# print("True")
						return True
				if sudoku[a][b] == 0 :
					num = 1
					while num <=9:
						if isvalid(a,b, num) == True:
							sudoku[a][b] = num
							# delay = cv.getTrackbarPos('delay', 'sudoku')
							cv.waitKey(delay)
							cv.rectangle(img,( (b*99)+10, (a*99)+10), ( (b*99)+80, (a*99)+80), (0, 0 , 0), -1)
							cv.putText(img, str(num),((b*99)+32, ( a*99)+80) , cv.FONT_HERSHEY_PLAIN , 5 , (0,0,255), 3)
							cv.imshow('sudoku', img)
							if solve(a,b) == True :
								cv.putText(img, '--------------------Solving Sudoku ------------------', (10, (297*3)+35), cv.FONT_HERSHEY_TRIPLEX , 0.7, (0, 0, 0), 2)
								cv.putText(img, '------------------Solved Successfully -----------------------', (10, (297*3)+35), cv.FONT_HERSHEY_TRIPLEX , 0.7, (0, 255, 0), 2)
								cv.imshow('sudoku', img)
								a = 8 
								b = 8
								break 
						num += 1 
					if num == 10 :
						sudoku[a][b] = 0
						cv.rectangle(img,( (b*99)+10, (a*99)+10), ( (b*99)+80, (a*99)+80), (0, 0 , 0), -1)
						# print("False")
						return False 
		return True
							
delay = 1
img = np.zeros([(297*3)+50,(297*3)+10, 3], np.uint8)
# cv.namedWindow('sudoku')
# cv.createTrackbar('delay','sudoku',-5, 1000, track_callback)
drawline()
putnumber()
cv.imshow('sudoku',img)
solve(0,0)
print("Done")
cv.putText(img, '--------------------Solving Sudoku ------------------', (10, (297*3)+35), cv.FONT_HERSHEY_TRIPLEX , 0.7, (0, 0, 0), 2)
cv.putText(img, '------------------Solved Successfully -----------------------', (10, (297*3)+35), cv.FONT_HERSHEY_TRIPLEX , 0.7, (0, 255, 0), 2)
cv.imshow('sudoku', img)
# print(sudoku[1][1])
# print(sudoku)
cv.waitKey(0)