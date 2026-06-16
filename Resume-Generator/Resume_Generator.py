# printing welcome message
print("\n---------------Welcome to Resume Generator---------------\n")

# Import required modules
import os
import subprocess
import random
from docx import Document  #this library helps python create a microsoft word document
 
# creating list to store all created resumes
resume_list = []

# predefined personal info descriptions
personal_info_list = [
    """A highly motivated and responsible individual with strong communication skills.
Able to work effectively both independently and as part of a team.
Quick learner with a positive attitude towards challenges and growth.
Dedicated to achieving organizational goals with sincerity and commitment.""",

    """An enthusiastic and hardworking person with a passion for continuous learning.
Possesses good problem solving skills and attention to detail.
Capable of adapting to new environments and handling responsibilities efficiently.
Eager to contribute skills and knowledge for organizational success.""",

    """A disciplined and focused individual with strong work ethics.
Able to manage time efficiently and complete tasks within deadlines.
Good interpersonal skills with the ability to collaborate in team environments.
Committed to personal and professional development.""",

    """A reliable and dedicated candidate with a strong sense of responsibility.
Skilled in communication and maintaining positive working relationships.
Open to learning new technologies and improving existing skills.
Aims to deliver quality work and contribute to company growth.""",

    """A self driven and goal oriented individual with a proactive mindset.
Strong analytical thinking and ability to solve problems effectively.
Comfortable working in dynamic environments and handling challenges.
Focused on building a successful career while supporting organizational objectives."""
]


# creating a Class called Resume
class Resume:

    # creating a constructor method to initialize resume details
    def __init__(self, Name, Age, Phone_Number, Email, Address, Skills, Languages, Hobbies, Experience, Education):
        self.Name = Name
        self.Age = Age
        self.Phone_Number = Phone_Number
        self.Email = Email
        self.Address = Address
        self.Skills = Skills
        self.Languages = Languages
        self.Hobbies = Hobbies
        self.Experience = Experience
        self.Education = Education 
        self.Personal_Info = random.choice(personal_info_list)          # Randomly assign one personal info description

    # creating a method called clear_resume to convert list to string
    def clear_resume(self):
        if type(self.Skills) == list:
            self.Skills = ", ".join(self.Skills)

        if type(self.Languages) == list:
            self.Languages = ", ".join(self.Languages)

        if type(self.Hobbies) == list:
            self.Hobbies = ", ".join(self.Hobbies)

        self.Email = self.Email.strip()        #strip removes spaces starting and ending of mail and doesnt remove space in between .

    # creating a method to update resume fields 

    def update_resume(self, Name=None, Age=None, Phone_Number=None, Email=None,
                      Skills=None, Languages=None, Hobbies=None, Experience=None, Education=None, Address=None):

        if Name is not None:
            self.Name = Name

        if Age is not None:
            self.Age = Age

        if Phone_Number is not None:
            self.Phone_Number = Phone_Number

        if Email is not None:
            self.Email = Email

        if Address is not None:
            self.Address = Address

        if Skills is not None:
            self.Skills = Skills

        if Languages is not None:
            self.Languages = Languages

        if Hobbies is not None:
            self.Hobbies = Hobbies

        if Experience is not None:
            self.Experience = Experience

        if Education is not None:
            self.Education = Education

  #creating a method called resume_format to print the details 
    def resume_format(self):
        education_text = ""

          # Loop through education list and format each entry

        for edu in self.Education:     
            education_text += f"""
       Qualification: {edu['qualification']}  
       Institution: {edu['institution']}
       Year of Completion: {edu['year']}
       Percentage: {edu['percentage']}
"""
# returning formatted resume string
        return f"""

       ----------------------------
       Resume Details
       ----------------------------

       Name = {self.Name}
       Age = {self.Age}
       Phone Number = {self.Phone_Number}
       Email = {self.Email}
       Address = {self.Address}

       Personal Info:
       {self.Personal_Info}

       Skills = {self.Skills}
       Languages = {self.Languages}
       Hobbies = {self.Hobbies}
       Experience = {self.Experience} years

       Education:
{education_text}
       """
 # Method to generate Word (.docx) resume
    def generate_docx(self):
        print(f"\n[*] Generating Word document for {self.Name}...")

 # Create filename using name
        filename = f"{self.Name.replace(' ', '_')}_Resume.docx"
        doc = Document()            #creates  a new empty word document
 # Add headings and content to document
        doc.add_heading(self.Name, 0)             # level=0 creates the document title (largest heading)

        doc.add_heading("Personal Info", level=1)       # level=1 creates major section headings such as Skills, Education, etc.
        doc.add_paragraph(self.Personal_Info)

        doc.add_heading("Basic Details", level=1)
        doc.add_paragraph(f"Age: {self.Age}")
        doc.add_paragraph(f"Phone: {self.Phone_Number}")
        doc.add_paragraph(f"Email: {self.Email}")
        doc.add_paragraph(f"Address: {self.Address}")

        doc.add_heading("Skills", level=1)
        doc.add_paragraph(str(self.Skills))

        doc.add_heading("Languages", level=1)
        doc.add_paragraph(str(self.Languages))

        doc.add_heading("Hobbies", level=1)
        doc.add_paragraph(str(self.Hobbies))

        doc.add_heading("Experience", level=1)
        doc.add_paragraph(f"{self.Experience} years")

        doc.add_heading("Education", level=1)

        for edu in self.Education:                                  #add education details
            doc.add_paragraph(f" {edu['qualification']}")
            doc.add_paragraph(f"  Institution: {edu['institution']}")
            doc.add_paragraph(f"  Year of Completion: {edu['year']}")
            doc.add_paragraph(f"  Percentage: {edu['percentage']}")

        file_path = os.path.abspath(filename)            # converts a simple fine name into the full path where the resume is saved
        doc.save(file_path)                       

        print(f" Word file saved at: {file_path}")  

        try:                        # Try opening the file automatically
            if os.name == 'nt':         #windows
                os.startfile(file_path)
            else:
                subprocess.call(['open', file_path])    #mac/linx
        except Exception as e:
            print(f"Could not open file automatically: {e}")


#creating a function to collect education details
def get_education_details():
    education_list = []

    print("\nEnter Education Details:\n")
    #taking input details

    while True:
        qualification = input("Enter qualification/course (example: 10th, Inter, Diploma, B.Tech, M.Tech):\n")
        institution = input("Enter school/college/university name:\n")
        year = input("Enter year of completion:\n")
        percentage = input("Enter percentage:\n")

# Store details in dictionary
        education = {
            "qualification": qualification,
            "institution": institution,
            "year": year,
            "percentage": percentage
        }

        education_list.append(education)

        choice = input("\nDo you want to add another education? (yes/no):\n").lower()

        if choice != "yes":
            break

    return education_list


# Main function to run resume generator menu
def resume_generator():

    while True:
        print("\n-------------Resume menu--------------\n")
        print("1. Create Resume")
        print("2. View all Resumes")
        print("3. Search Resume by Name")
        print("4. Update Resume")
        print("5. Exit")

        choice = int(input("\nPlease select:\n"))

        if choice == 1:

               #--------------------------Input details-------------------------------

            while True:
                Name = input("Enter Your name:\n").capitalize()

                for ch in range(len(Name)):

                    if Name[ch] in "!@#$%^&*,":
                        print("\nInvalid name. Please enter a valid name without special characters.")
                        break

                    elif Name[ch].isdigit():
                        print("\nPlease enter only letters\n")
                        break

                else:
                    break

            while True:
                Age = int(input("\nEnter your Age:\n"))

                if Age <= 18 or Age >= 60:
                    print("\nThe user's age must be between 18 and 60\n")
                    continue
                else:
                    break

            while True:
                Phone_Number = input("\nEnter Your Phone Number:\n")

                if len(Phone_Number) != 10:
                    print("\nInvalid phone number. Please enter a valid 10 digit phone number\n")
                    continue

                for i in range(len(Phone_Number)):
                    if Phone_Number[i] < "0" or Phone_Number[i] > "9":
                        print("\nPlease enter only numbers\n")
                        break
                else:
                    break
            while True:
                Email = input("\nEnter Your Email ID:(without @gmail.com)\n") + "@gmail.com"

                for i in range(len(Email)):
                    if Email[i] == " ":
                        print("\nInvalid email.Please enter a valid email ID without spaces\n")
                        break

                    elif Email[i] == "@":
                        if Email[i - 1] == "." or Email[i + 1] == ".":
                            print("\nInvalid email ID. Please enter a valid email ID without '.' before or after '@'\n")
                            break

                    elif Email[i].isupper():
                        print("\nEmail should contain only small letters\n")
                        break

                    elif Email[i] in "!#$%^&*,":
                        print("\nEmail should not Contain any specail characters\n")
                        break

                else:
                    break

            while True:
                Address = input("\nEnter Your Address:\n").strip()

                if Address == "":
                    print("\nAddress cannot be empty\n")
                    continue

                break

            while True:
                Skills = list(input("\nEnter Your Skills (separated by commas):\n").split(", "))

                if Skills[0] == "":
                    print("\nPlease enter at least one skill\n")
                    continue

                else:
                    break

            while True:
                Languages = list(input("\nEnter Your Languages (separated by commas):\n").split(", "))

                if Languages[0] == "":
                    print("\nPlease enter at least one language\n")
                    continue

                else:
                    break

            while True:
                Hobbies = list(input("\nEnter Your Hobbies (separated by commas):\n").split(", "))

                if Hobbies[0] == "":
                    print("\nPlease enter at least one hobby\n")      
                    continue

                else:
                    break

            while True:
                Experience = int(input("\nEnter your Work Experience:\n"))

                if Experience < 0:
                    print("\nExperience cannot be negative\n")
                    continue
                else:
                    break

            Education = get_education_details()           #get education details

            resume = Resume(Name, Age, Phone_Number, Email, Address, Skills, Languages, Hobbies, Experience, Education)    #creating resume object

            resume.clear_resume()

            resume_list.append(resume)               #storing resume details

            print("\nResume Created Successfully\n")
  #generate word document
            resume.generate_docx()

        elif choice == 2:        #viewing all registered resumes
 
            if len(resume_list) == 0:
                print("No resume found\n")

            else:
                for i in resume_list:
                    print(i.resume_format())

        elif choice == 3:                      #searching for registered resume
            name = input("\nPlease enter your name:\n")

            found = False

            for i in resume_list:
                if i.Name == name:
                    print("\nResume Found\n")
                    print(i.resume_format())
                    found = True
                    break

            if found == False:
                print("\nResume not found\n")

        elif choice == 4:          #updating the fields


            name = input("Enter name to update:\n")
            found = False

            for r in resume_list:

                if r.Name == name:

                    found = True

                    field = input("What to update (Name/Age/Phone/Email/Address/Skills/Languages/Hobbies/Experience/Education):\n").strip().lower()

                    if field == "name":
                        new_name = input("Enter new name:\n")
                        r.update_resume(Name=new_name)

                    elif field == "age":
                        new_age = int(input("Enter new age:\n"))
                        r.update_resume(Age=new_age)

                    elif field == "phone":
                        new_phone = input("Enter new phone:\n")
                        r.update_resume(Phone_Number=new_phone)

                    elif field == "email":
                        new_mail = input("Enter new mail ID:\n")
                        r.update_resume(Email=new_mail)

                    elif field == "address":
                        new_address = input("Enter new Address:\n")
                        r.update_resume(Address=new_address)

                    elif field == "skills":
                        new_skills = input("Enter new Skills:\n")
                        r.update_resume(Skills=new_skills)

                    elif field == "languages":
                        new_languages = input("Enter new Languages:\n")
                        r.update_resume(Languages=new_languages)

                    elif field == "hobbies":
                        new_hobbies = input("Enter new Hobbies:\n")
                        r.update_resume(Hobbies=new_hobbies)

                    elif field == "education":
                        new_education = get_education_details()
                        r.update_resume(Education=new_education)

                    elif field == "experience":
                        new_experience = int(input("Enter Your Experience:\n"))
                        r.update_resume(Experience=new_experience)

                    else:
                        print("Invalid field")
                        break

                    print("\nResume Updated Successfully\n")

                    r.generate_docx()

                    break

            if found == False:
                print("Resume not found")

        elif choice == 5:
            print("\nExiting...\n")                   #exit option
            break

        else:
            print("\nInvalid Choice\n")
    


resume_generator()                  #calling the function 
