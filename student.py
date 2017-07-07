__author__ = 'shreyas'

class student(object):
    def __init__(self, name, GPA, age):
        self.name = name
        self.GPA = GPA
        self.age = age
        if(not str(self.name).isalpha()): raise ValueError("Name can only contain alpha chars. Cannot be empty")
        if(self.GPA > 4.0 or self.GPA < 0): raise ValueError("GPA must be within 0 to 4.0")
        if(self.age < 0): raise ValueError("Age must be greater than 0")

    def __repr__(self):
        return self.name

    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'GPA: ' + str(self.GPA) + '\n' + 'Age: ' + str(self.age) + '\n'

    def __lt__(self, other):
        if isinstance(other,student):

            #cmp name, break on age then GPA
            if(str(self.name).lower() < str(other.name).lower()):return True
            elif(str(self.name).lower() > str(other.name).lower()):return False
            else:
                if(self.age < other.age): return True
                elif(self.age > other.age): return False
                else:
                    if(self.GPA < other.GPA): return True
                    else: return False

        else: return NotImplemented

    def __eq__(self, other):
        if isinstance(other,student):
            if ((self.GPA == other.GPA) and (self.name == other.name) and (self.age == other.age)):
                return True
            else: return False
        return NotImplemented

    def __hash__(self):
        return hash(self.name + str(self.GPA) + str(self.age))


#Beging Testing:

shreyas =  student('shreyas',4,24)
nica = student('nica', 4.0, 25)
cartman = student('cartman', 0.0, 16)
timmy = student('timmy', 1.2, 16)
harsha = student('harsha', 3.3, 21)
students = dict([(shreyas, 1), (nica, 1), (timmy, 1), (harsha, 1), (cartman, 1)])
not_there = student('none', 0, 0)

#make sure everyone is in the dict
assert shreyas in students
assert nica in students
assert harsha in students
assert cartman in students
assert timmy in students

#make sure no one else is in the dict
assert ~(not_there in students)


#test __lt__ method
assert cartman < timmy
assert timmy > harsha
assert harsha < nica
assert nica < shreyas
assert shreyas > cartman

#do a visible check of sorting
print sorted(students)

#check tie break strategy
otherShreyas = student('shreyas', 3.99, 24)
assert otherShreyas < shreyas
otherShreyas.name = 'z'
assert otherShreyas > shreyas
otherShreyas.name = 'shreyas'
otherShreyas.age = 25
otherShreyas.GPA = 4
assert otherShreyas > shreyas

#cmp GPA, break on name then age
mycmp = lambda x,y: lessGPA(x,y) if isinstance(x,student) and isinstance(y,student) else NotImplemented
lessGPA = lambda x,y:-1 if (x.GPA < y.GPA) \
    else 1 if(x.GPA>y.GPA) \
    else lessName(x,y)
lessName = lambda x,y:-1 if (str(x.name).lower() < str(y.name).lower()) \
    else 1 if (str(x.name).lower() > str(y.name).lower()) \
    else lessAge(x,y)
lessAge = lambda x,y:-1 if (x.age < y.age) else 1

#some assertions based on expected behavior
assert mycmp( cartman,timmy) == -1
assert mycmp( timmy , harsha ) == -1
assert mycmp(harsha , nica ) == -1
assert mycmp(nica , shreyas) == -1
assert mycmp(shreyas, cartman) == 1

#test tie breaking strategy, ensure age is last compared
otherTimmy = student('timmy', 1.2, 15)
assert mycmp(otherTimmy,timmy) == -1

#make sure sorting on works on two student objects
assert mycmp(shreyas, 30) == NotImplemented

#do a visible check of sorting
print sorted(students, mycmp)
