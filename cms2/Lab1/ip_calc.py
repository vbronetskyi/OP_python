"""Lab_1.1: Work with network adres"""

def get_ip_from_raw_address(raw_address: str) -> str:
    """
    gives raw adres type "00.000.000.000/00"
    return IP address type "00.000.000.000"
    >>> get_ip_from_raw_address("56.032.230.126/22")
    '56.032.230.126'
    >>> get_ip_from_raw_address("17.105.232.201/30")
    '17.105.232.201'
    """
    if check_address_validity(raw_address):
        return raw_address[:raw_address.index('/')]
    return None

def mask_int(raw_address: str) -> int:
    """
    return mask
    """
    count, mask, index_elem, astr= 0, "", [], []
    for indx, element in enumerate(raw_address):
        if element == ".":
            count+=1
        elif count == 4:
            index_elem = indx
            count+=1
        if indx == len(raw_address) - 1:
            if count == 3:
                astr = [raw_address[a:] for a in range(len(raw_address)) if raw_address[a] == "/"]
                mask+=str(astr[0]).replace("/", "")
            elif count == 5:
                mask+=str(raw_address[index_elem:]).replace(".", "")
    return int(mask)

def check_address_validity(raw_address: str) -> bool:
    """
    check address ability
    return True or False
    >>> check_address_validity("hah")
    False
    >>> check_address_validity("try.this.wor.dst/do")
    False
    >>> check_address_validity("534.323.12.22/30")
    False
    >>> check_address_validity("134.203.04.23/23")
    True
    """
    try:
        maska = mask_int(raw_address)
        raw_address = raw_address.replace("/", ".").split(".")[:-1]
        if int(maska) > 32:
            return False
        if int(raw_address[0]) > 255 or int(raw_address[1]) > 255 \
             or int(raw_address[2]) > 255 or int(raw_address[3]) > 255:
            return False
        return True
    except (ValueError, TypeError, IndexError, UnboundLocalError):
        return False

def get_network_address_from_raw_address(raw_address: str) -> str:
    """
    receive raw_address. If address is ability does bitwise "and"
    return network address
    >>> get_network_address_from_raw_address('41.121.142.124/30')
    '41.121.142.124'
    """
    if not check_address_validity(raw_address):
        return None
    raw_address_bin = bin_address(raw_address.replace("/", ".").split(".")[:-1])
    mask_address_bin = get_binary_mask_from_raw_address(raw_address)
    solut = str()
    for indx, elem in enumerate(raw_address_bin):
        if elem == "1" and mask_address_bin[indx] == "1":
            solut += "1"
        elif elem == "." and indx != len(raw_address_bin):
            solut += "."
        elif indx != len(raw_address_bin):
            solut += "0"
    solut = solut.split(".")
    solut_bin_form = ""
    for binary_num in solut:
        solut_bin_form += str(int(binary_num, 2))
        solut_bin_form += "."
    return solut_bin_form[:-1]


def bin_address(raw_address: list) -> str:
    """
    receive list with number.
    return bit.

    >>> bin_address(['32', '236', '164', '123'])
    '00100000.11101100.10100100.01111011'
    >>> bin_address(['12', '124', '223', '10'])
    '00001100.01111100.11011111.00001010'
    """
    raw_address_bin = str()
    for indx, elem in enumerate(raw_address):
        raw_address_bin += ((bin(int(elem)))[2:]).zfill(8)
        if len(raw_address) > indx:
            raw_address_bin += "."
    return raw_address_bin[:-1]

def get_binary_mask_from_raw_address(raw_address: str) -> str:
    """
    recieve raw address
    return binaru mask.
    >>> get_binary_mask_from_raw_address('56.032.230.126/22')
    '11111111.11111111.11111100.00000000'
    >>> get_binary_mask_from_raw_address('123.032.230.126.23')
    '11111111.11111111.11111110.00000000'
    >>> get_binary_mask_from_raw_address('113.042.210.226.9')
    '11111111.10000000.00000000.00000000'
    >>> get_binary_mask_from_raw_address('113.042.210.226.90')

    """
    if check_address_validity(raw_address) == False:
        return None
    mask = mask_int(raw_address)
    bit_mask = ["","","",""]
    for indx, _ in enumerate(bit_mask):
        if mask >= 8:
            for i in range(8):
                bit_mask[indx] += "1"
            mask-=8
        else:
            for i in range(8):
                if i + 1 > mask:
                    bit_mask[indx]+= "0"
                    mask-= i + 1
                else:
                    bit_mask[indx]+= "1"
    bit_mask_solve = ""
    for indx, elem in enumerate(bit_mask):
        bit_mask_solve += elem
        if indx != (len(bit_mask) - 1):
            bit_mask_solve += "."
    return bit_mask_solve

def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    """
    recieves raw address
    return broadcast address.
    >>> get_broadcast_address_from_raw_address('17.105.232.201/30')
    '17.105.232.203'
    """
    if not check_address_validity(raw_address):
        return None
    ip_adrs = get_ip_from_raw_address(raw_address).split('.')
    mask_adrs_bin = get_binary_mask_from_raw_address(raw_address).split('.')
    mask_ad, broadcast_ad = '', ''
    for binary_num in mask_adrs_bin:
        mask_ad += str(int(binary_num, 2))+'.'
    mask_invert = [255 - int(k) for k in mask_ad[:-1].split(".")]
    for indx, elem in enumerate(mask_invert):
        broadcast_ad += str(int(elem) | int(ip_adrs[indx]))+'.'
    return broadcast_ad[:-1]

def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    usable IP address
    >>> get_first_usable_ip_address_from_raw_address("17.105.232.234/18")
    '17.105.192.1'
    >>> get_first_usable_ip_address_from_raw_address("17.105.162.161/27")
    '17.105.162.161'
    >>> get_first_usable_ip_address_from_raw_address("17.105.162.161/86")

    """
    if not check_address_validity(raw_address):
        return None
    raw_address_crt = get_network_address_from_raw_address(raw_address).split(".")
    raw_address_crt[3] = str(int(raw_address_crt[3]) + 1)
    solut = '.'.join(raw_address_crt)
    return solut

def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    penultomate usable ip adress
    >>> get_penultimate_usable_ip_address_from_raw_address("17.105.162.161/24")
    '17.105.162.253'
    >>> get_penultimate_usable_ip_address_from_raw_address("17.105.162.161/31")
    '17.105.162.159'
    """
    if not check_address_validity(raw_address):
        return None
    raw_address_crt = get_broadcast_address_from_raw_address(raw_address).split(".")
    raw_address_crt[3] = str(int(raw_address_crt[3]) - 2)
    solut = '.'.join(raw_address_crt)
    return solut

def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    """
    return number of hosts
    >>> get_number_of_usable_hosts_from_raw_address("17.105.162.161/24")
    254
    >>> get_number_of_usable_hosts_from_raw_address("17.105.162.161/05")
    134217726
    >>> get_number_of_usable_hosts_from_raw_address("367.105.1362.161/2400")
    """
    if not check_address_validity(raw_address):
        return None
    return 2**(32 - mask_int(raw_address)) - 2
def get_ip_class_from_raw_address(raw_address: str) -> str:
    """
    return class address
    >>> get_ip_class_from_raw_address("17.105.162.161/05")
    'A'
    >>> get_ip_class_from_raw_address("987.105.162.161/05")

    >>> get_ip_class_from_raw_address("234.105.162.161/05")
    'D'
    """
    if not check_address_validity(raw_address):
        return None
    first_elem = int(get_broadcast_address_from_raw_address(raw_address).split(".")[0])
    if first_elem >= 1 and first_elem < 127: return "A"
    elif first_elem>=128 and first_elem<=191: return "B"
    elif first_elem>=192 and first_elem<=223: return "C"
    elif first_elem>=224 and first_elem<=239: return "D"
    elif first_elem>=240 and first_elem< 247: return "E"

def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    """
    get rew adress
    return True if address is privat
    in another case return False

    >>> check_private_ip_address_from_raw_address("192.087.121.223/30")
    True
    >>> check_private_ip_address_from_raw_address("17.105.162.161/05")
    False
    >>> check_private_ip_address_from_raw_address("234.1035.162.161/50")
    """
    if not check_address_validity(raw_address):
        return None
    if int(get_broadcast_address_from_raw_address(raw_address).split(".")[0]) in (10, 172, 192):
        return True
    return False

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
