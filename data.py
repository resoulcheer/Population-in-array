import pprint

people = {'Pipo': 'age: 20, sex: Male, Birthday: 9/4/2541',
          'Deedo': 'age 19, sex: Female, Birthday: 1/3/2540',
          'Jele': 'age 21, sex: Female, Birthday: 30/9/2539',
          'Yoyo': 'age 22, sex: Male, Birthday: 23/12/2538'}

def Add(name):
    age = input("age: ")
    sex = input("sex: ")
    bd = input("Birthday(Example: 5/12/2560): ")
    people[name] = "age: " + age + ", sex: " + sex + ", Birthday: " + bd
    return(pprint.pprint(people))

def Search(name):
    for i in people:        
        if i == name:
            return people[name]
    return( "No Data")

def Delete(name):
    for i in people:        
        if i == name:                        
            del people[name]
            return(pprint.pprint(people))
    print( "No Data")

IsActive = True;

def Choice(choice):
    while IsActive:
        if choice == "1":
            name = input("name: ")
            Add(name)                  

        elif choice == '2' :
            name = input("name: "'') 
            print(Search(name))

        elif choice == '3' :
            name = input("name: "'') 
            Delete(name)

        elif choice == 'Q' :
            exit()

        else:
            return Choice(input("Error, Please Enter again: "))
        
        print("1:Add")
        print("2:Search")
        print("3:Delete")
        print("Q:Quit")
        choice = input("Enter your choice: ")

print("1:Add")
print("2:Search")
print("3:Delete")
print("Q:Quit")
choice = input("Enter your choice: ")
print(Choice(choice))
