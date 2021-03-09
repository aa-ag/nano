def hash_function(string):
    hash_code = 0
    for character in string:
        hash_code += ord(character)
    return hash_code


hash_code_1 = hash_function("abcd")
print(hash_code_1)
# 394
