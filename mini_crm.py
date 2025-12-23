
users=[]
def add_user(name,age):
    users.append({"name":name,"age":age})
    print("User added successfully")


def list_user():
    if not users:
        print ("No users found")
    for user in users:
        print(user)

def delete_user(name):
    global users 
    users=[user for user in users if user["name"]!=name]
    print ("user deleted if exist")

add_user("shubhangi",33)
add_user("gaurav",34)
list_user()
delete_user("shubhangi")
list_user()
delete_user("ram")
list_user()