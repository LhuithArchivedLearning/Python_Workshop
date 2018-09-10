from turtle import *


setup();
student_marks = [8,8,8,8,8,6,6,6,6,6]

def average(marks) :
    avg = sum(marks)//len(marks);
    return avg;

print("The average mark is", average(student_marks));

done();
