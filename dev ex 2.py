import pickle

class Person():
    def __init__(self):
        self.name = None
        self.dob = None

people = []
self = Person()
for count in range(2):
    self.name = input("enter name")
    self.dob = input("enter date of birth (YYYY-MM-DD): ")
    people.append(Person())

with open("devex1.dat",mode="wb") as binary_file:
    pickle.dump(people,binary_file)

with open("devex1.dat",mode="rb") as binary_file:
    people = pickle.load(binary_file)
    for line in people:
        print(self.name,self.dob)
