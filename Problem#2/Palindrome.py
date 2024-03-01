def check_palindrome(user_input):
 #type your code here
    input_str = user_input.replace(" ", "").lower()
    if input_str == input_str[::-1]:
        print(f"palindrome: {user_input}")
    else:
        print(f"not a palindrome: {user_input}")
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
