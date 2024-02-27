def check_string(string):
    if 'a' in string or 'o' in string:
        if 'i' not in string and 'e' not in string:
            return True
    return False
string = input()
if check_string(string.lower()):
    print("True")
else:
    print("False")