"""

Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

def cast_vote(votes, candidate):
    pass
Example Usage:

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
Example Output:

{"Alice": 6, "Bob": 3}
{"Alice": 6, "Bob": 3, "Gina": 1}

  """
  

def cast_vote(votes, candidate):
  
  # vote_dict.setdefault(candidate, 0)
  # vote_dict[candidate] += 1
  
  if candidate in votes:
    votes[candidate] += 1
  else:
    votes[candidate] = 1
    
  return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)