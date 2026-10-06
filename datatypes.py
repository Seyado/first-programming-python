maths = int(input("maths marks: "))
english = int(input("english marks: "))

average = (maths + english)/2
if average >=88:
    print(f"average marks: {average}% - grade A: Excellent work!")
elif average >=75:
    print(f"average marks: {average}% - grade B: Very good!")
elif average >=70:
    print(f"average marks: {average}% - grade c: good!")
else:
    print(f"average marks: {average}% - grade D pull up your socks!")



