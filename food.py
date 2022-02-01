import mysql.connector
import random


db =mysql.connector.connect(host="localhost",user="root",password="Password123#", database = "OnlineFood")

mycursor=db.cursor()  



def about():
    print("Welcome to Our Foodies Restaurant".center(90,"~"))

    print("Foodies Restaurant has varied food options to choose from. Our program provides an easy interface to interact with providing a website where customers can view a restaurants menu, place an order and book a table.".center(20, " "))

    print("\n")

def main():
    print("Our Online System provides the following options:  ".center(90,"*"))


    print("""
            (1) ORDER FOOD
            (2) RESERVE TABLE
            (3) CANCEL TABLE
            (4) VIEW MENU
            (5) EXIT
                    """)

    print("Select one from the above options".center(90,"="))

    option = input("Enter Your Choice No.: ")
    print("\n")

    if option == "1": orderFood()
    elif option == "2": reserveTable()
    elif option == "3": cancelTable()
    elif option == '4': viewMenu()
    elif option == "5": exit()
    else:
        print("Try Again! Please, chose from the given options ")
    print("\n")
    main()



def exit():
    print("Thank You! Do Visit Us again!".center(90,"."))
    print("Closing The Application!".center(90,"*"))
    quit()

    
def reserveTable():
    print("Restaurant is open on all days from 12:00 PM to 11:00 PM")
    print("Tables can be booked in given time slots, 12:00 PM, 01:00 PM ,02:00 PM, 03:00PM, 05:00PM, 06:00PM,07:00PM,08:00PM,09:00PM,10:00PM,11:00PM")
    date = input("Enter date of reservation in DD-MM-YYYY format : ")
    time = int(input("Select time slot between 12 PM to 11PM, Enter in hours only:"))

    while time<1 and time>12:
        time=int(input("Enter valid time : "))
    s='select capacity,time from tableDates where date=%s'
    d=(date,)
    mycursor.execute(s,d)
    l=mycursor.fetchall()
    
    if l==[]:
        s='insert into tableDates values(%s,%s,%s)'
        d=(date,time,9)
        mycursor.execute(s,d)
        db.commit()
        bookTable(date,time)
    else:
        if int(l[0][1])==time:
            if l[0][0]>=1:
                s='update tableDates set capacity=%s where date=%s and time=%s'
                d=(l[0][0]-1,date,time)
                mycursor.execute(s,d)
                db.commit()
                bookTable(date,time)
            else:
                print("Tables not available at the given time ")
        else:
            s='insert into tableDates values(%s,%s,%s)'
            d=(date,time,9)
            mycursor.execute(s,d)
            db.commit()
            bookTable(date,time)
    print("\n")
    main()

            
def bookTable(d,t):

    print("Enter your details!".center(90,"."))

    name=input("Enter your name : ")
    phone=input("Enter your phone number : ")
    s='select b_id from tableReservation'
    mycursor.execute(s)
    l=mycursor.fetchall()
    id=random.randint(1,100000)
    while id in l:
        id=random.randint(1,100000)
    s='insert into tableReservation values(%s,%s,%s,%s,%s)'
    d=(d,t,name,phone,id)
    mycursor.execute(s,d)
    print("Booking successful")
    print("Your booking id is ",id)
    print("\n")
    db.commit()
                 
def cancelTable():

    i=int(input("Enter booking id : "))
    try:
        b='select date,time from tableReservation where b_id=%s'
        q=(i,)
        mycursor.execute(b,q)
        l=mycursor.fetchone()
        date=l[0]
        time=l[1]
        sql1='delete from tableReservation where b_id=%s'
        d1=(i,)
        mycursor.execute(sql1,d1)
        a='select capacity from tableDates where date=%s and time=%s'
        d2=(date,time)
        mycursor.execute(a,d2)
        l=mycursor.fetchone()
        sql2='update tableDates set capacity=%s where date=%s and time=%s'
        d2=(l[0]+1,date,time)
        mycursor.execute(sql2,d2)
        db.commit()
        print("Cancellation successful!")
        print("\n")
        main()
    except:
        print("No booking found! ")
        print("\n")
        main()
    
def orderFood():
        
        
    print("Let's Get You Some Food!".center(90,"."))
    name=input("Enter your name : ")
    phno = input("Enter your phone number: ")
    location  =  input("Enter the location : ")
    s='select cust_id from cust_details'
    mycursor.execute(s)
    data = mycursor.fetchall()
    id = random.randint(1,100000)
    sql='insert into cust_details values(%s,%s,%s,%s)'
    x=(id,name,phno,location)
    mycursor.execute(sql,x)
    db.commit()
    chooseMenu(id)
    print("\n")
    main()
        
        
                                        
def chooseMenu(cid):
    print("Choose What you Wish To Eat/Drinks".center(90,"."))

    print("Our Online System provides the following options: ".center(90,"*"))

    lis=['starters','maincourse','desserts','drinks']
    total=0
    for i in lis:
        print("|NO|".center(30," ")+"|FOOD NAME|".center(30," ")+"|PRICE|".center(30," "))
        mycursor.execute("select * from "+i)
        for x in mycursor:
            no = x[0]
            name = x[1]
            price = x[2]
            print(str(no).center(30," ") + str(name).center(30," ")  + str(price).center(30," "))
        print("\n")
        k=input("Do you want "+i+"? press yes or no : ")
        while True:
            if k=='yes':
                while True:
                    fid=input("Enter FID : ")
                    q=int(input("Enter quantity : "))
                    z='select fname,fprice from '+i+' where fid = %s'
                    w=(fid,)
                    mycursor.execute(z,w)
                    l=mycursor.fetchone()
                    fname,fprice=l[0],l[1]
                    cost=q*fprice
                    s=(cid,fid,fname,fprice,q,cost)
                    x='insert into orders values(%s,%s,%s,%s,%s,%s)'
                    mycursor.execute(x,s)
                    db.commit()
                    a=input("Enter 0 to quit ")
                    if a=='0':
                        k='no'
                        break
            elif k=='no':
                break
            else:
                k=input("enter a valid string yes/no : ")

    print("\n")
            
    total_bill=0
    print("Your bill is : ")
    sql='select fname,price,quantity,cost from orders where cust_id=%s'
    d=(cid,)
    mycursor.execute(sql,d)
    l=mycursor.fetchall()
    j=0
    print("s.no".center(15," ")+"food name".center(15," ")+"price".center(15," ")+"quantity".center(15," ")+"cost".center(15," "))
    for i in l:
        print(str(j).center(15," ")+str(i[0]).center(15," ")+str(i[1]).center(15," ")+str(i[2]).center(15," ")+str(i[3]).center(15," "))
        j+=1
        total_bill+=i[3]
    s="Total amount to be paid is : "+str(total_bill)
    print(s.center(90," "))
    print("\n")

def viewMenu():
    print("Our Online System provides the following categories and food items in our FoodMenu: ".center(90,"*"))
    print("\n")
    lis=['starters','maincourse','desserts','drinks']
    for i in lis:
        print("\n")
        print(i.upper().center(90,"."))
        print("|NO|".center(30," ")+"|FOOD NAME|".center(30," ")+"|PRICE|".center(30," "))
        mycursor.execute("select * from "+i)
        for x in mycursor:
            no = x[0]
            name = x[1]
            price = x[2]
            print(str(no).center(30," ") + str(name).center(30," ")  + str(price).center(30," "))
    print("\n")
    main()

about()
main()


