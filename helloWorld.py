print("Hello World!")

lastname=input("Enter your lastname: ")
if (len(lastname)<=15):
    print("SAT-competible")
else:
    print("SAT-incompetible")

totalmoneyused=0
money=[]
for i in range(7):
    spent=int(input("How much money did you spend today? "))
    totalmoneyused=totalmoneyused+spent
    money.append(spent)
    maxmoney=max(money)
print("You used an average of", totalmoneyused/7, "baht per day")
print("Your maximum amount of money used per day is ", maxmoney, "baht")

phonenum=input("Phone number(xxx-xxx-xxxx): ")
def sum_digits(phonenum):
    return sum(int(ch) for ch in phonenum if ch.isdigit())
print(sum_digits(phonenum))

phonenum1=input("phone num1: ")
phonenum2=input("phone num2: ")
def sum_digits(phonenum1):
    return sum(int(ch) for ch in phonenum1 if ch.isdigit())

def sum_digits(phonenum2):
    return sum(int(ch)for ch in phonenum2 if ch.isdigit())

if sum_digits(phonenum1)>sum_digits(phonenum2) and sum_digits(phonenum1)!=60:
    print("The first phone number is more auspicious")
elif sum_digits(phonenum1)==60:
    print("The first phone number is the least auspicious")
elif sum_digits(phonenum2)==60:
    print("The second phone number is the least auspicious")
elif sum_digits(phonenum2)>sum_digits(phonenum1) and sum_digits(phonenum2)!=60:
    print("The second phone number is more auspicious")
    
thbudyr=int(input("Thai year: "))
yr=thbudyr-543
if ((yr%400==0)or(yr%100!=0)and(yr%4==0)):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
    
age=int(input("Age: "))
married=str(input("Are you married?(y-yes, n-no) "))
if married=="y" or married=="n":
    if age>=20:
        print("You are not a minor")
    elif age<20 and married=="y":
        print("You are not a minor")
    elif age<20 and married =="n":
        print("You are a minor")
else:
    print("Please enter y or n")

words=[]
while True:
    add=input("Enter a word: ")
    print("word added")
    if add=="exit":
        break;
    elif add in words:
        print("The word is already in the list")
    else:
        words.append(add)
print(words)