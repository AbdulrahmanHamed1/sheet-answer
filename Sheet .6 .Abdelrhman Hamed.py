#1)
file = open("sheet6.txt", "w")  
file.write("Hello from file")  
file.close()  

#2)
file = open("Sheet6.txt", "a")
file.write("Abdelrahman Hamed\n")  
file.close()

#3)
file = open("sheet6.txt", "a")
for x in range(1, 101):
    file.write(f"{x}\n") 
file.close()

#4)
with open("sheet6.txt", "r") as file:
    lines = file.readlines()  
if len(lines) >= 60:
    selected_lines = lines[49:60]
    print("Lines 50 to 60:")
    for line in selected_lines:
        print(line.strip())  
else:
    print("The file has less than 60 lines. Try adding more content.")
    
#json 
import json
users = [
    {"username": "Abdelrhman", "pass": "245vf"},
    {"username": "Hamed", "pass": "dv5d5v"},
    {"username": "Anas", "pass": "vs534"},
    {"username": "mohamed", "pass": "vdkc58"}
        ]
file = open('users.json', 'w')
json.dump(users, file)
file.close()
file = open('users.json', 'r')
users = json.load(file)
file.close()
print(f"First user: {users[0]['username']} , pass: {users[0]['pass']}")
users.append({"username": "Hamed", "pass": "m6969"})
file = open('users.json', 'w')
json.dump(users, file)
file.close()
print("User added")
u = input("Username: ")
p = input("Password: ")
file = open('users.json', 'r')
users = json.load(file)
file.close()
x = False
for user in users:
    if user['username'] == u and user['pass'] == p:
        x = True
        break
print("Success" if x else "Failed")

#Math Module
import math
r = 4.5
A = math.pi*r*r
print(f"The area of the circle is: {A:4f}")