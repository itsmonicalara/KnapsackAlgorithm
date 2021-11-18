# Knapsack Tabulated -  Dynammic Programming (Recursive to iterative). Divided into subproblems.
# Time Complexity: O(N*W).
def tabulated(backpack, items):
	# Create a table to store the results of subproblems
	table = [[0 for x in range(backpack.capacity + 1)] for x in range(backpack.total + 1)]
	# Fill the entries for 0th item
	for i in range(0, backpack.capacity + 1):
		table[0][i] = 0
	# Fill the entries for 0th item
	for i in range(0, backpack.total + 1):
		table[i][0] = 0
	# Fill rest of the entries in bottom-up manner
	for i in range(1, backpack.total + 1):
		for w in range(1, backpack.capacity + 1):
			if(items[i-1].weight <= w):
				table[i][w] = max(items[i-1].value + table[i-1][w-items[i-1].weight], table[i-1][w])
			else:
				table[i][w] = table[i-1][w]
	# Stores the result of Knapsack
	backpack.opt_value = table[backpack.total][backpack.capacity]
	backpack.pack_unpack_items(items, table)
	
	

# # Test case 1
# backpack = Knapsack(50,3)
# #Item(w,v,name)
# item1 = Item(10, 60, "Acta de nacimiento") 
# item2 = Item(20, 100, "Agua") 
# item3 = Item(30, 120, "Medicinas") 
# # Expected output: 220
# items = [item1, item2, item3]
# tabulated(backpack, items)
# print(str(backpack))