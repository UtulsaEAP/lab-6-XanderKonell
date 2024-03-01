def process_user_contacts(user_input):
    user_contacts = {}
    tokens = user_input.split()

    # Put word pairs into a dictionary
    for i in range(0, len(tokens), 2):
        user_contacts[tokens[i]] = tokens[i + 1]
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    print(user_contacts.get(contact_name, "Contact not found"))

   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)