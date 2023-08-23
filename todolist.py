from tkinter import *

# import messagebox class from tkinter
from tkinter import messagebox

# global list is declare for storing all the task
tasks_list = []

# global variable is declare for counting the task
counter = 1


def inputError() :
	
	# check for enter task field is empty or not
	if enterTaskField.get() == "" :
		
		# show the error message
		messagebox.showerror("Input Error")
		
		return 0
	
	return 1


def clear_taskNumberField() :
	
	# clear the content of task number text field
	taskNumberField.delete(0.0, END)


def clear_taskField() :

	# clear the content of task field entry box
	enterTaskField.delete(0, END)
	

def insertTask():

	global counter
	
	# check for error
	value = inputError()

	# if error occur then return
	if value == 0 :
		return

	# get the task string concatenating
	# with new line character
	content = enterTaskField.get() + "\n"

	# store task in the list
	tasks_list.append(content)

	# insert content of task entry field to the text area
	# add task one by one in below one by one
	TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

	# incremented
	counter += 1

	# function calling for deleting the content of task field
	clear_taskField()

# function for deleting the specified task
def delete() :
	
	global counter
	
	# handling the empty task error
	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return

	# get the task number, which is required to delete
	number = taskNumberField.get(1.0, END)

	
	if number == "\n" :
		messagebox.showerror("input error")
		return
	
	else :
		task_no = int(number)

	
	clear_taskNumberField()
	
	# deleted specified task from the list
	tasks_list.pop(task_no - 1)

	# decremented
	counter -= 1
	
	# whole content of text area widget is deleted
	TextArea.delete(1.0, END)

	# rewriting the task after deleting one task at a time
	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
	

# Driver code
if __name__ == "__main__" :

	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background = "light pink")

	# set the title of GUI window
	gui.title("Todo GUI")

	# set the configuration of GUI window
	gui.geometry("250x300")

	# create a label : Enter Your Task
	enterTask = Label(gui, text = "Enter Your Task", bg = "light green")


	enterTaskField = Entry(gui)

	# create a Submit Button and place into the root window
	
	Submit = Button(gui, text = "Submit", fg = "Black", bg = "Red", command = insertTask)

	
	TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")

	# create a label : Delete Task Number
	taskNumber = Label(gui, text = "Delete Task Number", bg = "blue")
						
	taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")

	# create a Delete Button and place into the root window
	
	delete = Button(gui, text = "Delete", fg = "Black", bg = "yellow", command = delete)

	# create a Exit Button and place into the root window
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

	
	enterTask.grid(row = 0, column = 2)

				
	enterTaskField.grid(row = 1, column = 2, ipadx = 50)
						
	Submit.grid(row = 2, column = 2)
		
	
	TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
						
	taskNumber.grid(row = 4, column = 2, pady = 5)
						
	taskNumberField.grid(row = 5, column = 2)

			
	delete.grid(row = 6, column = 2, pady = 5)
						
	Exit.grid(row = 7, column = 2)

	
	gui.mainloop()

