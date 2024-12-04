class Student:
    def __init__(self, height, year, hometown):
        self.height = height
        self.year = year
        self.hometown = hometown

    def learning(self):
        print('This student is studying at UniVersity.')

    def gotohometown(self):
        print('This student is away at hometown.')

ali = Student(170, 3, 'Selangor') #class 'Student' instantiation to create Object 'ali'
david = Student(150, 2, 'Perak')

print(ali.height)
print(ali.year)
print(ali.hometown)
ali.learning()  #Method
print('David') + david.gotohometown()

# print(type(ali.height))
# print(type(ali.year))
# print(type(ali.hometown))