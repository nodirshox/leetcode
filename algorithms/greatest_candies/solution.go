func kidsWithCandies(candies []int, extraCandies int) []bool {
	var answers []bool

	for i := 0; i < len(candies); i++ {
		selectedKid := candies[i] + extraCandies

		isBigger := true
		for j := 0; j < len(candies); j++ {
			if selectedKid < candies[j] {
				isBigger = false
			}
		}

		answers = append(answers, isBigger)
	}

	return answers
}