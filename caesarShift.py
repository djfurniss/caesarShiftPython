# Recreating the Caesar Shift encryption code that I did in JS during my bootcamp

# -25 < shift < 25

def caesar_shift(str, shift, encode=True):
    # BASE CASE FOR RETURNING EARLY
    if shift > 25:
        return 'Shift cannot be greater than 25'
    elif shift < -25:
        return'Shift cannot be less than 25'
    elif not str:
        return'No string to decipher'
    
    # return value to be built on
    result = ""
    
    # determines which way the shift should go if encoding or decoding
    if not encode:
        shift = shift * - 1
    
    # iterate through the str
    for char in str:
        # get the char code for each char
        char_code = ord(char)
        
        # if char is a space or any other character besides a-z, leave as is
        if char == " " or char_code < 97 or char_code > 122:
            result += char
        else:     
            new_char_code = char_code + shift
            # check to see (per each char) if adding the shift will get a char that's outside of the alphabet range
            if new_char_code > 122: # past z
                # if so, subtract 26 to get back around and THEN add the shift
                new_char_code = (char_code - 26) + shift
            elif new_char_code < 97:
                # if it hits a char before a, ADD 26 then keep shifting to get to the other side of the alphabet
                new_char_code = (char_code + 26) + shift

            result += chr(new_char_code)
        
    return result
   
print(caesar_shift("shifting is fun", 3))
print(caesar_shift("vkliwlqj lv ixq", 3, False))
