import ast

class Eval():
    def __init__(self, text):
        self.text = ast.dump(ast.parse(text))
        self.list = []
        self.left = 0
        self.right = 0
        self.level = 0
        self.dict = {"root":[],"assign":[]}
        self.last=["root"]
        self.past=''

    def change_to_smaller_strings(self):
        word = ""
        small = []
        for i in self.text:
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
                small.remove(a)
        return small

    def tree_dict(self):
        sentence = self.change_to_smaller_strings()
        for i in range(len(sentence)):
            if (sentence[i].isalpha() and sentence[i+1] in "[("):
                self.dict[sentence[i]]=[]
                self.last.append(sentence[i])
                self.dict[self.last[self.level]].append(sentence[i])
                self.level += 1
                self.past = sentence[i]

            elif (sentence[i].isalpha() and sentence[i+1]=="=" and sentence[i+2] in "[(" and not sentence[i-1].isalpha()):
                self.dict[sentence[i]] = []
                self.last.append(sentence[i])
                self.dict[self.last[self.level]].append(sentence[i])
                self.level += 1
                self.past = sentence[i]

            elif (sentence[i].isalpha() and sentence[i+1]=="=" and sentence[i+2].isalnum() and sentence[i+3] in "[("):
                l=[]
                l.append(sentence[i])
                l.append(sentence[i+2])
                self.dict["assign"].append(tuple(l))
                self.dict[sentence[i]] = []
                self.last.append(sentence[i])
                self.dict[self.last[self.level]].append(sentence[i])
                self.level += 1
                self.past = sentence[i]


            elif (sentence[i] in "])"):
                self.level-=1
                self.last.pop()
                self.past = self.last[-1]
                self.dict["assign"].append(tuple(l))

            elif (sentence[i].isalpha() and sentence[i+1]=="=" and sentence[i+2].isalnum()):
                l=[]
                l.append(sentence[i])
                l.append(sentence[i+2])
                self.dict[self.last[self.level]].append(tuple(l))
                self.dict["assign"].append(tuple(l))

            elif (sentence[i].isalpha() and sentence[i+1]=="(" and sentence[i+2]==")"):
                l = ["Function"]
                l.append(sentence[i])
                self.dict[self.last[self.level]].append(tuple(l))
                self.level+=1
                self.last.append(sentence[i])

        return self.dict


