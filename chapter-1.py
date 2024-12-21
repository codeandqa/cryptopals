def hex_to_binary(hex_string):
    """
    Converts a hexadecimal string to a binary string.
    """
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    try:
        return ''.join(hex_to_bin_map[char.upper()] for char in hex_string)
    except KeyError:
        raise ValueError("Invalid character in hexadecimal string")

def bin_to_decimal(binary_string):
    """
    Converts a binary string to a list of decimal values, using 6-bit chunks.
    """
    # Pad the binary string to ensure its length is a multiple of 6
    remainder = len(binary_string) % 6
    if remainder:
        binary_string += '0' * (6 - remainder)

    # Split the binary string into 6-bit chunks
    chunks = [binary_string[i:i + 6] for i in range(0, len(binary_string), 6)]

    # Convert each chunk to a decimal number
    return [int(chunk, 2) for chunk in chunks]

def decimal_to_base64(decimal_list):
    """
    Converts a list of decimal values to a Base64-encoded string.
    """
    base64_chars = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789+/"
    )

    # Convert decimal values to Base64 characters
    base64_string = ''.join(base64_chars[num] for num in decimal_list)

    # Pad the Base64 string to make its length a multiple of 4
    padding_length = (4 - len(base64_string) % 4) % 4
    base64_string += '=' * padding_length

    return base64_string

if __name__ == "__main__":
    try:
        hex_string = "4BC1"
        binary_string = hex_to_binary(hex_string)
        decimal_list = bin_to_decimal(binary_string)
        base64_string = decimal_to_base64(decimal_list)
        print(f"Base64 representation of {hex_string}: {base64_string}")
    except ValueError as e:
        print(e)
