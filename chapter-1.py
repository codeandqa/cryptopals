def hex_to_binary(hex_string):
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    binary_string=""
    for s in hex_string:
        binary_string +=hex_to_bin_map[s.upper()]
    return binary_string

def bin_to_decimal(binary_string):
    leng = len(binary_string)
    remainder = leng%6
    leading_zeros = ''
    if(remainder > 0):
        leading_zeros = '0'*(6-remainder)
    binary_string = binary_string +leading_zeros
    chunk_size = 6
    chunks = chunk_string(binary_string, chunk_size)
    decimals = []
    for chunk in chunks:
        num = 0
        for i, value in enumerate(chunk[::-1]):
            num += int(value) * (2 ** i)
        decimals.append(num)
    return decimals


def decimal_to_base64(decimal_list):

    dec_to_base64 = {
        '0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H',
        '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', 
        '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', 
        '24': 'Y', '25': 'Z', '26': 'a', '27': 'b', '28': 'c', '29': 'd', '30': 'e', '31': 'f', 
        '32': 'g', '33': 'h', '34': 'i', '35': 'j', '36': 'k', '37': 'l', '38': 'm', '39': 'n', 
        '40': 'o', '41': 'p', '42': 'q', '43': 'r', '44': 's', '45': 't', '46': 'u', '47': 'v', 
        '48': 'w', '49': 'x', '50': 'y', '51': 'z', '52': '0', '53': '1', '54': '2', '55': '3', 
        '56': '4', '57': '5', '58': '6', '59': '7', '60': '8', '61': '9', '62': '+', '63': '/'
    }
    eqls = ''
    base64=''
    for item in decimal_list:
        base64 +=dec_to_base64[str(item)]
    rem = len(base64)%4
    if(rem>0):
        eqls = '='*(4-rem)
    base64 +=eqls
    print(base64)

def chunk_string(string, chunk_size):
    return [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]

if __name__ == "__main__":
    binary = hex_to_binary("4BC1")
    decimal_list = bin_to_decimal(binary)
    decimal_to_base64(decimal_list)
