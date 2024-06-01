from main import *
vectors=[]
numberOfVectors=input("Number of vectors to add: ")
for i in range(int(numberOfVectors)):
    vectors.append(tuple(float(x) for x in input("Enter vector separted by spaces: ").split()))
    print(vectors)
print(tuple(round(x,10) for x in addVectors(*vectors)))