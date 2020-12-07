import "strconv"

func fizzBuzz(n int) []string {
	var word []string

	count := 1

	for count <= n {
		if count%3 == 0 && count%5 == 0 {
			word = append(word, "FizzBuzz")
		} else if count%3 == 0 {
			word = append(word, "Fizz")
		} else if count%5 == 0 {
			word = append(word, "Buzz")
		} else {
			word = append(word, strconv.Itoa(count))
		}
		count += 1
	}

	return word
}