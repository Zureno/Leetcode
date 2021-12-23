def reorderLogFiles(logs):
	digits = []
	letters = []
	for log in logs:
		if log.split()[1].isdigit():
			digits.append(log)
		else:
			letter.append(log)
	letters.sort(key = lambda x: x.split()[1])
	letters.sort(key= lambda x: x.split()[1:])
	result = letters + digit
	return result
