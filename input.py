maths = int(input("maths marks: "))
english = int(input("english marks: "))
kiswahili = int(input("kiswahili marks: "))
physics = int(input("physics marks: "))
chemistry = int(input("chemistry marks: "))
history = int(input("history marks: "))
biology = int(input("biology marks: "))
computer = int(input("computer marks: "))

average = (maths + english + kiswahili + physics + chemistry + history + biology + computer)/8

if average >=88:
    print(f"average marks: {average}% - grade A: Excellent work!")
elif average >=75:
    print(f"average marks: {average}% - grade B: Very Good work!")
elif average >=70:
    print(f"average marks: {average}% - grade C: Good work!")
else:
    print(f"average marks: {average}% - grade D: Work Harder!")