#! venv/bin/python

complete_address = ["234.67.0.5", "20"] #[i for i in input().split("/")]
network_parts = [int(i) for i in complete_address[0].split(".")]
machine_part = complete_address[1]


def get_mask(netmask):
    bits = []
    mask = ""
    for i in range(1, 33):
        if i <= netmask:
            bits.append("1")
        else:
            bits.append("0")
        if i % 8 == 0 and i <= netmask:
            bits.append(".")
    for i in bits:
        mask += i
    return mask


def get_binary(octets):
    bin_ip = ""
    bin_bdcast = ""
    for i, v in enumerate(octets):
        bin_ip += bin(v)[2:].zfill(8)
        bin_ip += "." if i < len(octets) - 1 else ""
        if i == 2:
            bin_bdcast = bin_ip + "1" * 8
            bin_ip += "0" * 8
            break
    return bin_ip, bin_bdcast


def get_human_address(bin):
    hb = ""
    for i, v in enumerate(bin):
        hb += str(int(v, 2))
        hb += "." if i < len(bin) - 1 else ""
    return hb


if __name__ == "__main__":
    mask = get_mask(int(machine_part))
    binary_ip, binary_bdcast = get_binary(network_parts)

    if int(machine_part) <= 24:
        human_network_address = get_human_address([i for i in binary_ip.split(".")])
        human_bdcast_address = get_human_address([i for i in binary_bdcast.split(".")])
        print(human_network_address)
        print(human_bdcast_address)
    else:
        print("\n".join(complete_address[0]))
