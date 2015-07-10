def isIsomorphic(s, t):
	if (len(s) < 2): 
		return True

	listA = [128] * 128
	listB = [128] * 128

	for x, d in enumerate(s):
		# x is index d is element
		# str(s[x]) is char in s, str(t[x]) is char in t
		# print "comparing", str(s[x]), str(t[x])
		a = ord(str(s[x]))
		b = ord(str(t[x]))

		if (listA[a] != 128):
			if (listA[a] != b): 
				return False
		else:
			listA[a] = b

		if (listB[b] != 128):
			if (listB[b] != a):
				return False
		else:
			listB[b] = a

	return True

def main():
	print isIsomorphic("egg", "add")
	print isIsomorphic("foo", "bar")
	print isIsomorphic("paper", "title")
	print isIsomorphic("ab", "aa")
	print isIsomorphic("13", "42")

if __name__ == "__main__":
	main()