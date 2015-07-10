def maxPoints(points):
	count = {}
	if len(points) == 0:
		return 0
	if len(points) == 1:
	    return 1
	for x in range(0,len(points)):
		for y in range(x+1, len(points)):
			if (points[y][0]-points[x][0]) == 0:
				g = 0.0
			else:
				g = float(points[y][1]-points[x][1])/(points[y][0]-points[x][0])
			if str([y,g]) in count:
				count[str([y,g])] += 1
			else:
				count.update({str([y,g]):2})
	return max(count.values())

def main():
	print maxPoints([])
	print maxPoints([[0,0],[0,0]])
	# same point case
	print maxPoints([[0,0],[1,1],[0,0]])
	print maxPoints([[0,0],[1,2],[3,1],[2,4],[5,3],[3,6]])

if __name__ == "__main__":
	main()