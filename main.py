import tkinter as tk
from tkinter import *

class Test:

    def __init__(self, nuymber):
        self.x = 5
        pass

    def clalc(self):
        self.x = self.x+4

class Question:

    def __init__(self, text, type, answers, correctAns):
        ###hEj
        self.text = text

class MultChoice(Question):
    def __init__(self, text, answer0, answer1, answer2, correctAns):

        self.text = text
        self.type = "MultChoice"
        self.answers = [answer0, answer1, answer2, correctAns]
        pass


def NextQuestion():
    global questionIndex
    print("Sigma")
    questionIndex += 1
    lb2.config(text = questions[questionIndex].text)
    answerB1.config(text=questions[questionIndex].answers[0])
    answerB2.config(text=questions[questionIndex].answers[1])
    answerB3.config(text=questions[questionIndex].answers[2])
    answerB4.config(text=questions[questionIndex].answers[3])

def BackQuestion():
    global questionIndex
    print("Ligma")
    if questionIndex - 1 != -1:
        questionIndex -= 1
    lb2.config(text = questions[questionIndex].text)
    answerB1.config(text = questions[questionIndex].answers[0])
    answerB2.config(text=questions[questionIndex].answers[1])
    answerB3.config(text=questions[questionIndex].answers[2])
    answerB4.config(text=questions[questionIndex].answers[3])



q1 = MultChoice("Vad av följande kan du inte programmera en dator till att göra?", "Visa bilder / videor", "Göra matematiska beräknignar", "Köra DOOM'93", "Ha riktiga känslor")
q2 = MultChoice("Vad betyder binärkod?", "Kod som är ooptimerad.", "Kod som är optimerad.", "Processorinstruktioner, text eller annan data som representeras av ett \nsextontalssystem, 1 - F.", "Processorinstruktioner, text eller annan data som representeras av ett tvåtalssytem, 1 och 0.")
q3 = MultChoice("Vad gör en kompilator?","En kompilator används för att överklocka en processor.", "Ett program som gör det lättare att lägga till olika språk i appar;\n det tar även mindre plats än andra metoder.", "En kompilator är vad kopplingarna mellan olika delar på moderkortet kallas.", "Ett program som översätter kod från ett programmeringsspråk till ett annat.\n Ex: Ett lättanvänt programmeringsspråk till ett lågnivåspråk som maskinkod.")



questions = [q1, q2, q3]
questionIndex = -1
true = 0

answerID = 0


root = tk.Tk()
root.title("Teknikprov")
root.geometry("1920x1080")
answerFrame = Frame(root)
questionsFrame = Frame(root)
arrowFrame = Frame(questionsFrame)

lb1 = Label(answerFrame, text="Teknikprov", font = ("Arial", 30), bg="#1aaeed", fg="white", width= 57)
lb2 = Label(answerFrame, text="Fråga 1: Vad dator är haha!?", font = ("Arial", 40))
lb3 = Label(questionsFrame, text="Fråga 1: Vad dator är haha!?", font = ("Arial", 25))
lb4 = Label(answerFrame, text = "Zkogs Inc.", font = ("Arial", 30), bg="#1aaeed", fg="white")

backButton = Button(arrowFrame, text="←", command=BackQuestion)
nextButton = Button(arrowFrame, text="→", command=NextQuestion)

answerB1 = Button(answerFrame, text = "Button 1")
answerB2 = Button(answerFrame, text = "Button 2")
answerB3 = Button(answerFrame, text = "Button 3")
answerB4 = Button(answerFrame, text = "Button 4")



root.columnconfigure(0,weight=4)
root.columnconfigure(1,weight=1)

answerFrame.grid(row=0, column=0)
questionsFrame.grid(row=0, column=1)
arrowFrame.grid(row=0, column=0)
nextButton.pack(side = "right", fill = "both", expand = True)
backButton.pack(side = "left", fill = "both", expand = True)

answerB1.grid(row=3, column=0)
answerB2.grid(row=3, column=1)
answerB3.grid(row=4, column=0)
answerB4.grid(row=4, column=1)


lb1.grid(row=0, column=0)
lb2.grid(row=1,column=0)

lb4.grid(row=0, column=1)

root.attributes('-fullscreen',True)

root.mainloop()


