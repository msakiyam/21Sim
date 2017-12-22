import hashlib

for i in list(range(0,2**32)):
    str_i = str(i)
    print(str_i)
    string =  str_i + "Make America Great Again"
    #print(string)
    b = string.encode('utf-8')
    objHash = hashlib.sha256(b)
    hex = objHash.hexdigest()
    string_hex = str(hex)
    if string_hex[:12] == '000000000000':
        print(string)
        print(string_hex)

