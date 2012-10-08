import time
tiempo = time.time()
def quickSort(toSort):
	if len(toSort) <= 1:
		return toSort
	end = len(toSort) - 1
	pivot = toSort[end]
	low = []
	high = []
	for num in toSort[:end]:
		if num <= pivot:
			low.append(num)
		else:
			high.append(num)

	sortedList = quickSort(low)
	sortedList.append(pivot)
	sortedList.extend(quickSort(high))

	return sortedList

def main():
        
	l = [3,8,2,1, 6, 7, 2, 76, 45, 23, 4, 8, 12, 11]
	sortedList = quickSort(l)
	print sortedList
	print time.time()-tiempo

if __name__ == '__main__':
	main()
