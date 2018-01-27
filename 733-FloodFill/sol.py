class Solution(object):
    def helper(self, sr, sc, newColor, oldColor, from_dir):
        if sr >= 0 and sr < len(self.image) and sc >= 0 and sc < len(self.image[0]) and self.travelled[sr][sc] == 0:
            if oldColor == self.image[sr][sc]:
                self.image[sr][sc] = newColor
                self.travelled[sr][sc] = 1
                if from_dir == "left":
                    self.helper(sr-1, sc, newColor, oldColor, "down")
                    self.helper(sr+1, sc, newColor, oldColor, "up")
                    self.helper(sr, sc+1, newColor, oldColor, "left")
                elif from_dir == "right":
                    self.helper(sr-1, sc, newColor, oldColor, "down")
                    self.helper(sr+1, sc, newColor, oldColor, "up")
                    self.helper(sr, sc-1, newColor, oldColor, "right")
                elif from_dir == "up":
                    self.helper(sr, sc-1, newColor, oldColor, "right")
                    self.helper(sr+1, sc, newColor, oldColor, "up")
                    self.helper(sr, sc+1, newColor, oldColor, "left")
                elif from_dir == "down":
                    self.helper(sr-1, sc, newColor, oldColor, "down")
                    self.helper(sr, sc-1, newColor, oldColor, "right")
                    self.helper(sr, sc+1, newColor, oldColor, "left")
                else:
                    self.helper(sr-1, sc, newColor, oldColor, "down")
                    self.helper(sr+1, sc, newColor, oldColor, "up")
                    self.helper(sr, sc+1, newColor, oldColor, "left")
                    self.helper(sr, sc-1, newColor, oldColor, "right")

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        self.travelled = [[0 for x in self.image[0]] for y in self.image]
        self.helper(sr, sc, newColor, self.image[sr][sc], "")
        return self.image