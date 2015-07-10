def rotate(matrix):
    length = len(matrix) - 1

# when x = 0, y = 1 length = 3
# [0][1] <- [2][0] <- [3][2] <- [1][3] <- [0][1]
    for x in range(0, len(matrix)/2):
        for y in range(x, length-x):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[length-y][x]
            matrix[length-y][x] = matrix[length-x][length-y]
            matrix[length-x][length-y] = matrix[y][length-x]
            matrix[y][length-x] = tmp
            
    return matrix

def main():
    print rotate([[1,3,5,7],[10,11,16,20],[23,30,34,50],[23,30,34,50]])
    print rotate([[1,2,3],[4,5,6],[7,8,9]])
    print rotate([[1,2],[3,4]])
    print rotate([[1]])

if __name__ == "__main__":
	main()