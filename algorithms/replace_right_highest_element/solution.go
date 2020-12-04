func replaceElements(arr []int) []int {
	var newOrder []int
	for i := 0; i < len(arr)-1; i++ {
		slicedArr := arr[i+1 : len(arr)]
		newOrder = append(newOrder, takeMax(slicedArr))
	}
	newOrder = append(newOrder, -1)
	return newOrder
}

func takeMax(sliced []int) int {
	max := sliced[0]
	for i := 0; i < len(sliced); i++ {
		if max < sliced[i] {
			max = sliced[i]
		}
	}
	return max
}