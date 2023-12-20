from datetime import datetime
from queue import Queue

# create a queue
queue = Queue()
task_number = 0

def generate_request(queue):
  global task_number
  new_task = { "task_number": task_number, "task_time": datetime.today() }
  task_number += 1
  queue.put(new_task) 

def process_request(queue):
    if not queue.empty():
        my_task = queue.get()
        print ("Task with task number ", my_task["task_number"], '-', my_task["task_time"], ' is running')
    else:
        print ("Queue is empty")

def main():
    print ("Starting...")
    i = 1
    while i != '0':
        generate_request(queue)
        process_request(queue)
        i = input ("press any key to continue... or press 0 to finish program  ")

if __name__ == "__main__":
    main()