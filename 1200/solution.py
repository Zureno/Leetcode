def minimumAbsDifference(arr):
	arr.sort()
	rm = min(b-a for a,b in zip(arr,arr[1:]))
	return ([a,b] for a,b in zip(arr,arr[1:)] if b-a == rm])
