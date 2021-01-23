from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

	def __init__(self, quiz_brain: QuizBrain):
		self.quiz = quiz_brain

		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)

		# Labels
		self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
		self.score_label.grid(column=1, row=0)

		self.canvas = Canvas(width=300, height=250, bg="white")
		self.question_text = self.canvas.create_text(
			150, 
			125, 
			width=280,
			text="Some Question Text", 
			fill=THEME_COLOR,
			font=("Ariel", 20, "italic")
			)
		self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

		# Buttons
		check_image = PhotoImage(file="images/true.png")
		self.check_button = Button(image=check_image, highlightthickness=0)
		self.check_button.grid(column=0, row=2)

		cross_image = PhotoImage(file="images/false.png")
		self.cross_button = Button(image=cross_image)
		self.cross_button.grid(column=1, row=2)

		self.get_next_question()

		self.window.mainloop()

def get_next_question(self):
	q_text = self.quiz.next_question()
	self.canvas.itemconfig(self.question_text, text=q_text)


