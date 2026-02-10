import validators
import sys

def main():
    email_input = input("What's your email address? ") 

    try:
        valid = validators.email(email_input, r_ve=True)
    except validators.utils.ValidationError:
        print("Invalid")
    else:
        print("Valid")



if __name__ == "__main__":
    main()
