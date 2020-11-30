func sumZero(n int) []int {
	var uniqueIntegers []int
	if n%2 == 1 {
		uniqueIntegers = append(uniqueIntegers, 0)
		n -= 1
	}

	for i := 1; i <= n/2; i++ {
		uniqueIntegers = append(uniqueIntegers, i*(-1))
		uniqueIntegers = append(uniqueIntegers, i)
	}

	return uniqueIntegers
}