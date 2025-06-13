"""

Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.

def common_keys(dict1, dict2):
	pass
Example Usage:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
Example Output:

['b', 'c']
"""

def common_keys(dict1, dict2):
  common = []
 
  for key in dict1:
    if key in dict2:
      common.append(key)
      
  return common


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)