# O(nLogn) Time O(1) Space
def nonConstructibleChange(coins):
	summed_coins = 0
	if len(coins) == 0:
		return 1
	else:
		coins.sort()
		for coin in coins:
			if coin > summed_coins +1:
				return summed_coins + 1
			summed_coins +=coin
			
	return summed_coins+1


coins = [5, 7, 1, 1, 2, 3, 22]
nonConstructibleChange(coins)
