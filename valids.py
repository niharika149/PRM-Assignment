class Triangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_triangle(self,l):
        if len(l)==3 and (l[0]+l[1])>l[2]:
            return "Valid Triangle"         
        else:
            return "Invalid Triangle"
class Rectangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_rectangle(self,l):
        if len(l)==4 and  (l[0]==l[2]) and (l[1]==l[3]):
            return "Valid Rectangle"         
        else:
            return "Invalid Rectangle"
triang=list(map(int,input("Enter the size lenght of traingle : ").split()))
rect=list(map(int,input("Enter the size lenght of rectangle : ").split()))
triangle=Triangle(triang)       
print(triangle.validate_triangle(triang))
rectangle=Rectangle(rect)
print(rectangle.validate_rectangle(rect))