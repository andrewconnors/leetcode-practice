import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  # Write your code here
  contains_map = {}
  for a in array_a:
    if a not in contains_map:
      contains_map[a] = 0
    contains_map[a] += 1
  
  for b in array_b:
    if b in contains_map:
      contains_map[b] -=1
      if contains_map[b] < 0:
        return False
    else:
      return False
  
  for item in contains_map.keys():
    if contains_map[item] < 0:
      return False
  return True


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here