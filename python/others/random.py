import random

rich=[]
poor=[]
data=open("C:/Users/lsjsg/Desktop/math.cvs","w+")
def place_generator0():
    place_x=random.randint(0,400)
    place_y = random.randint(0, 100)
    for i in range(5):
        piont=[]
        piont_x=random.randint(-10,10)
        piont.append(piont_x+place_x)
        piont_y=random.randint(-10,10)
        piont.append(piont_y+place_y)
        rich.append(piont)

def place_generator1():
    place_x=random.randint(0,400)
    place_y=random.randint(0,100)
    for i in range(5):
        piont=[]
        piont_x=random.randint(-10,10)
        piont.append(piont_x+place_x)
        piont_y=random.randint(-10,10)
        piont.append(piont_y+place_y)
        poor.append(piont)

for i in range(15):
    place_generator0()
    place_generator1()


for r in rich:
    string1=str(r[0])+","+str(r[1])+","
    data.write(string1)
    data.write("\n")

for p in poor:
    string2 = str(p[0]) + "," + str(p[1]) + ","
    data.write(string2)
    data.write("\n")
data.close()