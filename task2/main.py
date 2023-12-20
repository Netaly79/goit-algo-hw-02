from collections import deque

def sanitize_string (my_string):
    return my_string.lower().replace(" ", "")

def check_is_palindrome(input_string):
    char_queue = deque(input_string)
    
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

def main():
  input_string = input ("Give me your string or press 0 to finish   ")
  while input_string != '0':
    sanitized_string = sanitize_string(input_string)
    result = check_is_palindrome(sanitized_string)

    if result:
        print(f'String "{input_string}" is a palindrome.')
    else:
        print(f'String "{input_string}" is not palindrome.')
    
    input_string = input ("Give me your string or press 0 to finish   ")

if __name__ == "__main__":
    main()