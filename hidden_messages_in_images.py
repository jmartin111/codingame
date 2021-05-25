#! venv/bin/python3
width, height = [int(i) for i in input().split()]
bytestring = []
bits = ""
# scan through the lines
for i in range(height):
    
    # get all the input in each line
    for j in input().split():
        # grab the LSB of each input to create a byte
        bits += bin(int(j))[-1]
    # add the byte to our message
    bytestring.append(bits)
converted = int(bits, 2)
decoded = converted.to_bytes((converted.bit_length() + 7) // 8, 'big').decode()
print(decoded)



