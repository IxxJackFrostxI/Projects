import pickle
print("------------------------------------------")
print("**********Bank Management System**********")
print("------------------------------------------")

data = {}
list1 = ["Acc no.","Name","Address","Phone NO.","GOVT. ID.","ACC Type","Amount"]
list2 = []
def new():
    
    for item in list1:

        list2.append(input("Enter %s:"%item))
    
    
    data = dict(zip(list1,list2))
    obj=open("Database.txt","wb")
    pickle.dump(list2,obj)
    obj.close()
    print("-----------")
    print("acc created")
    print("-----------")

    
        

def exis():
    print(data)
    B=int(input("Enter your choice:\n1.Check balance\n2.Withdraw\n3.Deposite\n"))
    if B==1:
        print("-----------------------------")
        print("Your balance is:",data['Amount'])
        print("-----------------------------")
    elif B==2:
        wth=int(input("Enter amount to withdraw:"))
        tot=int(data[Amount]) - wth
        data[pin]["Amount"] = tot
        print("------------------------------")
        print("Your updated balance is:",data[pin]["Amount"])
        print("------------------------------")
    elif B==3:
        dep=int(input("Enter amount to Deposite:"))
        tot=int(data[pin]["Amount"]) + dep
        data[pin]["Amount"] = tot
        print("------------------------------")
        print("Your updated balance is:",data[pin]["Amount"])
        print("------------------------------")
        
def exi():
    exit()

while True:
    print("Please choose any one option:\n")
    print("1. New Customer")
    print("2. Existing Customer")
    print("3. Exit")
    print("")
    A = int(input("Enter a choice:"))
    if A==1:
        new()
    elif A==2:
        with open('Database.txt','rb') as f:
            ab = pickle.load(f)
            acnum=input("Please enter ACC NO.:")
            if acnum in ab:
                print("------------")
                print("record found")
                print("------------")
                exis()
            else:
                print("---------------")
                print("Invalid acc no.")
                print("---------------")
    elif A==3:
        exit()
    else:
        print("wrong input")
