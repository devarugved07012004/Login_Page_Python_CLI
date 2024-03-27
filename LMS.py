# sign up
# login
# view details
# logout

class LMS:
    d=dict()
    k=0
    def Signup(self):
        name=input("Enter Name ")
        rollno=input("Enter Roll no ")
        password=input("Enter Password ")
        email=input("Enter Email ")
        if rollno in self.d:
            print("User aldready Exist")
        else:
            self.d[rollno]=[name,email,password]
            print("User Created Succesfully")
    
    def Login(self):
        rollno1=input("Enter Roll no ")
        if rollno1 not in self.d.keys():
            print("User not Exist")
        else:
            password1=input("Enter Password ")
            if password1 in self.d[rollno1]:
                print("Login Succesfull")
                self.k=1
            else:
                print("Incorrect Password")
    
    def View_details(self):
        if self.k==1:
            l=[]
            for i in self.d:
                l.append(i)
            for i in self.d.values():
                l+=i
            print("Name: ",l[1])
            print("Roll No: ",l[0])
            print("Email: ",l[2])
        else:
            print("Please Login First")
            
    def logout(self):
        print("Logout Succesful")

a=LMS()
while True:
    print('''
1.Signup
2.Login
3.View Details
4.Logout
      ''')
    p=int(input())
    if p==1:
        a.Signup()
    elif p==2:
        a.Login()
    elif p==3:
        a.View_details()
    else:
        a.logout()
        break