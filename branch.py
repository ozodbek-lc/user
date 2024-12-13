class Student:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def malumot(self):
        return f"ismi : {self.name}\ntelefon raqamami : {self.phone}"

student1=Student("ali","+998906881019")
print(student1.malumot())