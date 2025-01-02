"""
Author: Sean Coggeshall
About: 
This program takes an IP Address and Subnet Mask and converts each to its binary
representation, gets the network address, the broadcast address, and the wildcard mask.

"""

def decimal_to_binary(octet):
    """Convert a decimal octet to an 8-bit binary string."""
    binary_representation = ""
    powers_of_two = [128, 64, 32, 16, 8, 4, 2, 1]
    
    for power in powers_of_two:
        if octet >= power:
            binary_representation += '1'
            octet -= power
        else:
            binary_representation += '0'
    
    return binary_representation

def ip_to_binary(ip_address):
    """Convert an IP address to its binary representation."""
    octets = ip_address.split(".")
    binary_ip = []
    
    for octet in octets:
        binary_ip.append(decimal_to_binary(int(octet)))

    return ".".join(binary_ip)

def subnet_to_binary(subnet_mask):
    """Convert a subnet mask to its binary representation."""
    octets = subnet_mask.split(".")
    binary_subnet = []
    
    for octet in octets:
        binary_subnet.append(decimal_to_binary(int(octet)))

    return ".".join(binary_subnet)

def calculate_network_and_broadcast(ip_address, subnet_mask):
    """Calculate the network and broadcast addresses from IP and subnet mask."""
    ip_octets = list(map(int, ip_address.split(".")))
    subnet_octets = list(map(int, subnet_mask.split(".")))
    
    # Calculate network address using bitwise AND
    network_address = [ip & subnet for ip, subnet in zip(ip_octets, subnet_octets)]
    
    # Calculate broadcast address using bitwise OR with inverted subnet mask
    inverted_subnet = [255 - subnet for subnet in subnet_octets]
    broadcast_address = [ip | inverted for ip, inverted in zip(ip_octets, inverted_subnet)]
    
    # Join the octets to form the final addresses
    network_address_str = ".".join(map(str, network_address))
    broadcast_address_str = ".".join(map(str, broadcast_address))
    
    return network_address_str, broadcast_address_str

def calculate_wildcard_mask(subnet_mask):
    """Calculate the wildcard mask from the subnet mask."""
    subnet_octets = list(map(int, subnet_mask.split(".")))
    wildcard_mask = [255 - subnet for subnet in subnet_octets]
    return ".".join(map(str, wildcard_mask))

def is_valid_ip(ip):
    """Check if the IP address is valid."""
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not (0 <= int(octet) <= 255):
            return False
    return True

def is_valid_subnet(subnet):
    """Check if the subnet mask is valid."""
    octets = subnet.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not (0 <= int(octet) <= 255):
            return False
    return True

# User Input for IP address and Subnet mask
while True:
    ip_address = input("Enter your IP Address: ")
    if is_valid_ip(ip_address):
        break
    else:
        print("Invalid IP address. Please enter a valid IP address.")

while True:
    subnet_mask = input("Enter your Subnet Mask: ")
    if is_valid_subnet(subnet_mask):
        break
    else:
        print("Invalid subnet mask. Please enter a valid subnet mask.")

# Convert IP address and Subnet mask to binary
binary_ip = ip_to_binary(ip_address)
binary_subnet = subnet_to_binary(subnet_mask)

# Calculate Network and Broadcast Addresses
network_address, broadcast_address = calculate_network_and_broadcast(ip_address, subnet_mask)

# Calculate Wildcard Mask
wildcard_mask = calculate_wildcard_mask(subnet_mask)

# Display results
print(f"\nBinary representation of IP Address {ip_address}: {binary_ip}")
print(f"Binary representation of Subnet Mask {subnet_mask}: {binary_subnet}")
print(f"Network Address: {network_address}")
print(f"Broadcast Address: {broadcast_address}")
print(f"Wildcard Mask: {wildcard_mask}")

# Display Network and Broadcast in Binary
print(f"Binary Network Address: {ip_to_binary(network_address)}")
print(f"Binary Broadcast Address: {ip_to_binary(broadcast_address)}")
print(f"Binary Wildcard Mask: {subnet_to_binary(wildcard_mask)}")





        






    