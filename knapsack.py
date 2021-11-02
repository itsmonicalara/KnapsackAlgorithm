# Knapsack 0/1 - Takes objects in whole numbers.
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

# Knapsack Tabulated -  Dynammic Programming (Recursive to iterative).
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
	return table[n][capacity]

# Knapsack - Dynamic Programming approach with optimized space complexity.
# Time Complexity: O(N*W).
# Space Complexity: O(W). 1D list is used instead of 2D list.
def knapsack_optimized(capacity, weight, value, n, list):
	for i in range(1, n + 1):
		for j in range(capacity, 0, -1):
			if weight[i-1] <= j:
				list[j] = max(list[j], list[j-weight[i - 1]] + value[i - 1])
	return list[capacity]
	
# Knapsack Memoization - Extension of recursive for redundant calculations and increased time complexity.
# Time Complexity: O(N*W).
def knapsack_memoization(capacity, weight, value, n, list):
	# It is necessary to to initialize the list with a -1 at the start.
	# Base case
	if(n == 0 or capacity == 0):
		return 0
	# Check if the combination of n and capacity is not already calculated.
	if(list[n-1][capacity] != -1):
			return list[n-1][capacity]
	# The object weights less than the backpack.
	if(weight[n-1] <= capacity):
		list[n][capacity] = max(value[n-1] + knapsack_memoization(capacity - weight[n-1], weight, value, n-1, list), knapsack_memoization(capacity, weight, value, n-1, list))
		return list[n][capacity]
	# The object does not fit in the backpack.
	elif(weight[n-1] > capacity):
		list[n][capacity] = knapsack_memoization(capacity, weight, value, n-1, list)
		return list[n][capacity]

# Knapsack - Fractional 
def knapsack_fractional(capacity, weight, value, n):
	return

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
	list = [[-1 for x in range(capacity + 1)] for x in range(n + 1)]
	list_2 = [0 for i in range(capacity + 1)] 
	print(knapsack_recursive(capacity, weight, value, n))
	print(knapsack_tabulated(capacity, weight, value, n))
	print(knapsack_memoization(capacity, weight, value, n, list))
	print(knapsack_optimized(capacity, weight, value, n, list_2))
	# Output: 220
