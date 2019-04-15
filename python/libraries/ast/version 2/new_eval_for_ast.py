import ast


class Eval():
    def __init__(self, text):
        self.text = ast.dump(ast.parse(text))
        self.list = []
        self.left_list = 0
        self.right_list = 0
        self.left_tuple = 0
        self.right_tuple = 0
        self.last = True
        self.glevel = 0
        self.levels = []

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

    def form_new_list(self):
        sentence = self.change_to_smaller_strings()
        # the first element is the name of the list
        # the second element stands for whether it is a list or a tuple
        # the third digit is the level of the tuple or the list
        # the forth digit marks the glevel
        self.levels.append([{"root": []}, True, 0, 0])

        def listleft(i):
            # by using the name if the string before the list to create a new list
            name = sentence[i]
            self.last = True
            # the level of the list plus one
            self.left_list += 1
            # the genenral level plus one
            self.glevel += 1
            # self.levels will append the information of the lists and tuples
            self.levels.append([{name: sentence[i]}, self.last, self.left_list, self.glevel])

        def tupleleft(i):
            name = sentence[i]
            self.last = False
            self.left_tuple += 1
            self.glevel += 1
            self.levels.append([{name: sentence[i]}, self.last, self.left_tuple, self.glevel])

        for i in range(len(sentence)):

            if (sentence[i].isalpha() and sentence[i + 1] == "["):
                listleft(i)

            elif (sentence[i].isalnum() and sentence[i + 1] == "("):
                tupleleft(i)

            elif sentence[i] == "]":
                self.glevel -= 1
                self.right_list += 1

            elif sentence[i] == ")":
                self.glevel -= 1
                self.right_tuple += 1

            elif (sentence[i].isalnum() and sentence[i + 1] == "=" and sentence[i + 2].isalnum()):
                d={sentence[i]:sentence[i + 2]}
                self.levels[self.glevel].append(d)

            elif (sentence[i].isalnum() and sentence[i + 1] == "=" and sentence[i + 2] == "["):
                listleft(i)

            elif (sentence[i].isalnum() and sentence[i + 1] == "=" and sentence[i + 2] == "("):
                tupleleft(i)
