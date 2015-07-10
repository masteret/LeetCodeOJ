__author__ = 'ET'

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = float(a)
        self.y = float(b)

    def tostring(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

# @param {Point[]} points
# @return {integer}
def maxPoints(points):
    if len(points) < 3:
        return len(points)

    grad_list = {}
    same_list = {}
    for xcount, xpoint in enumerate(points[:-1]):
        same = 0
        for ypoint in points[xcount+1:]:
            if ypoint.x - xpoint.x == 0:
                grad = -1.0
            else:
                grad = (ypoint.y - xpoint.y)/(ypoint.x - xpoint.x)

            if xpoint.x == ypoint.x and xpoint.y == ypoint.y:
                if same_list.get(xpoint.tostring()) is None:
                    same_list.update({xpoint.tostring():0})
                else:
                    same_list.update({xpoint.tostring():same_list.get(xpoint.tostring())+1})

            if grad_list.get(grad) is None:
                grad_list.update({grad:[[xpoint.tostring(), ypoint.tostring()]]})
            else:
                inserted = False
                for index, item in enumerate(grad_list.get(grad)):
                    if xpoint.tostring() in item and ypoint.tostring() not in item:
                        # print xpoint.tostring(), item
                        grad_list.get(grad)[index] += [ypoint.tostring()]
                        inserted = True
                    elif xpoint.tostring() not in item and ypoint.tostring() in item:
                        # print xpoint.tostring(), item
                        grad_list.get(grad)[index] += [xpoint.tostring()]
                        inserted = True
                    elif xpoint.tostring() in item and ypoint.tostring() in item:
                        inserted = True
                if not inserted:
                    print xpoint.tostring(), ypoint.tostring(), "not inserted in", grad_list.get(grad)
                    grad_list.update({grad:grad_list.get(grad).extend([xpoint.tostring(), ypoint.tostring()])})

    for key, item in grad_list.items():
        print key, item
    for key, item in same_list.items():
        print key, item
    return None

if __name__ == "__main__":
    # 5 0 3 2 3 3 4
    print maxPoints([Point(1,2), Point(2,3), Point(3,3), Point(3,4), Point(4,5), Point(5,6)])
    # print maxPoints([])
    # print maxPoints([Point(0,0), Point(-1,-1), Point(2,2)])
    # print maxPoints([Point(0,0), Point(-1,-1), Point(1,-1)])
    # print maxPoints([Point(0,0), Point(-1,-1), Point(0,0)])
    # print maxPoints([Point(1,1), Point(1,1), Point(1,1)])
    # print maxPoints([Point(1,1), Point(1,1), Point(2,2), Point(2,2)])