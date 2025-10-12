class Student():
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    
    def Average (self):
        '''print("Hello", self.name, self.marks)
         sum=0
         for i in self.marks:
             sum += i
         avg=sum/3
         print("Average:", avg)'''
        sum=self.marks1 + self.marks2 + self.marks3
        avg=sum/3
        print("Hello", self.name, "Your Average is: ", avg)

s1=Student("Harsh", 96, 46, 89)
s1.Average()
s2=Student("Riya", 79,16,91)
s2.Average()
s3=Student("Kartik", 13, 46, 37)
s3.Average()