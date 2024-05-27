from main import *
vectors=[]
numberOfVectors=input("Number of vectors to add: ")
for i in range(int(numberOfVectors)):
    vectors.append(tuple(input("Enter vector separted by spaces: ").split()))
    print(vectors)
print(addVectors(*vectors))