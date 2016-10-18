__author__ = 'ET'
import timeit
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
from fractions import Fraction
    
class Solution:
    # @param {Point[]} points
    # @return {integer}
    def tostring(self, point):
        return [point.x, point.y]
    
    def maxPoints(self, points):
        # problem is when two same points maps to a different point, some grad doesn't represent it correctly
        if len(points) < 3:
            return len(points)
    
        grad_list = {}
        same_point_list = {}
        for xcount, xpoint in enumerate(points):
            xpoint = self.tostring(xpoint)
    
            point_occur = same_point_list.get(str(xpoint))
            # update a list of same point occurence
            if point_occur is None:
                same_point_list.update({str(xpoint):0})
            else:
                same_point_list.update({str(xpoint):point_occur+1})

            # start to loop the 2nd point from the starting of 1st point, so it will connect every points to every points
            for ypoint in points[xcount+1:]:
                ypoint = self.tostring(ypoint)
                # calculate the grad of the line
                if ypoint[0] - xpoint[0] == 0 and ypoint[1] - xpoint[1] == 0:
                    grad = "samepoint"
                elif ypoint[0] - xpoint[0] == 0:
                    grad = "infinity"
                else:
                    grad = str(Fraction(ypoint[1] - xpoint[1], ypoint[0] - xpoint[0]))

    
                current_grad = grad_list.get(grad)
                if current_grad is None:
                    grad_list.update({grad:[[xpoint, ypoint]]})
                else:
                    inserted = False
                    # check if current grad list has the 2 points in it
                    for index, item in enumerate(current_grad):
                        if xpoint in item and ypoint not in item:
                            current_grad[index].append(ypoint)
                            inserted = True
                            break
                        elif xpoint in item and ypoint in item:
                            inserted = True
                            break
                    if not inserted:
                        current_grad.append([xpoint, ypoint])
    
        result = 0
        for grad_key, grad_items in grad_list.items():
            for grad_item in grad_items:
                real_len = len(grad_item)
                if grad_key != "samepoint":
                    for point in grad_item:
                        real_len += same_point_list.get(str(point))
                else:
                    real_len += 1
                result = max(result, real_len)
    
        return result

if __name__ == "__main__":
    # 5 0 3 2 3 3 4 3 6
    puppy = Solution()
    print puppy.maxPoints([Point(1,2), Point(2,3), Point(3,3), Point(3,4), Point(4,5), Point(5,6)])
    print puppy.maxPoints([])
    print puppy.maxPoints([Point(0,0), Point(-1,-1), Point(2,2)])
    print puppy.maxPoints([Point(0,0), Point(-1,-1), Point(1,-1)])
    print puppy.maxPoints([Point(0,0), Point(-1,-1), Point(0,0)])
    print puppy.maxPoints([Point(1,1), Point(1,1), Point(1,1)])
    print puppy.maxPoints([Point(1,1), Point(1,1), Point(2,2), Point(2,2)])
    print puppy.maxPoints([Point(-4,1), Point(-7,7), Point(-1,5), Point(9,-25)])
    print puppy.maxPoints([Point(84,250),Point(0,0),Point(1,0),Point(0,-70),Point(0,-70),Point(1,-1),Point(21,10),Point(42,90),Point(-42,-230)])
    start = timeit.default_timer()
    print puppy.maxPoints([Point(40,-23),Point(9,138),Point(429,115),Point(50,-17),Point(-3,80),Point(-10,33),Point(5,-21),Point(-3,80),Point(-6,-65),Point(-18,26),Point(-6,-65),Point(5,72),Point(0,77),Point(-9,86),Point(10,-2),Point(-8,85),Point(21,130),Point(18,-6),Point(-18,26),Point(-1,-15),Point(10,-2),Point(8,69),Point(-4,63),Point(0,3),Point(-4,40),Point(-7,84),Point(-8,7),Point(30,154),Point(16,-5),Point(6,90),Point(18,-6),Point(5,77),Point(-4,77),Point(7,-13),Point(-1,-45),Point(16,-5),Point(-9,86),Point(-16,11),Point(-7,84),Point(1,76),Point(3,77),Point(10,67),Point(1,-37),Point(-10,-81),Point(4,-11),Point(-20,13),Point(-10,77),Point(6,-17),Point(-27,2),Point(-10,-81),Point(10,-1),Point(-9,1),Point(-8,43),Point(2,2),Point(2,-21),Point(3,82),Point(8,-1),Point(10,-1),Point(-9,1),Point(-12,42),Point(16,-5),Point(-5,-61),Point(20,-7),Point(9,-35),Point(10,6),Point(12,106),Point(5,-21),Point(-5,82),Point(6,71),Point(-15,34),Point(-10,87),Point(-14,-12),Point(12,106),Point(-5,82),Point(-46,-45),Point(-4,63),Point(16,-5),Point(4,1),Point(-3,-53),Point(0,-17),Point(9,98),Point(-18,26),Point(-9,86),Point(2,77),Point(-2,-49),Point(1,76),Point(-3,-38),Point(-8,7),Point(-17,-37),Point(5,72),Point(10,-37),Point(-4,-57),Point(-3,-53),Point(3,74),Point(-3,-11),Point(-8,7),Point(1,88),Point(-12,42),Point(1,-37),Point(2,77),Point(-6,77),Point(5,72),Point(-4,-57),Point(-18,-33),Point(-12,42),Point(-9,86),Point(2,77),Point(-8,77),Point(-3,77),Point(9,-42),Point(16,41),Point(-29,-37),Point(0,-41),Point(-21,18),Point(-27,-34),Point(0,77),Point(3,74),Point(-7,-69),Point(-21,18),Point(27,146),Point(-20,13),Point(21,130),Point(-6,-65),Point(14,-4),Point(0,3),Point(9,-5),Point(6,-29),Point(-2,73),Point(-1,-15),Point(1,76),Point(-4,77),Point(6,-29)])
    print timeit.default_timer() - start