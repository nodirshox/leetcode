package main

import "fmt"

func shuffle(nums []int, n int) []int {
	var shufledArray []int

	for i := 0; i < n; i++ {
		shufledArray = append(shufledArray, nums[i])
		shufledArray = append(shufledArray, nums[i+n])
	}

	return shufledArray
}

func main() {
	numbers := []int{2, 5, 1, 3, 4, 7}
	fmt.Println(shuffle(numbers, 3))
}
