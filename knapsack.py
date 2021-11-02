# Knapsack 0/1 - Takes objects in whole numbers.
def knapsack_recursive(capacity, weight, value, n):
	# Base case
	if(n == 0 or capacity == 0):
		return 0;
	# The objects weights more than the backpack
	if(weight[n-1] > capacity):
		return knapsack_recursive(capacity, weight, value, n-1);
	else:
		# The object fits in the backpack
		return max(value[n-1] + knapsack_recursive(capacity - weight[n-1], weight, value, n-1), knapsack_recursive(capacity, weight, value, n-1));

# Knapsack Tabulated -  Dynammic Programming (Recursive to iterative)
def knapsack_tabulated(capacity, weight, value, n):
	# Create a table to store the results of subproblems
	K = [[0 for x in range(capacity + 1)] for x in range(n + 1)];
	# Fill the entries for 0th item
	for i in range(0, capacity + 1):
		K[0][i] = 0;
	# Fill the entries for 0th item
	for i in range(0, n + 1):
		K[i][0] = 0;
	# Fill rest of the entries in bottom-up manner
	for i in range(1, n + 1):
		for w in range(1, capacity + 1):
			if(weight[i-1] <= w):
				K[i][w] = max(value[i-1] + K[i-1][w-weight[i-1]], K[i-1][w]);
			else:
				K[i][w] = K[i-1][w];
	return K[n][capacity];

# Knapsack Memoization
def knapsack_memoization(capacity, weight, value, n):
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
	capacity = 50;
	weight = [10, 20, 30];
	value = [60, 100, 120];
	n = len(weight);
	print(knapsack_recursive(capacity, weight, value, n));
	print(knapsack_tabulated(capacity, weight, value, n));
	# Output: 220
	# Explanation: The optimal solution is to take the first, the second and the fourth item.
	# The total value is 1 + 4 + 7 = 13.
	# The backpack cannot hold the fifth item, so we ignore it.
	# The backpack can hold the first, second and third item.
	# The total value is 1 + 4 + 5 = 9.
	# The backpack can hold the first and second item.
