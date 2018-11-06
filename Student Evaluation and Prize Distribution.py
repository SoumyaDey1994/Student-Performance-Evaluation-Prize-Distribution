student_NameWithMarks={};               # Dictonary Which Contains Student Name and His/Her Total Marks
performanceReward=(500,300,100);        # Reward for Top 3 Performer

def displayMainMenu():                  #Dispaly The Main Menu
    print();
    print("\t\tEnter 1 to Enter Student Details ");
    print("\t\tEnter 2 to Edit Student Details ");
    print("\t\tEnter 3 to Evaluate ");
    print("\t\tEnter 4 to Display All Student Details ");
    print("\t\tEnter 5 to quit" );
    print();
    userChoice=int(input("Enter Your Choice(1-5): "));
    return userChoice;

def performActions(userChoice):         # Operations Corresponds to User Choice
    if(userChoice==1):
        enter_Student_Details();
    elif(userChoice==2):
        update_Student_Details();
    elif(userChoice==3):
        evaluate_students();
    elif(userChoice==4):
        printAllStudentListWithMarks();
    elif(userChoice==5):
              quit();
    else:
        print("\nInvalid Option Selected!!!! Please Choose a valid Option between(1-5)....");
        userChoice=displayMainMenu();
        performActions(userChoice);
        
def enter_Student_Details():            # Operation to Add New Student Details
    print();
    name=input("Enter The Name of the Student: ");
    userAnswar= checkIfStudentAlreadyExists(name);
    if(userAnswar== ""):
        marks=int(input("Enter {}'s Total Marks(in 1000): " .format(name)));
        student_NameWithMarks[name.upper()]=marks;      # Adding Student in Student List
        
    elif userAnswar.upper()=="NO" or userAnswar.upper()=="N":
        print("\nGoing back to main Menu.........");
        userChoice=displayMainMenu();       # Calling Menu Display Function
        performActions(userChoice);
        
    elif userAnswar.upper()=="YES" or userAnswar.upper()=="Y":
        marks=int(input("Enter {}'s Modified Total Marks(in 1000): " .format(name)));
        student_NameWithMarks[name.upper()]=marks;
    else:
        print("Invalid Option Entered..!! Please Enter Your Answar as Yes or No");
        print("Going back to Main Menu...............");      
        userChoice=displayMainMenu();       # Calling Menu Display Function
        performActions(userChoice);
        
def checkIfStudentAlreadyExists(name):      # Check wheather Student's Name ASlready exists in the List or not
    userAnswar="";                          # If yes, the prompt user with an Alert "Do You want to Override ??!! "
    if name.upper() in student_NameWithMarks.keys():
        print();
        print("Student Having Name {} Already Exists in the List.... Do You want to Override the Existing Record ??(yes/No) " .format(name), end='');
        userAnswar=input();
    return userAnswar;
    
def getUserUpdateWish():                # Available Update  Options
    print();
    print("Enter 1 to Update Only Student's Name ");
    print("Enter 2 to Update Only Student's Total Marks ");
    print("Enter 3 to Update Both Student's Name and Total Marks ");
    print("Enter 4 to Back to Main Menu ");
    print();
    userWish= int(input("Please Select Your Option(1-4): "));
    return userWish;

def update_Student_Details():           #Operation to Update Existing Student Record
    print();
    userWish= getUserUpdateWish();      # Ask for user's Choice of Update
    if(userWish >=1 and userWish<=3):
        studentDetails=getStudent();
        studentName=studentDetails[0];
        totalMarks=studentDetails[1];
        
    if(userWish==1):                    #Update Only Student Name
        updatedName=input("Enter Modified name of the Student: ");
        student_NameWithMarks[updatedName.upper()]=totalMarks;
        del student_NameWithMarks[studentName];
        print(".............Record Updated Succesfully...................");
        
    elif(userWish==2):                  #Update Only Student Total Marks
        updatedMarks=int(input("Enter Updated Marks of {}" .format(studentName)));
        student_NameWithMarks[studentName]=updatedMarks;
        print(".............Record Updated Succesfully...................");
        
    elif(userWish==3):                  #Update Both Student Name and Total Marks
        updatedName=input("Enter Modified name of the Student: ");
        updatedMarks=int(input("Enter Updated Marks of {}: " .format(updatedName.upper())));
        student_NameWithMarks[updatedName]=updatedMarks;
        del student_NameWithMarks[studentName.upper()];
        print(".............Record Updated Succesfully...................");
        
    elif(userWish==4):                  #Go Back to Main Menu
        userChoice=displayMainMenu();
        performActions(userChoice);
        
    else:                               # Alert!!!! Invalid Option Selected
        print("\nInvalid Choice..... Please Enter a Valid Option......");
        update_Student_Details();
        
def getStudent():                       #Get Student Name from user as Input and then Return Complete Details of The Student
    print();
    print("Enter The Student's Name whose Record You want to Update: ", end='');
    studentName=input();
    marks=student_NameWithMarks.get(studentName.upper());
    if marks is not None:
        return [studentName.upper(), marks];
    else:
        print("\n No Such Student Exists in Our List..........");
        userChoice=displayMainMenu();
        performActions(userChoice);

def evaluate_students():                # Evaluate Students Performance
    listOfAllMarksDesc=(list(sorted(student_NameWithMarks.values())))[::-1];    # Fetch Marks of Every Student in Decending Order
    toppers_score=get_Top3Score(listOfAllMarksDesc);
    top3Student=get_Top3StudentName(toppers_score);
    congratulateExcellentPerformers(listOfAllMarksDesc);
    displayNameOfTop3(top3Student);
    
def get_Top3Score(listOfAllMarksDesc):  #Get Top 3 Score
    toppers_score=[];                   # List of Top 3 Scores 
    for marks in listOfAllMarksDesc:
        if(len(toppers_score)==3):
            break;
        elif(marks in toppers_score):
            pass
        else:
            toppers_score.append(marks);
    return toppers_score

def get_Top3StudentName(toppers_score): # Get Top 3 Student Name
    toppersList=[];                     # List of Names of Top Students
    for marks in toppers_score:
        for item in sorted(student_NameWithMarks.items()):
            if(len(toppersList)==3):
                break;
            if(marks==item[1]):
                student=item[0];
                toppersList.append(student);
    return toppersList;

def congratulateExcellentPerformers(listOfAllMarksDesc):    # Congratulate Excellent Performers who have scored 950 or Above
    ExcellentPerformers=[];
    print("\n\t......Heartiest Congratulation to All the Mentioned Student for their Brilliant Performance......\n");
    for item in sorted(student_NameWithMarks.items()):
            if(item[1]>=950):
                student=item[0];
                ExcellentPerformers.append(student);
                print("\t\t %s" %(student));
            else:
                pass
        
def displayNameOfTop3(top3Student):     #Dispaly Top 3 Student Name along with their Reward Prize Money
    rewardVariable=0;
    print("\n\n\t\t\t.........Top Performers Are.......... \n");
    for name in top3Student:
        print("\tName:"+name+"\t\tScore: "+str(student_NameWithMarks[name])+"\t\t"+"Reward: "+repr(performanceReward[rewardVariable])+"$ Cash Prize");
        rewardVariable=rewardVariable+1;
        
def printAllStudentListWithMarks():     # Print All Student with Their Total Marks
    for student in student_NameWithMarks:
              print("Student Name: {}\tTotal Marks Obtained: {}" .format(student,student_NameWithMarks[student]));
              
while True:
    userChoice=displayMainMenu();       # Calling Menu Display Function
    performActions(userChoice);         # Trigger Action based on User's Choice
    

