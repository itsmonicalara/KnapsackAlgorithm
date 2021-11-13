from knapsack import Knapsack
from item import Item

# Knapsack Tabulated -  Dynammic Programming (Recursive to iterative). Divided into subproblems.
# Time Complexity: O(N*W).
def tabulated(backpack, items, n):
	# Create a table to store the results of subproblems
	table = [[0 for x in range(backpack.capacity + 1)] for x in range(n + 1)]
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
	print('Optimal value of the backpack: ', backpack.opt_value)
	
	items = []
	name_items = []
	for i in range(n, 0, -1):
		if res <= 0:
			break
		if res == table[i - 1][capacity]:
			continue
		else:
			# Just in case we need weight and values of selected items
			items.append([weight[i - 1], value[i - 1]])
			name_items.append(name[i - 1])
			res = res - value[i - 1]
			capacity = capacity - weight[i - 1]
	

if __name__ == '__main__':
	# Test case 1
	backpack = Knapsack(50)
	#Item(w,v,name)
	item1 = Item(10, 60, "Acta de nacimiento") 
	item2 = Item(20, 100, "Agua") 
	item3 = Item(30, 120, "Medicinas") 
	# Expected output: 220
	items = [item1, item2, item3]
	tabulated(backpack, items)
