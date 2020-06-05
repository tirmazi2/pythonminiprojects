#Admission Automation system
#Developer: tirmazi2

import random
import time

#kind of data base
registeredUser = [["admin"], ["admin"], ["admin@gmail.com"]]
ineligibleUser = [[],[],[]]
venue = ["Hall 1","Hall 2","Hall 3","Hall 4","Hall 5"]
MCQS = ["""1. International Space Station (ISS) orbits the Earth for ____ times per day.
        (A) 5.5 
        (B) 10.5
        (C) 15.5
        (D) 20.5""", 
        """2. The play “The Doctor’s Dilemma” that describes moral dilemmas because of limited medical resources and business was written by
        (A) William Shakespeare
        (B) Bernard Shaw
        (C) Vladimir Nabokov
        (D) Thomas More""", 
        """3. The famous “Mount Fuji” is the highest mountain in
        (A) China
        (B) Japan
        (C) Fiji
        (D) Vietnam""", 
        """4. We live on the planet Earth. According to the scientists, the Earth was formed about _____ years ago.
        (A) 4.6 million
        (B) 5.6 million
        (C) 4.6 billion
        (D) 5.6 billion""", 
        """5. Dinosaurs and many other species were extinct about _____ years ago.
        (A) 55 million
        (B) 65 million
        (C) 75 million
        (D) 85 million""", 
        """6. The deepest hole in the Earth, ‘Kola Superdeep Borehole’ on Russia’s Kola Peninsula, is about _____ feet deep.
        (A) 10,000
        (B) 20,000
        (C) 30,000
        (D) 40,000"""]
mcqAnswers = ["C", "B", "B", "C", "B", "D"]

#Registers a user
def register():
    print("Please provide information to proceed!")
    
    username = input("Username: ")
    while(username in registeredUser[0]):
        print(username + " already registered!")
        username = input("Username: ")
    
    username.upper()
    registeredUser[0].insert(len(registeredUser[0]), username)

    email = input("Email: ")
    
    while(("@" in list(email)) != True):
        print("Please provide a valid email as: xyz@example.com")
        email = input("Email: ")
    
    registeredUser[2].insert(len(registeredUser[2]), email)

    password = input("Choose a password: ")
    passwordRetype = input("Retype password: ")
    
    while(password != passwordRetype):
        print("Passwrod not matched, try again!")
        password = input("Choose a password: ")
        passwordRetype = input("Retype password: ")
    
    registeredUser[1].insert(len(registeredUser[1]), password)
    print("Registered successfully!")

    return email

#Form filling
def fillForm(email):
    uname = input("Username: ")
    psswd = input("Password: ")
    valid = False

    if(uname in registeredUser[0]) and (psswd in registeredUser[1]):
        print("Welcome " + uname.upper() + ", please provide your other information.")
    
        fullName = input("Full Name: ")
        fatherName =  input("Father Name: ")
        fullName.upper()
        fatherName.upper()
    
        print("1- BS(IT) \n2- BS(CS) \n3- BBA \n4- Media Studies")
        program = input("Please make a choice: ")
        if(program == "1"):
            program = "BS(IT)"
        elif(program == "2"):
            program = "BS(CS)"
        elif(program == "3"):
            program = "BBA"
        elif(program == "4"):
            program = "Media Studies"
    
        interDegreeList = ["FSC", "ICS", "FA", "I.Com"]
        intermediate = input("Name of your last degree: ")
        if(intermediate.upper() not in interDegreeList):
            print("You need an equvalence certificate from IBCC")
            intermediate += " (Verification required)"
            intermediate.upper()

        isPassed = input("Please enter your overall % in last exam: ")
        while(float(isPassed) > 100):
            print("Sorry you typed an invalid percentage!")
            isPassed = input("Please enter your overall % in last exam: ")
        
        if(float(isPassed) < 50.00):
            print("Sorry you can't proceed further, you do not meet eligibility criteria!")

            #Maintains another list of ineligible users
            ineligibleUser[0].insert(len(ineligibleUser[0]), uname)
            ineligibleUser[1].insert(len(ineligibleUser[1]), psswd)
            ineligibleUser[2].insert(len(ineligibleUser[2]), email)
            
            #Remove ineligible user from register users list
            registeredUser[0].pop()
            registeredUser[1].pop()
            registeredUser[2].pop()

            fullName = fatherName = program = intermediate = testDate = testVen = ""
            return fullName, fatherName, program, intermediate, testDate, testVen, valid
        else:
            print("Operation successful!")
            day = random.randrange(1,31)
            month = random.randrange(1,12)
            testDate = str(day) + "-" + str(month) + "-2020"
            testVen = random.randrange(0,5)
            valid = True
            return fullName, fatherName, program, intermediate, testDate, venue[testVen], valid
    else:
        print("Invalid username or password, make sure you're a registered user!")
        fullName = fatherName = program = intermediate = testDate = testVen = ""
        return fullName, fatherName, program, intermediate, testDate, testVen, valid

#Prints user information
def viewProfile(fullName, fatherName, program, intermediate, testDate, testVenue):
    print("User Information")
    print("Full Name: " + fullName)
    print("Father Name: " + fatherName)
    print("Enrolled Program: " + program)
    print("Intermediate Degree: " + intermediate)
    print("Test Date: " + testDate)
    print("Test Venue: " + testVenue)

def enteranceTest():
    score = 0
    index = 0
    print("Exam Time: 2 minutes")
    start = input("Please type 'start' to start exam: ")
    if(start == "start") or (start == "START"):
        for i in MCQS:
            print(i)
            choice = input("Option: ")
            if(choice == mcqAnswers[index]):
                score += 1
            index += 1
        
    print("You scored: " + str(score) + "/" + str(len(MCQS)))

    return score
        
def applyAdmission():
    print("\t\t\t\t\tWelcome to XYZ University")
    print("Registration")
    email = register()
    print("Registration > Fill Admission Form")
    fullName, fatherName, program, intermediate, testDate, testVenue, valid = fillForm(email)

    if(valid == True):
        print("Registration > Fill Admission Form > Verify your Profile")
        viewProfile(fullName, fatherName, program, intermediate, testDate, testVenue)
        print("Registration > Fill Admission Form > Verify your Profile > Entrance Test")
        score = enteranceTest()
        if(score >= 5):
            print("Hurray!, thanks for consider XYZ University. You can join as quickly as this month!")
        else:
            print("Sorry!, you could'nt qualify, better luck next time!")

    else:
        print("Exiting...")
        
#####################################################################################
###################################Execution Point###################################
#####################################################################################
applyAdmission()
