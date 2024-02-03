#define a person class with private attribute

#define a child class to inherit from person

class Person:
    def __init__(self,temperament,blood_group,salary,physique):
        self.temperament = temperament
        self.blood_group = blood_group
        self.__salary = salary
        self.physique = physique

    def social_media(self):
        return "TikTok"
    
    def marathon (self) :
        return "Stanchart"
    
myPerson = Person ("Sanguine", "O negative", "250m", "Tall Built")

print(myPerson)


class Child (Person):
    def __init__(self,temperament,blood_group,salary,physique):
        Person.__init__(self,temperament,blood_group,salary,physique)
                    

myChild = Child ("phlegmatic","A +ive"," 4000","skinny")

print(myChild.temperament)
print(myChild.blood_group)
print(myChild.physique)
print(myChild.social_media())
print(myChild.marathon())
