import os
import platform

studentList = ["Kenneth Soliva", "Cedric Ebanos", "Dash Adriano", "Jane Nilo", "Mike Hapin", "Mitra Virbe"]

## App Process Loop Regulator
def continueAgain():
	runningAgain = input("\nDo you want to continue the process? [yes/no]: ")
	if(runningAgain.lower() == 'yes'):
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		studentManagement()
		continueAgain()

	elif(runningAgain.lower() == 'no'):
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		print('Program terminated.') 
		quit()

	else: 
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		print('\nInvalid input. Answer only with yes or no.')
		continueAgain()

# App 
def studentManagement():
	print("\nWelcome to Phinma College Student Management System!\n")
	print("[Choice 1: Showing the List of Students]")
	print("[Choice 2: Adding a New Student to List]")
	print("[Choice 3: Searching a Student from List]")
	print("[Choice 4: Deleting a Student from List]")
	print("[Choice 5: Exit Program]\n")

	# Initial Input
	try:
		x = int(input("Enter a choice [1-5]: "))
	except ValueError:
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		print("\nInvalid input. Please only input a number.")
		continueAgain()
	else:
		print()

	# Input-based Logic
	if(x==1):
		print("Student List:\n")
		for students in studentList:
			print("{}".format(students))

	elif(x==2):
		studentNew = input("Enter new student's full name: ")
		if(studentNew in studentList):
			print("\nThe student, {}, is already in the list.".format(studentNew))
		else:
			studentList.append(studentNew)
			print("\n{} has been added to the list successfully.\n".format(studentNew))
			print("Updated Student List:\n")
			for students in studentList:
				print("{}".format(students))

	elif(x==3):
		studentSearching = input("Enter student's full name.\n[SEARCHING]: ")
		if(studentSearching in studentList):
			print("\nThe student, {}, is in the list.".format(studentSearching))
		else:
			print("\nThe student, {}, is not in the current program instance's list.".format(studentSearching))

	elif(x==4):
		studentDelete = input("Enter student full name.\n[DELETING]: ")
		if(studentDelete in studentList):
			studentList.remove(studentDelete)
			print("\nThe student, {}, has been removed from the student list.".format(studentDelete))
			print("\nUpdated Student List:\n")
			for students in studentList:
				print("{}".format(students))
		else:
			print("\nThe student, {}, is not in the list.".format(studentDelete))
	
	elif(x==5):
		print("\nProgram terminated.")
		quit()

	elif(x < 1 or x > 4):
		print("Please enter a valid choice.")

## Instantiation of Program
studentManagement()
continueAgain()
