amount_due = 50
acceptable_coins = [25, 10, 5]

while amount_due > 0:
	print(f"Amount Due: {amount_due}")
	coin_inserted = int(input("Insert Coin: "))
	if coin_inserted in acceptable_coins:
		amount_due -= coin_inserted 
		
print(f"Change Owed: {abs(amount_due)}")




