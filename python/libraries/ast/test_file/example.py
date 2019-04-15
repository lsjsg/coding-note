import ast
p3="""
def decision(num):
    if num==1:
        return True
    else:
        return False
"""
text=ast.dump(ast.parse(p3))
def change(text):
    word = ""
    small = []
    for i in text:
        if i.isalpha() or i == "_":
            word += i  # form complete word
        elif i.isdigit():
            small.append(i)
        else:
            if len(word) > 0:
                small.append(word)
                word = ""
            small.append(i)  # append []()
    for a in small:
        if a in "' ,":  # remove , '
            print(a)
            small.remove(a)
    return small
print(change(text))
