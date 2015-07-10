__author__ = 'ET'

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def tostring(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

# @param {Point[]} points
# @return {integer}
def maxPoints(points):
    if len(points) < 3:
        return len(points)

    result = 0
    for xcount, xpoint in enumerate(points[:-1]):
        count = {}
        same = 0
        for ypoint in points[xcount+1:]:
            if ypoint.x - xpoint.x == 0:
                grad = 0.0
            else:
                grad = float((ypoint.y - xpoint.y)/(ypoint.x - xpoint.x))

            if xpoint.x == ypoint.x and xpoint.y == ypoint.y:
                same += 1
            else:
                if count.get(grad) is None:
                    count.update({grad:2})
                else:
                    count.update({grad:count.get(grad)+1})
        if len(count) != 0:
            for key, val in count.items():
                count.update({key:val+same})
            result = max(result, max(count.values()))
        elif len(count) == 0 and same != 0:
            result = max(result,same+1)

    return result

if __name__ == "__main__":
    # 5 0 3 2 3 3 4
    print maxPoints([Point(1,2), Point(2,3), Point(3,3), Point(3,4), Point(4,5), Point(5,6)])
    print maxPoints([])
    print maxPoints([Point(0,0), Point(-1,-1), Point(2,2)])
    print maxPoints([Point(0,0), Point(-1,-1), Point(1,-1)])
    print maxPoints([Point(0,0), Point(-1,-1), Point(0,0)])
    print maxPoints([Point(1,1), Point(1,1), Point(1,1)])
    print maxPoints([Point(1,1), Point(1,1), Point(2,2), Point(2,2)])