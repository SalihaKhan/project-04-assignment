def get_user_data():
    """Collects and returns user's first name, last name, and email as a tuple."""
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email  # Returns as a tuple

# Example usage:
user_data = get_user_data()
print(f"Received the following user data: {user_data}")