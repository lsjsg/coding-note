def check_password(password):
    def check_digit(string):
        num = 0
        for i in list(string):
            if i.isdigit():
                num += 1
        return num > 1
    if len(password)<8:
        return False
    elif not password.isalnum():
        return False
    else:
        return check_digit(password)