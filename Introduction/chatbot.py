details={}
print("Hi,I am Nemo.I will be guiding you for your Job Application")
stop=False
while stop==False:
    name=input("What is your Name ")
    details["Name"]=name
    while len(name) <3 or len(name)>18:
        print("Enter a valid name")
        name=input("What is your Name ")
    details["Name"]=name 
    print(f"Hi {name} hope you are fine .")

    #checking e mail
    email=input("Enter your Email id")
    while "@gmail.com" not in email:
        print("Enter a valid email id ")
        email=input("Enter your Email id")
    details["E-mail id"]=email 

    #checking contact number
    phone_number=input("Enter your contact nnumber")
    while len(phone_number)!=10:
        print("Enter a valid 10 digit phone number")
        phone_number=input("Enter your contact number correctly")
    details["Contact number"]=phone_number


    #taking age
    age=input("Enter your age")
    details["Age"]=age


    #checking about graduation
    qualification=input('Are you an Engineering graduate in Coomputer Science --"YES" or " NO"' )
    while qualification !="YES":
        print("Sorry to inform you that you are not aligible for this job role ,I wish you all the best for your future ")
        stop=True
        break
        # qualification=input('Are you an Engineering graduate in Coomputer Science --"YES" or " NO"' )
    details["Gratuated"]=qualification 
    if stop==True:
        break

    
    #checking programming languages
    p_languages=list(map(str,input("Enter the programming languages you are proficient in.\nPlease enter the languages seperated bu space so that I can access your skills").split(" ")))
    while("Python" or "PYTHON" or "python" not in p_languages ):
        print("Sorry to inform you that my company is looking for an employee who is proficient in Python.\nSince you are not profficient in Python Programming Language you cannot go ahead with the rest of the application process.\nAll the best for your future endeavours")
        # p_languages=list(map(str,input("Enter the programming languages you are proficient in.\nPlease enter the languages seperated bu space so that I can access your skills").split(" ")))
        stop=True
        break
    details["Languages"]=p_languages 
    if stop==True:
        break
    
        
    #Experienced in AI
    AI=input(f"Hi {name} We are looking for an experienced employee who is upto date with the latest trent in AI industry \nEnter YES if you are proficient in  Machine learning or AI related concepts else Enter NO")
    if AI=="NO":
        print("Sorry to inform you that my company is looking for a candidate who can develop great AI application.\nsince you dont have enough expertice in this industry ,you wont be able to go ahead with the application")
        break
    
    
    #checking skills
    print("Theese are the skills our team is looking forward in pur employee :")
    print(r"Machine learning\nDeep Learning\nGen AI\nTensor flow\nPandas\Num Py\nSci-Kit Learn\nModel Training \nComputer vision\nPython Programming Language\nData Preprocessing\nPower BI\nData Analytics\nDataScience")
    skills=list(map(str,input("Please Enter the skills that you belive you are having.\nPlease seperate the skills by comma ,because it will make it simple for me to acess your skills").split(" ")))
    if len(skills)<10:
        print("After carefully inspecting your skills ,We find that you dont have the necessary skills that we are looking in our employee \nI wish all the best for your future endeavours")
        break
    details["Skills"]=skills

    
    #industry experience
    experience=int(input("How many years of Experience do you have in Python Programming language"))
    while experience<3:
        print("I am sorry to inform you that you wont be able to continue with the application process \nWe dont find the necessary industry experience we are looking in our future employee in you \nAll the best for your future endeavours")
        # experience=int(input("How many years of Experience do you have in Python Programming language"))
        stop=True
        break
    details["Python_Experience"]=experience 
    if stop==True:
        break

    #previous company
    company=input("Enter the name of the company you are working in")
    details["Previous Company"]=company
    print("Good,So you have experience working in top companies")

    
    #current salary
    current_salary=input("Enter the current salary you are being paid in your company")
    details["Current Salary"]=current_salary

    #Expected salary
    expected_salary=input("Enter the salary you are expecting from our company for this job")
    while expected_salary>current_salary+((30*current_salary)/100):
        print("Sorry to inform you that you are having unreal expectations about the salary.\nIt is not an industry standard to ask more than 30 percent hike from your current job\nSo please mention salary according to industry standards")
        xpected_salary=input("Enter the salary you are expecting from our company for this job")
    details["Expected Salary"]=expected_salary

    #notice period
    notice_period=input("If you have notice period in your company please enter the notice period in months")
    while notice_period>2:
        print("We are looking for an employee who can join immediatly\nYou you can join within one month you may proceed with the aplication .\nPlease contact your current employer and confirm the notice period")
        notice_period=input("If you belive you van be flexible with the notice period please mention 1 month notice period and proceed with the application")

    details["Notice Period"]=notice_period
    
    
    #project description
    project=input("Give a brief Description about the project that you have done:Give the best project that you can showcase")
    details["Project"]=project
    print("Good , Seems like you have done a very good project , incorporating most of the python concepts\nYou semm like a really good employee to our company")
    

    #referal
    referal=input("Enter YES if you have friends or relatives working in our company ,if not any enter NO")
    if referal=="YES":
        referal_id=input("Enter the Referal ID of the employee working in our company")
        details["Referal_id"]=referal_id
    
    #came to know
    details["Enquiry"]=input("Where did you come to know about our hiring ")
    print("You are shortlisted for the Aptitude test that will be attending in your headoffice in Bangalore\nThe date and the other details will be mailed to your personal email id .")

print(details)