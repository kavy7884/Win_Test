# Encoding
string = "abc"
print(len(string))

string_bytes = string.encode('utf-8')
print(len(string_bytes))
print(string_bytes)

name = "周情凱"
print(len(name))

name_bytes = name.encode('utf-8')
print(len(name_bytes))
print(name_bytes)

# Decoding
string_ucode = string_bytes.decode('utf-8')
print(string_ucode)

name_ucode = name_bytes.decode('utf-8')
print(name_ucode)


