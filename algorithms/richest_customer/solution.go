func maximumWealth(accounts [][]int) int {
	wealth := 0

	for i := 0; i < len(accounts); i++ {
		oneCustomer := accounts[i]
		customerWealth := 0

		for j := 0; j < len(oneCustomer); j++ {
			customerWealth += oneCustomer[j]
		}
		if wealth < customerWealth {
			wealth = customerWealth
		}
	}

	return wealth
}