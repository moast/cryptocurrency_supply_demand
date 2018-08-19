##Crypto Coin Buy/Sell Based On Demand/Supply##

while 1:
	print("########### PROGRAM INFO ##########")
	print("Supply is the Circulating supply value")
	print("Demand is the Market Cap")
	print("##################################")

	supply = int(input("Please enter supply: "))
	current_price = float(input("Please enter current price of Coiin in USD: "))
	demand = int(input("Please enter Market cap value: "))

    print("###############################")
	print("What Should I DO?")
	if supply>demand:
		print("price will go down! sell")
	elif demand>supply:
		print("price will go up! buy") 	
	else:
		print("wait!")
	print("################################")
	print("")       