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

if __name__ == '__main__':
	capacity = 10;
	weight = [1, 2, 3, 4, 5];
	value = [1, 4, 5, 7, 9];
	n = len(weight);
	print(knapsack_recursive(capacity, weight, value, n));
	# Output: 13
	# Explanation: The optimal solution is to take the first, the second and the fourth item.
	# The total value is 1 + 4 + 7 = 13.
	# The backpack cannot hold the fifth item, so we ignore it.
	# The backpack can hold the first, second and third item.
	# The total value is 1 + 4 + 5 = 9.
	# The backpack can hold the first and second item.
