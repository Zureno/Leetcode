def minimumAbsDifference(arr):
	arr.sort()  #sort the array 
	rm = min(b-a for a,b in zip(arr,arr[1:])) #use zip to find the minimum between two consecutive pairs.
	return ([a,b] for a,b in zip(arr,arr[1:)] if b-a == rm]) #return the pair whose difference is equal to minimum.
