def permutations(nums):
	result = []
	length = len(nums)
	
	if length == 1:
		result.append(nums)
	else:
		elem = nums.pop(0)
		for x in permutations(nums):
			xlength = len(x)
			for y in range(0, xlength+1):
				z = list(x)
				z.insert(y, elem)
				result.append(z)

	return result

def main():
	print permutations([1,2,3])

if __name__ == "__main__":
	main()