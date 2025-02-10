def check_password(password_text):

    # Check minimum length
    if len(password_text) < 8:
        return False, "Password must be at least 8 characters long"

    return True, "Password is valid"


def check_address(address_text):
    """
    Validates that an address starts with numbers followed by location information.
    """
    if not address_text.strip():
        return False, "Address cannot be empty"

    parts = address_text.strip().split(' ')

    if len(parts) < 2:
        return False, "Address must contain house number and street name"

    first_part = parts[0]
    if not any(char.isdigit() for char in first_part):
        return False, "Address must start with a house number"

    remaining_text = ' '.join(parts[1:])
    if not remaining_text.strip():
        return False, "Address must contain location information after the number"

    # Check for minimum length of location part (arbitrary minimum of 5 characters)
    if len(remaining_text) < 5:
        return False, "Location information is too short"

    return True, "Address is valid"


def check_phone(phone_text):
    """
    Validates phone number format.
    """
    phone_text = phone_text.strip()

    if not phone_text:
        return False, "Phone number cannot be empty"

    length = len(phone_text)

    if length == 11:
        if not phone_text.isdigit():
            return False, "Local number must contain only digits"
        return True, "Phone number is valid"

    elif length == 13:
        if not phone_text.startswith('+'):
            return False, "International number must start with '+'"

        # Check if remaining characters are digits
        remaining_digits = phone_text[1:]
        if not remaining_digits.isdigit():
            return False, "Phone number must contain only digits after '+'"

        return True, "Phone number is valid"

    else:
        return False, "Phone number must be either 11 digits (local) or 13 characters (international with '+')"