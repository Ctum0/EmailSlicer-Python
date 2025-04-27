"""
Title: Email Slicer
Description: A simple program to extract username and domain from an email address.
Author: Sithum Ranasinghe
"""

def main():
    email = input("Enter Your Email Address: ").strip()

    try:
        index = email.index("@")  # Finds the index of the @ symbol
        username = email[:index]  # Username is from start till @
        domain = email[index+1:]  # Domain is after @

        print(f"Your Username is '{username}' and Domain is '{domain}'.")
    except ValueError:
        print("Invalid Email Address. Please include '@' symbol.")

if __name__ == "__main__":
    main()
