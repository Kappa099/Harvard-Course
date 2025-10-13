from validator_collection import validators, errors

def main():
    email = input("What's your email address? ")
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

def is_valid_email(address):
    try:
        validators.email(address)
        return True
    except errors.InvalidEmailError:
        return False
    except Exception:
        return False

if __name__ == "__main__":
    main()