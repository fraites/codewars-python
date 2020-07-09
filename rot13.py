# rot13 algorithm that translates each letter to a corresponding 'code' letter 13 characters over
# ex. 'test' ==> 'grfg'

from string import ascii_lowercase, ascii_uppercase

def rot13(message):
    lower = str.maketrans(ascii_lowercase, ascii_lowercase[13:] + ascii_lowercase[:13])
    upper = str.maketrans(ascii_uppercase, ascii_uppercase[13:] + ascii_uppercase[:13])
    return message.translate(lower).translate(upper)
