import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
 	# Write your code here
  count = 0
  compliment_map = {}
  for index, item in enumerate(arr):
    compliment = abs(k - item)
    if compliment in compliment_map:
      count += compliment_map[compliment]
      
    if item not in compliment_map:
      compliment_map[item] = 0
    
    compliment_map[item] += 1
    
  return count
    
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
	print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
	global test_case_number
	result = False
	if expected == output:
		result = True
	rightTick = '\u2713'
	wrongTick = '\u2717'
	if result:
		print(rightTick, 'Test #', test_case_number, sep='')
	else:
		print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
		printInteger(expected)
		print(' Your output: ', end='')
		printInteger(output)
		print()
	test_case_number += 1

if __name__ == "__main__":
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
    k_3 = 6
    arr_3 = [1, 2, 3, 4, 2, 3, 3, 3]
    expected_3 = 8
    output_3 = numberOfWays(arr_3, k_3)
    check(expected_3, output_3)

    # Add your own test cases here
    k_4 = 6
    arr_4 = [0,0,0]
    expected_4 = 0
    output_4 = numberOfWays(arr_4, k_4)
    check(expected_4, output_4)

    # Add your own test cases here
    k_5 = 6
    arr_5 = []
    expected_5 = 0
    output_5 = numberOfWays(arr_5, k_5)
    check(expected_5, output_5)