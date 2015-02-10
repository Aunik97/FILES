import pickle
class Person():
    def __init__(self):
        self.name = None
        self.dob = None


with open("devex1.dat",mode="rb") as binary_file:
    pickle.load(people,binary_file)
