import math

# def trailingZeroes(n):
# 	o = str(math.factorial(n))
# 	count = 0
# 	for x in reversed(range(0, len(o))):
# 		if o[x] == '0':
# 			count += 1
# 		else:
# 			return count

def trailingZeroes(n):
	if n == 0:
		return 0
	result = 0
	for x in range(1,1+int(math.log(n,5))):
		result += n/int(math.pow(5,x))
	return result

def main():
	for x in range(1, 51):
		print trailingZeroes(x*5)
		# trailingZeroes(x*5)

if __name__ == "__main__":
	main()