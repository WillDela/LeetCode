def get_highest_priority_task():

  highest_priority = max(tasks, key=tasks.get)
  for priority in tasks:
    if priority > highest_priority:
      highest_priority = priority


tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)