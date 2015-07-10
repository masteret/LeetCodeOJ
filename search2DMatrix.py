def searchMatrix(matrix, target):
    row = 0
    col = len(matrix[0])-1
    while (row < len(matrix) and col < len(matrix[0]) and row > -1 and col > -1):
    	if (matrix[row][col] < target):
    		row += 1
    		col = len(matrix[0])-1
    	elif (matrix[row][col] > target):
    		col -= 1
    	else:
    		return True
    return False

def main():
	print searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 23)
	print searchMatrix([[1]], 0)

if __name__ == "__main__":
	main()