# Problem Statement
# Write a function that takes two string parameters, an IP (v4) address and a subnet mask, and returns two strings: the network block, and the host identifier.

# The function does not need to support CIDR notation.

# Description
# A single IP address with subnet mask actually specifies several addresses: a network block, and a host identifier, and a broadcast address. These addresses can be calculated using a bitwise AND operation on each bit.

# (The broadcast address is not used in this kata.)

# Example
# A computer on a simple home network might have the following IP and subnet mask:

# IP: 192.168.2.1
# Subnet: 255.255.255.0
# (CIDR Notation: 192.168.2.1 /24)
# In this example, the network block is: 192.168.2.0. And the host identifier is: 0.0.0.1.

# bitwise AND
# To calculate the network block and host identifier the bits in each octet are ANDed together. When the result of the AND operation is '1', the bit specifies a network address (instead of a host address).

# To compare the first octet in our example above, convert both the numbers to binary and perform an AND operation on each bit:

# 11000000 (192 in binary)
# 11111111 (255 in binary)
# --------------------------- (AND each bit)
# 11000000 (192 in binary)
# So in the first octet, '192' is part of the network address. The host identifier is simply '0'.

# For more information see the Subnetwork article on Wikipedia.

# Solution
# Write a function that takes two string parameters, an IP (v4) address and
# a subnet mask, and returns two strings: the network block,
# and the host identifier.

# For example:
# >>> print ipv4__parser('192.168.50.1', '255.255.255.0')
# ('192.168.50.0', '0.0.0.1')
BINARY_VALUES = [128,64,32,16,8,4,2,1]

def convertToBinary(value=[]):
    result=[]
    for num in value:
        bin = [0,0,0,0,0,0,0,0]
        number = int(num)
        i=0
        complete=False
        while i<=7 or complete==False:
            if BINARY_VALUES[i]>number:
                bin[i]=0
            else:
                number=number-BINARY_VALUES[i]
                bin[i]=1
                
            if number==0:
                result.append(bin)
                complete=True
                break
            i=i+1
    
    return result
        
def andOperation(bin1,bin2):
    result=[]
    for i in range(len(bin1)):
        octet1=bin1[i]
        octet2=bin2[i]
        m=len(octet1)
        bin=[0,0,0,0,0,0,0,0]
        for j in range(m):
            if octet1[j]==1 and octet2[j]==1:
                bin[j]=1

        result.append(bin)
    return result

def orOperation(bin1,bin2):
    result=[]
    
    for i in range(len(bin1)):
        bin=[]
        for j in range(8):
            if bin1[i][j]-bin2[i][j]==1:
                bin.append(1)
            else:
                bin.append(0)
            
        result.append(bin)
    
    return result

def convertToValue(binary_list):
    value = []
    for binary in binary_list:
        sum = 0
        for i in range(8):
            if binary[i] == 1:
                sum = sum + BINARY_VALUES[i]
        value.append(str(sum))
    return value
                
        
def ipv4__parser(ip_addr, mask):
    ip_addr_list = ip_addr.split('.')
    mask_list = mask.split('.')
    
    ip_addr_list_binary=convertToBinary(ip_addr_list)
  
    mask_list_binary=convertToBinary(mask_list)
    
    network_prefix_list_binary=andOperation(ip_addr_list_binary, mask_list_binary)
    
    host_identifier_list_binary=orOperation(ip_addr_list_binary, mask_list_binary)

    network_prefix_list=convertToValue(network_prefix_list_binary)

    host_identifier_list=convertToValue(host_identifier_list_binary)
    
    return ".".join(network_prefix_list), ".".join(host_identifier_list)
