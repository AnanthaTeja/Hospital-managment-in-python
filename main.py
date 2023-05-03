import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet


print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome Hospital Management System                     *")
print("*                                                                          *")
print("****************************************************************************")
    
    
tries = 0
tries_flag = ""
while tries_flag != "Close the program" :
        Pateints_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
        Doctors_DataBase  = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()
                
        print("-----------------------------------------")
        print("|Enter 1 for Admin mode          |\n|Enter 2 for user mode           |")
        print("-----------------------------------------")
        Admin_user_mode = input("Enter your mode : ") 
        

        if Admin_user_mode == "1" :
                print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
                Password = input("Please enter your password : ")
                while True :
                    
                    if Password == "SRMAP123" :
                        print("-----------------------------------------")
                        print("|To manage patients Enter 1      |\n|To manage docotrs Enter 2       |\n|To be back Enter B              |")
                        print("-----------------------------------------")
                        AdminOptions = input ("Enter your choice : ")
                        AdminOptions = AdminOptions.upper()
                        
                        if AdminOptions == "1" :
                                print("-----------------------------------------")
                                print("|To add new patient Enter 1          |")
                                print("|To display patient Enter 2          |")
                                print("|To delete patient data Enter 3      |")
                                print("|To edit patient data Enter 4        |")
                                print("|To Back enter B                     |")
                                print("-----------------------------------------")
                                Admin_choice = input ("Enter your choice : ")
                                Admin_choice = Admin_choice.upper()
                                
                                if Admin_choice == "1" :
                                            try :       
                                                patient_ID = int(input("Enter patient ID : "))
                                                while patient_ID in Pateints_DataBase :     
                                                    patient_ID = int(input("This ID is available, please try another ID : "))                 
                                                Department=input("Enter patient department                : ")
                                                DoctorName=input("Enter name of doctor following the case : ")
                                                while(DoctorName):
                                                        if DoctorName in open('Doctors_DataBase.csv').read():
                                                            print("Doctor present")
                                                            break
                                                        else:
                                                            print("Doctor NOT present or Doctor name wrong")
                                                            DoctorName=input("Enter name of doctor following the case : ") 
                                                Name      =input("Enter patient name                      : ")
                                                Age       =input("Enter patient age                       : ")
                                                Gender    =input("Enter patient gender                    : ")
                                                phone     =input("Enter patient phone no                  : ")
                                                while(len(phone)!=10):
                                                        print("Enter valid phone number")
                                                        phone     =int(input("Enter patient phone no                  : "))
                                                RoomNumber=input("Enter patient room number               : ")
                                                Pateints_DataBase[patient_ID]=[Department,DoctorName,Name,Age,Gender,phone,RoomNumber]
                                                print("----------------------Patient added successfully----------------------")
                                            except :
                                                print("Patient ID should be an integer number")
                                        
                                elif Admin_choice == "2" :
                                            try :       
                                                patient_ID = int(input("Enter patient ID : "))
                                                while patient_ID not in Pateints_DataBase :
                                                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                print(patient_ID)
                                                print("\npatient name        : ",Pateints_DataBase[patient_ID][2])
                                                print("patient age         : ",Pateints_DataBase[patient_ID][3])
                                                print("patient gender      : ",Pateints_DataBase[patient_ID][4])
                                                print("patient phone no    : ",Pateints_DataBase[patient_ID][5])
                                                print("patient room number : ",Pateints_DataBase[patient_ID][6])
                                                print("patient is in "+Pateints_DataBase[patient_ID][0]+" department")
                                                print("patient is followed by doctor : "+Pateints_DataBase[patient_ID][1])
                                            except :
                                                print("Patient ID should be an integer number")
                                
                                elif Admin_choice == "3" :                                      
                                            try :       
                                                patient_ID = int(input("Enter patient ID : "))
                                                while patient_ID not in Pateints_DataBase :
                                                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                Pateints_DataBase.pop(patient_ID)
                                                print("----------------------Patient data deleted successfully----------------------")
                                            except :
                                                print("Patient ID should be an integer number")
                                        
                                elif Admin_choice == "4" :                                      
                                            try :       
                                                patient_ID=int(input("Enter patient ID : "))
                                                while patient_ID not in Pateints_DataBase :
                                                    patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                                                while True :
                                                    print("------------------------------------------")
                                                    print("|To Edit pateint Department Enter 1 :    |")
                                                    print("|To Edit Doctor following case Enter 2 : |")
                                                    print("|To Edit pateint Name Enter 3 :          |")
                                                    print("|To Edit pateint Age Enter 4 :           |")
                                                    print("|To Edit pateint Gender Enter 5 :        |")
                                                    print("|To Edit pateint phone no Enter 6 :      |")
                                                    print("|To Edit pateint RoomNumber Enter 7 :    |")
                                                    print("|To be Back Enter B                      |")
                                                    print("-----------------------------------------")
                                                    Admin_choice = input("Enter your choice : ")
                                                    Admin_choice = Admin_choice.upper()
                                                    if Admin_choice == "1" :
                                                        Pateints_DataBase[patient_ID][0]=input("\nEnter patient department : ")
                                                        print("----------------------Patient Department edited successfully----------------------")
                                                        
                                                    elif Admin_choice == "2" :
                                                        Pateints_DataBase[patient_ID][1]=input("\nEnter Doctor follouing case : ")
                                                        print("----------------------Doctor follouing case edited successfully----------------------")
                                        
                                                    elif Admin_choice == "3" :
                                                        Pateints_DataBase[patient_ID][2]=input("\nEnter patient name : ")
                                                        print("----------------------Patient name edited successfully----------------------")
                                                    
                                                    elif Admin_choice == "4" :
                                                        Pateints_DataBase[patient_ID][3]=input("\nEnter patient Age : ")
                                                        print("----------------------Patient age edited successfully----------------------")
                                                
                                                    elif Admin_choice == "5" :
                                                        Pateints_DataBase[patient_ID][4]=input("\nEnter patient gender : ")
                                                        print("----------------------Patient address gender successfully----------------------")
                                                        
                                                    elif Admin_choice == "6" :
                                                        Pateints_DataBase[patient_ID][5]=input("\nEnter patient phone no : ")
                                                        print("----------------------Patient phone no edited successfully----------------------")
                                                        
                                                    elif Admin_choice == "7" :
                                                        Pateints_DataBase[patient_ID][6]=input("\nEnter patient RoomNumber : ")
                                                        print("----------------------Patient RoomNumber edited successfully----------------------")
                                                
                                                    elif Admin_choice == "B" :
                                                        break
                                                        
                                                    else :
                                                        print("Please Enter a correct choice")
                                            except :
                                                print("Patient ID should be an integer number")
                                                                             
                                else :
                                            print("Please enter a correct choice\n")
                                            
                        elif AdminOptions == "2" :                                                          
                            print("-----------------------------------------")
                            print("|To add new doctor Enter 1              |")
                            print("|To display doctor Enter 2              |")
                            print("|To delete doctor data Enter 3          |")
                            print("|To edit doctor data Enter 4            |")
                            print("|To be back enter B                     |")
                            print("-----------------------------------------")
                            Admin_choice = input ("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            
                            if Admin_choice == "1" :                                            
                                    try :       
                                        Doctor_ID = int(input("Enter doctor ID : "))
                                        while Doctor_ID in Doctors_DataBase :           
                                            Doctor_ID = int(input("This ID is unavailable, please try another ID : "))
                                        
                                        Department=input("Enter Doctor department : ")
                                        Name      =input("Enter Doctor name       : ")
                                        phone     =input("Enter Doctor phone no   : ")
                                        Doctors_DataBase[Doctor_ID]=[[Department,Name,phone]]
                                        print("----------------------Doctor added successfully----------------------")
                                    except :
                                        print("Doctor ID should be an integer number")
                                
                            elif Admin_choice == "2" :                                          
                                    try :       
                                        Doctor_ID = int(input("Enter doctor ID : "))
                                        while Doctor_ID not in Doctors_DataBase :
                                            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                        print("Doctor name    : ",Doctors_DataBase[Doctor_ID][0][1])
                                        print("Doctor address : ",Doctors_DataBase[Doctor_ID][0][2])
                                        print("Doctor is in "+Doctors_DataBase[Doctor_ID][0][0]+" department")
                                    except :
                                        print("Doctor ID should be an integer number")
                            
                            elif Admin_choice == "3" :                                          
                                    try :      
                                        Doctor_ID = int(input("Enter doctor ID : "))
                                        while Doctor_ID not in Doctors_DataBase :
                                            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                        Doctors_DataBase.pop(Doctor_ID)
                                        print("/----------------------Doctor data deleted successfully----------------------/")
                                    except :
                                        print("Doctor ID should be an integer number")

                            elif Admin_choice == "4" :                                          
                                    try :       
                                        Doctor_ID=input("Enter doctor ID : ")
                                        while Doctor_ID not in Doctors_DataBase :
                                            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                                        print("-----------------------------------------")
                                        print("|To Edit doctor's department Enter 1    |")
                                        print("|To Edit doctor's name Enter 2          |")
                                        print("|To Edit doctor's phone no Enter 3      |")
                                        print("To be Back Enter B                      |")
                                        print("-----------------------------------------")
                                        Admin_choice=input("Enter your choice : ")
                                        Admin_choice = Admin_choice.upper()
                                        if Admin_choice == "1" :
                                            Doctors_DataBase[Doctor_ID][0][0]=input("Enter Doctor's Department : ")
                                            print("/----------------------Doctor's department edited successfully----------------------/")
                                            
                                        elif Admin_choice == "2" :
                                            Doctors_DataBase[Doctor_ID][0][1]=input("Enter Doctor's Name : ")
                                            print("----------------------Doctor's name edited successfully----------------------")
                                            
                                        elif Admin_choice == "3" :
                                            Doctors_DataBase[Doctor_ID][0][2]=input("Enter Doctor's phone no : ")
                                            print("----------------------Doctor's phone no edited successfully----------------------")
                                        
                                        elif Admin_choice == "B" :
                                            break
                                        
                                        else :
                                            print("\nPlease enter a correct choice\n")
                                            
                                    except :
                                        print("Doctor ID should be an integer number")
                                            
                            elif Admin_choice == "B" :                                          
                                        break
                                    
                            else :
                                print("\nPlease enter a correct choice\n")
                        elif AdminOptions == "B":
                                break;
                    elif Password != "SRMAP123" :
                        if tries < 2 :
                            Password = input("Password incorrect, please try again : ")
                            tries += 1
                        else :
                            print("Incorrect password, no more tries")
                            tries_flag = "Close the program"
                            break
                
                    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Pateints_DataBase)
                    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
                    
                    
        elif Admin_user_mode == "2" :                                                                      
            print("****************************************\n|         Welcome to user mode         |\n****************************************")
            while True :
                print("\n-----------------------------------------")
                print("|To view hospital's departments Enter 1 |")
                print("|To view hospital's docotrs Enter 2     |")
                print("|To view patients' residents Enter 3    |")
                print("|To view patient's details Enter 4      |")
                print("|To be Back Enter B                     |")
                print("-----------------------------------------")
                UserOptions = input("Enter your choice : ")
                UserOptions = UserOptions.upper()
                if UserOptions == "1" :
                            print("Hospital's departments :")
                            for i in Doctors_DataBase :
                                print(" "+Doctors_DataBase[i][0][0])
                    
                elif UserOptions == "2" :                                           
                            print("Hospital's doctors :")
                            for i in Doctors_DataBase :
                                print(" ",Doctors_DataBase[i][0][1]," in ",Doctors_DataBase[i][0][0]," department, from ",Doctors_DataBase[i][0][2])
                                
                elif UserOptions == "3" :                                           
                    for i in Pateints_DataBase :
                        print(" patient name        : ",Pateints_DataBase[i][2])
                        print(" patient age         : ",Pateints_DataBase[i][3])
                        print(" patient gender      : ",Pateints_DataBase[i][4])
                        print(" patient phone no    : ",Pateints_DataBase[i][5])
                        print(" patient room number : ",Pateints_DataBase[i][6])
                        print(" patient is in ",Pateints_DataBase[i][0]," department")
                        print(" patient is followed by doctor : ",Pateints_DataBase[i][1])                
                elif UserOptions == "4" :                                           
                    try :               
                        patient_ID = int(input("Enter patient's ID : "))
                        while patient_ID not in Pateints_DataBase :
                            patient_ID = int(input("Incorrect Id, Please enter patient ID : "))
                        print(" patient name        : ",Pateints_DataBase[patient_ID][2])
                        print(" patient age         : ",Pateints_DataBase[patient_ID][3])
                        print(" patient gender      : ",Pateints_DataBase[patient_ID][4])
                        print(" patient phone no    : ",Pateints_DataBase[patient_ID][5])
                        print(" patient room number : ",Pateints_DataBase[patient_ID][6])
                        print(" patient is in "+Pateints_DataBase[patient_ID][0]+" department")
                        print(" patient is followed by doctor : "+Pateints_DataBase[patient_ID][1])
                    except :
                        print("Patient ID should be an integer number")
                elif UserOptions == "B":
                        break
        elif Admin_user_mode=="B":
                break
        else :
            print("Please choice just 1 or 2")
