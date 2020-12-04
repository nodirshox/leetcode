func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	isEqual := false
	if concatenateStrings(word1) == concatenateStrings(word2) {
		isEqual = true
	}
	return isEqual
}

func concatenateStrings(words []string) string {
	concatenated := ""
	for i := 0; i < len(words); i++ {
		concatenated += words[i]
	}
	return concatenated
}