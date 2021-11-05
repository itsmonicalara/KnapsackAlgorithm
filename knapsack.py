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
def knapsack_tabulated(capacity, weight, value, n):
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
	print(table[n][capacity])		
	return table


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
def knapsack_fractional(capacity, weight, value, n):
	list = []
	for i in range(n):
		# Join weight, value and index in a single list.
		list.append((weight[i], value[i], i))
	# Sort the list in descending order of value/weight ratio.
	list.sort(key=lambda tup: tup[1]/tup[0], reverse=True)
	total_value = 0
	for i in list:
		# If the weight of the object is less than the capacity, add it to the knapsack.
		if(capacity >= i[0]):
			# Add the value of the object to the total value.
			total_value += i[1]
			# Reduce the capacity by the weight of the object.
			capacity -= i[0]
		else:
			# If the weight of the object is more than the capacity, add the fractional part of the object to the knapsack.
			total_value += capacity * i[1]/i[0]
			break
	return total_value

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
	capacity = 50
	weight = [10, 20, 30]
	value = [60, 100, 120]
	n = len(weight)
	print('Maximum value that can be stored in the bag: ', knapsack_recursive(capacity, weight, value, n))
	print(knapsack_memoization(capacity, weight, value, n))
	print(knapsack_optimized(capacity, weight, value, n))
	print(knapsack_fractional(capacity, weight, value, n))
	# print(knapsack_tabulated(capacity, weight, value, n))
	table = knapsack_tabulated(capacity, weight, value, n)
	print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in table]))
	# Output: 220
