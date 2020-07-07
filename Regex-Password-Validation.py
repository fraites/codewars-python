# Kata instructions
# Password must be at least 6 characters
# Password must contain upper case letter
# Password must contain lower case letter
# Password must contain a number
# Password must be alphanumeric
import re
# the password will be automatically asserted by test cases. Below is only an example
password = "4fdg5Fj3"
# you only need to fill in the search condition you're looking for to complete this kata
regex = re.compile("^(?=.*[a-z])(?=.*[a-z])(?=.*[\d])[a-zA-Z\d]{6,}$")
if regex.search(password):
    print(True)
else:
    print(False)

