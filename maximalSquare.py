__author__ = 'ET'

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        pepsi = []
        for row in matrix:
            cola = []
            for index, item in enumerate(row):
                if item == 1:
                    cola.append(index)
            print cola
            sprite = []
            for index, item in enumerate(cola[:-1]):
                sprite.append(item)
                if cola[index+1] == (item + 1):
                    sprite.append(cola[index+1])
                else:
                    print sprite
                    pepsi.append(sprite)
                    sprite = []
        print pepsi

if __name__ == "__main__":
    puppy = Solution()
    print puppy.maximalSquare([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])
    # print puppy.maximalSquare(1)
    # print puppy.maximalSquare(5)
    # print puppy.maximalSquare(20)
    # print puppy.maximalSquare(100)