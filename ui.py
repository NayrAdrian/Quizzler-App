from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a score label and place it at the top
        self.score_label = Label(self.window, text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1, pady=20)

        # Create a canvas and place it below the score label
        self.canvas = Canvas(self.window, height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.question = self.canvas.create_text(150, 125, text="Sample", font=("Arial", 15, "italic"))

        # True/False Buttons
        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, highlightthickness=0, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=1)

        check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_image, highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0)

        self.window.mainloop()
