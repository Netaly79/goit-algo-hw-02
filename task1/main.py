from datetime import datetime
from queue import Queue
import time

# create a queue
queue = Queue()
task_number = 0
i = 1

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

    while True:
        try:
            generate_request(queue)
            time.sleep(1)
            process_request(queue)
        except KeyboardInterrupt:
            break
        


if __name__ == "__main__":
    main()