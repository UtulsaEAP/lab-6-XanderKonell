def process_and_print(input_string):
      # Split into separate strings
    numbers = input_string.split()
    # Convert strings to integers and filter out negative values
    numbers = [int(num) for num in numbers]
    negative_numbers = [num for num in numbers if num < 0]
    # Sort integers in reverse order
    negative_numbers.sort(reverse=True)
    # Print sorted integers
    for num in negative_numbers:
        print(num, end=" ")

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)