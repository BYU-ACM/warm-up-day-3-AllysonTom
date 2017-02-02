def Coin_Combinations(coins, value):
	"""
	   	A Generalized solution to the coins problem provided by project euler #31
	    Read it for more specifications
	    coins: a list of coins that can be used
	    value: the value that the coins should add to
	    returns:
	    number of possible combinations to make value with given coins in "coins"
	"""
	my_list = [0]*(value+1)
	my_list[0] = 1
  	#print my_list
  	for coin in coins:
  		new_list = [0]*(value+1)
  		my_list[0] = 1
  		for i in xrange(0, value+1):
  			new_list[i] = new_list[i - coin] + my_list[i]
  		my_list = new_list
  	return new_list[-1]
