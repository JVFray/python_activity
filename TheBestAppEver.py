a = int(input("What is the temperature outside?"))

def warm():
    print("warm")

def hot():
    print("hot")

def chilly():
    print("chilly")

if a > 60 and a < 90 :
    warm()
elif a >= 90:
    hot()
else:
    chilly()