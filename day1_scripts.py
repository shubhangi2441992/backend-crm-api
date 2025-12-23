'''
Username: shubhangi2441992
Password: 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
'''

def myname(name):
    return f"my name is {name}"

print ("do you know my name?", myname("shubhangi"))

fruits=["apple","orange","greps"]
print ("my feverate fruit is",fruits[1])

persone={"name":"shubhangi","age":"34"}
print ("my age is",persone["age"])

try:
    num=int(input("enter the number: "))
    print (10/num)
except ZeroDivisionError:
    print("Can not devide by zero")
except ValueError:
    print("Invalid number")