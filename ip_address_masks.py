#! venv/bin/python
complete_address = [i for i in "234.67.0.5/20".split("/")]
network_parts = [int(i) for i in complete_address[0].split(".")]
machine_part = complete_address[1]


def get_mask_bits(netmask):
    return f'{"1" * netmask}{"0" * (32 - netmask)}'


def get_binary_ip(octets, mask_bits):
    binary = ""
    for o in octets:
        binary += format(o, "08b")
    binary = bin(int(binary, 2) & int(mask_bits, 2))
    return binary[2:].zfill(32)


def get_human_address(binary):
    ip = ""
    for i in range(0, len(binary) - 7, 8):
        p = int(binary[i:i+8], 2)
        ip += f"{p}." 
    return ip.rstrip(".")


def get_human_bdcast(binary, mask):
    bdcast = ""
    if mask == "0" * 32:
        return "255.255.255.255"

    for i in range(0, len(binary) - 14, 8):
        p = int(binary[i:i + 8], 2) & int(mask[i:i + 8], 2)
        bdcast += f"{p}."
    return f"{bdcast}255"


if __name__ == "__main__":
    mask = get_mask_bits(int(machine_part))
    binary_ip = get_binary_ip(network_parts, mask)
    human_ip = get_human_address(binary_ip)

    print(human_ip)
    if int(machine_part) <= 24:
        print(get_human_bdcast(binary_ip, mask))
    else:
        print(f"{human_ip}")
