import ast
def change_to_smaller_strings(text):
    word = ""
    num=0
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
        if not (a.isalnum() or (a in "=[]()")):
            small.remove(a)
            # print("remove",a)
    return small


p="""
sum=0
for i in range(10):
    sum+=i
print(sum)
"""
text = ast.dump(ast.parse(p))
print(text)
a=change_to_smaller_strings(text)
# for i in a:
#     print(i,"1",i.isalnum(),"2",a=="=","3",a=="[","4",a=="(","5",a==")","6",a=="]")
print(a)