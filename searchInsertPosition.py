def searchInsert(nums,target):
	for x,d in enumerate(nums):
		if d == target:
			return x
		if d > target:
			return x

	return len(nums)



def main():
	print searchInsert([1,3,5,6],5)
	print searchInsert([1,3,5,6],2)
	print searchInsert([1,3,5,6],7)
	print searchInsert([1,3,5,6],0)
	print searchInsert([1],0)
	

if __name__ == "__main__":
	main()