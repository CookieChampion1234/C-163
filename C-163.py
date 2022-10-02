from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Fever Questions")
root.geometry("600x600")

question1_radioButton = StringVar(value="0")

Question1 = Label(root, text="Do you have an headche or sore throat?")
Question1.pack()
question_r1 = Radiobutton(root, text="yes", variable=question1_radioButton, value="yes")
question_r1.pack()
question_r2 = Radiobutton(root, text="no", variable=question1_radioButton, value="no")
question_r2.pack()

question2_radioButton = StringVar(value="0")

Question2 = Label(root, text="Is your body temperature high?")
Question2.pack()
question2_r1 = Radiobutton(root, text="yes", variable=question2_radioButton, value="yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text="no", variable=question2_radioButton, value="no")
question2_r2.pack()

question3_radioButton = StringVar(value="0")

Question3 = Label(root, text="Do you have any eye redness")
Question3.pack()
question3_r1 = Radiobutton(root, text="yes", variable=question3_radioButton, value="yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text="no", variable=question3_radioButton, value="no")
question3_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get() == "yes":
        score = score + 20
        print(score)
    if question2_radioButton.get() == "yes":
        score = score + 20
        print(score)
    if question3_radioButton.get() == "yes":
        score = score + 20
        print(score)

    if score <= 20:
        messagebox.showinfo("Report", "You do not need to visit a doctor")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report", "You may need to visit a doctor")
    else:
        messagebox.showinfo("Report", "I strongly advise you to go see a doctor")
btn = Button(root, text="click me", command = fever_score)
btn.pack()

root.mainloop()       

    
    
    
    