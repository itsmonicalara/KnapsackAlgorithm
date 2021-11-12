from backpack import *
from item import *

# Knapsack 0/1 - Takes objects in whole numbers. Brute Force.
# Time Complexity: O(2^n).
def knapsack_recursive(capacity, weight, value, n):
	# Base case
	if(n == 0 or capacity == 0):
		return 0
	# The objects weights more than the backpack.
	if(weight[n-1] > capacity):
		return knapsack_recursive(capacity, weight, value, n-1)
	else:
		# The object fits in the backpack
		return max(value[n-1] + knapsack_recursive(capacity - weight[n-1], weight, value, n-1), knapsack_recursive(capacity, weight, value, n-1))

# Knapsack Tabulated -  Dynammic Programming (Recursive to iterative). Divided into subproblems.
# Time Complexity: O(N*W).
def knapsack_tabulated(capacity, weight, value, n , name):
	# Create a table to store the results of subproblems
	table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
	# Fill the entries for 0th item
	for i in range(0, capacity + 1):
		table[0][i] = 0
	# Fill the entries for 0th item
	for i in range(0, n + 1):
		table[i][0] = 0
	# Fill rest of the entries in bottom-up manner
	for i in range(1, n + 1):
		for w in range(1, capacity + 1):
			if(weight[i-1] <= w):
				table[i][w] = max(value[i-1] + table[i-1][w-weight[i-1]], table[i-1][w])
			else:
				table[i][w] = table[i-1][w]
	# Stores the result of Knapsack
	res = table[n][capacity]
	print('Optimal value of the backpack: ', res)
	# Return list of items selected
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
	return name_items


# Knapsack - Dynamic Programming approach with optimized space complexity. 
# Time Complexity: O(N*W).
# Space Complexity: O(W). 1D list is used instead of 2D list.
def knapsack_optimized(capacity, weight, value, n):
	list = [0 for i in range(capacity + 1)] 
	for i in range(1, n + 1):
		for j in range(capacity, 0, -1):
			# If the weight of the object is less than the capacity, add it to the knapsack.
			if weight[i-1] <= j: 
				list[j] = max(list[j], list[j-weight[i - 1]] + value[i - 1])
	return list[capacity]
	
# Knapsack Memoization - Extension of recursive for redundant calculations and increased time complexity.
# Time Complexity: O(N*W).
def knapsack_memoization(capacity, weight, value, n):
	# It is necessary to to initialize the list with a -1 at the start.
	list = [[-1 for x in range(capacity + 1)] for x in range(n + 1)]
	# Base case
	if(n == 0 or capacity == 0):
		return 0
	# Check if the combination of n and capacity is not already calculated.
	if(list[n-1][capacity] != -1):
			return list[n-1][capacity]
	# The object weights less than the backpack.
	if(weight[n-1] <= capacity):
		list[n][capacity] = max(value[n-1] + knapsack_memoization(capacity - weight[n-1], weight, value, n-1), knapsack_memoization(capacity, weight, value, n-1))
		return list[n][capacity]
	# The object does not fit in the backpack.
	elif(weight[n-1] > capacity):
		list[n][capacity] = knapsack_memoization(capacity, weight, value, n-1)
		return list[n][capacity]

# Knapsack - Fractional. You can take fractional number of objects.
# Time Complexity O(n*log*n)
def knapsack_fractional(capacity, weight, value, n, name):
	my_list = list(range(n))
	ratio = [v/w for v, w in zip(value, weight)]
	# Sort the list in descending order of value/weight ratio.
	my_list.sort(key=lambda i:ratio[i], reverse=True)
	total_value = 0
	fractions = [0]*len(value)
	for i in my_list:
		if weight[i] <= capacity:
			fractions[i] = 1
			total_value += value[i]
			capacity -= weight[i]
		else:
			fractions[i] = capacity/weight[i]
			total_value += value[i]*capacity/weight[i]
			break
	print('Optimal value of the backpack: ', total_value)
	test = [i for i in zip(name, fractions)]
	return test

# Knapsack Backtracking
def knapsack_backtracking(capacity, weight, value, n):
	return

# Knapsack Branch and Bound
def knapsack_branch_and_bound(capacity, weight, value, n):
	return

# Knapsack - Greedy Technique
def knapsack_greedy(capacity, weight, value, n):
	return



if __name__ == '__main__':
	# Test case 1
	# capacity = 50
	# item1 = Item(10, 60, "Acta de nacimiento")
    # item2 = Item(20, 100, "Agua")
    # item3 = Item(30, 120, "Medicinas") 
	# Expected output: 220
	print('Knapsack Program\n')
	capacity = int(input('Enter the capacity of the backpack: '))
	backpack = Backpack(capacity)
	n = int(input("How many items do you want to choose? "))
	for i in range(n):
		name = input("Enter the name of the item: ")
		weight = int(input("Enter the weight of the item: "))
		value = int(input("Enter the value of the item: "))
		item = Item(weight, value, name)
		backpack.new_format(item)

	print('\nKnapsack Tabulated 1/0:')
	accepted_items = knapsack_tabulated(backpack.capacity, backpack.weight_list, backpack.values_list, n, backpack.names_list)
	backpack.list_items = accepted_items
	backpack.get_items()

	accepted_items2 = knapsack_fractional(backpack.capacity, backpack.weight_list, backpack.values_list, n, backpack.names_list)
	backpack.list_items = accepted_items2
	backpack.get_items()

	# print(knapsack_recursive(capacity, weight, value, n))
	# print(knapsack_memoization(capacity, weight, value, n))
	#print(knapsack_optimized(capacity, weight, value, n))
	# table = knapsack_tabulated(capacity, weight, value, n)
	# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in table]))
