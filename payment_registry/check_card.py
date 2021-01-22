def qvS923GxFE2VPWBH9UJsSw(cardnum):

	nDigits = len(cardnum)
	nSum = 0
	isSecond = False

	for i in range(nDigits-1, -1,-1):
		d = ord(cardnum[i])-ord('0')

		if(isSecond == True):
			d=d*2
		nSum += d // 10
		nSum += d % 10

		isSecond = not isSecond

	if(nSum % 10 == 0):
		return True
	else:
		return False
