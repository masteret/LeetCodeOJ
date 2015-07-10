def isPalindrome(s):
	if (len(s) < 2):
		return True

	l = list()
	for x in list(s.lower()):
		if (((ord(x)) > 96 and (ord(x) < 123)) or ((ord(x)) > 47 and (ord(x) < 58))):
			l.append(x)
	# print l

	for x in range(0, len(l)/2):
		if (l[x] != l[len(l)-x-1]):
			# print str(l[x]), "doesn't match", str(l[len(l) - x])
			return False

	return True



def main():
	print isPalindrome("A man, a plan, a canal: Panama")
	print isPalindrome("race a car")

if __name__ == "__main__":
	main()