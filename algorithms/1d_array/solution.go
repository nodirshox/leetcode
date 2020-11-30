package main

import "fmt"

func runningSum(nums []int) []int {
	var sumNumbers []int
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
		sumNumbers = append(sumNumbers, sum)
	}
	return sumNumbers
}

func main() {
	numbers := []int{1, 2, 3, 4}
	fmt.Println(runningSum(numbers))
}
