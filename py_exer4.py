data = []
class Enrollment():
    def printSubject():   
        print("----------LISTS OF SUBJECTS----------")

        print("\n".join(map(lambda sub: str(data.index(sub)+1) +" - " +sub, data )))     
    def addSubject(units):
        done=True
        while (done):
            print("----------ADDING SUBJECTS----------")
            subject = input("Enter subject: ")
            if subject in data:
                print("***",subject,"is already enrolled ***")
                continue
            elif units  >=24:
                print("***","Subjects exceeded to 24 units","***")
                done = False
            else:
                data.append(subject)
                print(subject+" successfully added!")                    
                done= False
    
    def dropSubject():
        pass
    
studentName= input("Enter your name: ")
print("Welcome",studentName)
while True:
    print("----------MAIN MENU----------")
    units = (len(data)) * 3    
    print("Current units enrolled",units, "\n1-add\n2-drop\n3-print\n4-exit")    
    choice = input("Enter your choice: ")
    if choice in ['1','2','3','4']:
        if choice == '1': Enrollment.addSubject(units)
        elif choice == '2': Enrollment.dropSubject()            
        elif choice =='3': Enrollment.printSubject()            
        elif choice == '4':
            print("Exiting.... ")
            print("Thank youu!")
            exit()                
    else:
        print("***NO CHOICE**")
        continue
#Created By Raizen Sangalang
