def check_password(password_text):
    """
    Validates a password against security requirements.

    Requirements:
    - Minimum length of 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)

    Args:
        password_text (str): The password to validate

    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    # Initialize error message
    error_message = ""

    # Check minimum length
    if len(password_text) < 8:
        return False, "Password must be at least 8 characters long"

    # All checks passed
    return True, "Password is valid"


def check_address(address_text):
    """
    Validates that an address starts with numbers followed by location information.

    Valid address formats:
    - "123 Main Street"
    - "4567 Oak Avenue, City"
    - "789-B Central Road, City, State"

    Args:
        address_text (str): The address to validate

    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    # Check if address is empty
    if not address_text.strip():
        return False, "Address cannot be empty"

    # Split address into parts
    parts = address_text.strip().split(' ')

    # Need at least 2 parts (number and street)
    if len(parts) < 2:
        return False, "Address must contain house number and street name"

    # First part should start with a number
    first_part = parts[0]
    if not any(char.isdigit() for char in first_part):
        return False, "Address must start with a house number"

    # Check if there's text after the number
    remaining_text = ' '.join(parts[1:])
    if not remaining_text.strip():
        return False, "Address must contain location information after the number"

    # Check for minimum length of location part (arbitrary minimum of 5 characters)
    if len(remaining_text) < 5:
        return False, "Location information is too short"

    # All checks passed
    return True, "Address is valid"


def check_phone(phone_text):
    """
    Validates phone number format.

    Valid formats:
    - 11 digits (local number): e.g., "01234567890"
    - 13 characters (with country code): Must start with "+", e.g., "+201234567890"

    Args:
        phone_text (str): The phone number to validate

    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    # Remove any spaces
    phone_text = phone_text.strip()

    # Check if phone is empty
    if not phone_text:
        return False, "Phone number cannot be empty"

    # Check length
    length = len(phone_text)

    if length == 11:
        # Check if all characters are digits for 11-digit format
        if not phone_text.isdigit():
            return False, "Local number must contain only digits"
        return True, "Phone number is valid"

    elif length == 13:
        # Check if starts with '+'
        if not phone_text.startswith('+'):
            return False, "International number must start with '+'"

        # Check if remaining characters are digits
        remaining_digits = phone_text[1:]
        if not remaining_digits.isdigit():
            return False, "Phone number must contain only digits after '+'"

        return True, "Phone number is valid"

    else:
        return False, "Phone number must be either 11 digits (local) or 13 characters (international with '+')"