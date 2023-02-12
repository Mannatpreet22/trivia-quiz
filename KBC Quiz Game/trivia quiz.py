<<<<<<< HEAD:KBC Quiz Game/trivia quiz.py
from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer
import random
from kbc_data import questions

folderLocation = "KBC Quiz Game/"
cheatMode = False

mixer.init()
mixer.music.load(folderLocation + "kbc.mp3")
mixer.music.play(-1)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def select(event):
    global questionNo

    mixer.music.set_volume(1)
    b = event.widget
    value = b["text"]
    resetButtons()
    if currentQuestion.check_answer(value):
        if questionNo == 14:

            def playagain():
                resetQuestions()
                root2.destroy()
                mixer.music.load(folderLocation + "kbc.mp3")
                mixer.music.play(-1)

            def on_closing():
                root2.destroy()
                root.destroy()

            mixer.music.stop()
            mixer.music.load(folderLocation + "Kbcwon.mp3")
            mixer.music.play()
            root2 = Toplevel()
            root2.overrideredirect(True)
            root2.grab_set()
            root2.config(bg="black")
            root2.geometry("500x400+140+30")
            root2.title("You won 1 million Pounds")
            centerimg = PhotoImage(file=folderLocation + "center.png")
            imgLabel = Label(
                root2,
                image=centerimg,
                bd=0,
            )
            imgLabel.pack(pady=30)

            winlabel = Label(
                root2,
                text="You Won",
                font=("arial", 40, "bold"),
                bg="black",
                fg="white",
            )
            winlabel.pack()

            happyimage = PhotoImage(file=folderLocation + "happy.png")
            happYLabel = Label(root2, image=happyimage, bg="black")
            happYLabel.place(x=400, y=280)

            happYLabel1 = Label(root2, image=happyimage, bg="black")
            happYLabel1.place(x=30, y=280)

            playagainButton = Button(
                root2,
                text="Play Again",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                cursor="hand2",
                activeforeground="white",
                command=playagain,
            )
            playagainButton.pack()

            closeButton = Button(
                root2,
                text="Close",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                cursor="hand2",
                activeforeground="white",
                command=on_closing,
            )
            closeButton.pack()

            root2.protocol("WM_DELETE_WINDOW", on_closing)
            root2.mainloop()

        changeQuestion()
        questionNo += 1
        amountlabel.config(image=images[questionNo])
    else:
        lose()


def lose():
    def tryagain():
        mixer.music.load(folderLocation + "kbc.mp3")
        mixer.music.play(-1)
        resetQuestions()
        root1.destroy()

    def on_closing():
        root1.destroy()
        root.destroy()

    mixer.music.stop()
    root1 = Toplevel()
    root1.overrideredirect(True)
    root1.grab_set()
    root1.config(bg="black")
    root1.geometry("500x400+140+30")
    root1.title("You won 0 Pound")
    img = PhotoImage(file=folderLocation + "center.png")
    imgLabel = Label(root1, image=img, bd=0)
    imgLabel.pack(pady=30)
    loselabel = Label(
        root1,
        text="You Lose",
        font=("arial", 40, "bold"),
        bg="black",
        fg="white",
    )
    loselabel.pack()
    sadimage = PhotoImage(file=folderLocation + "sad.png")
    sadlabel = Label(root1, image=sadimage, bg="black")
    sadlabel.place(x=400, y=280)
    sadlabel1 = Label(root1, image=sadimage, bg="black")
    sadlabel1.place(x=30, y=280)

    tryagainButton = Button(
        root1,
        text="Try Again",
        font=("arial", 20, "bold"),
        bg="black",
        fg="white",
        bd=0,
        activebackground="black",
        cursor="hand2",
        activeforeground="white",
        command=tryagain,
    )
    tryagainButton.pack()

    closeButton = Button(
        root1,
        text="Close",
        font=("arial", 20, "bold"),
        bg="black",
        fg="white",
        bd=0,
        activebackground="black",
        cursor="hand2",
        activeforeground="white",
        command=on_closing,
    )
    closeButton.pack()

    root1.protocol("WM_DELETE_WINDOW", on_closing)
    root1.mainloop()


def resetQuestions():
    global questionsDone, questionNo
    questionsDone = []
    questionNo = 0
    flipLifelineButton.config(state=NORMAL, image=flipImage)
    lifeline50Button.config(state=NORMAL, image=image50)
    # audiencePoleButton.config(state=NORMAL, image=audiencePole)
    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
    amountlabel.config(image=images[questionNo])
    changeQuestion()


def resetButtons():
    callButton.config(image="")

    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()


def changeQuestion():
    q = -1
    t = 0
    while q == -1 or q in questionsDone:
        q = random.randint(0, len(questions) - 1)
        t += 1
        if t > 1000:
            print("Out of Questions!")
            resetButtons()
            lose()
            return

    global currentQuestion
    currentQuestion = questions[q]
    questionsDone.append(q)
    questionData = currentQuestion.get_data()
    questionArea.delete(1.0, END)
    questionArea.insert(END, questionData["question"])
    optionButton1.config(text=questionData["options"][0])
    optionButton2.config(text=questionData["options"][1])
    optionButton3.config(text=questionData["options"][2])
    optionButton4.config(text=questionData["options"][3])


def lifeline50():
    if not cheatMode:
        lifeline50Button.config(image=image50x)
        lifeline50Button.config(state=DISABLED)

    questionData = currentQuestion.get_data()
    q = -1
    if questionData["correct_option"] == questionData["options"][0]:
        q = 0
    elif questionData["correct_option"] == questionData["options"][1]:
        q = 1
    elif questionData["correct_option"] == questionData["options"][2]:
        q = 2
    elif questionData["correct_option"] == questionData["options"][3]:
        q = 3
    else:
        print("Life-Line 50-50 did not find the Question.")

    r = -1
    while r == -1 or r == q:
        r = random.randint(0, 3)

    if r != 0 and q != 0:
        optionButton1.config(text="")
    if r != 1 and q != 1:
        optionButton2.config(text="")
    if r != 2 and q != 2:
        optionButton3.config(text="")
    if r != 3 and q != 3:
        optionButton4.config(text="")


# def audiencePoleLifeline():
#     if not cheatMode:
#         audiencePoleButton.config(image=audiencePolex)
#         audiencePoleButton.config(state=DISABLED)

#     progressbarA.place(x=580, y=190)
#     progressbarLabelA.place(x=580, y=320)

#     progressbarB.place(x=620, y=190)
#     progressbarLabelB.place(x=620, y=320)

#     progressbarC.place(x=660, y=190)
#     progressbarLabelC.place(x=660, y=320)

#     progressbarD.place(x=700, y=190)
#     progressbarLabelD.place(x=700, y=320)

#     questionData = currentQuestion.get_data()
#     q = -1
#     if questionData["correct_option"] == questionData["options"][0]:
#         q = 1
#     elif questionData["correct_option"] == questionData["options"][1]:
#         q = 2
#     elif questionData["correct_option"] == questionData["options"][2]:
#         q = 3
#     elif questionData["correct_option"] == questionData["options"][3]:
#         q = 4
#     else:
#         print("Life-Line 50-50 did not find the Question.")

#     r = random.randint(80, 95)

#     r1 = random.randint(20, 70)
#     r2 = random.randint(20, 70)
#     r3 = random.randint(20, 70)
#     r4 = random.randint(20, 70)

#     if q != 1:
#         progressbarA.config(value=r1)
#     else:
#         progressbarA.config(value=r)
#     if q != 2:
#         progressbarB.config(value=r2)
#     else:
#         progressbarB.config(value=r)
#     if q != 3:
#         progressbarC.config(value=r3)
#     else:
#         progressbarC.config(value=r)
#     if q != 4:
#         progressbarD.config(value=r4)
#     else:
#         progressbarD.config(value=r)


def flipLifeline():
    if not cheatMode:
        flipLifelineButton.config(image=flipImageX, state=DISABLED)
    changeQuestion()


def phoneLifeline():
    mixer.music.stop()
    mixer.music.load(folderLocation + "calling.mp3")
    mixer.music.play()

    if not cheatMode:
        phoneLifelineButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)


def phoneclick():
    mixer.music.load(folderLocation + "kbc.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    answer = "The Answer is " + currentQuestion.get_data()["correct_option"]
    print(answer)
    engine.say(answer)
    engine.runAndWait()


root = Tk()
root.geometry("1270x652+0+0")
root.resizable(0, 0)
root.title("TRIVIA QUIZ")
root.config(bg="black")

leftFrame = Frame(root, bg="black", padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg="black", padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg="black", pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg="black", pady=15)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg="black")
bottomFrame.grid(row=2, column=0)

centreImage = PhotoImage(file=folderLocation + "center.png")
logoLabel = Label(
    middleFrame, image=centreImage, bd=0, width=300, height=200, bg="black"
)
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file=folderLocation + "50-50.png")
image50x = PhotoImage(file=folderLocation + "50-50-X.png")
lifeline50Button = Button(
    topFrame,
    image=image50,
    bd=0,
    bg="black",
    cursor="hand2",
    activebackground="black",
    width=180,
    height=80,
    command=lifeline50,
)
lifeline50Button.grid(row=0, column=0)

# audiencePole = PhotoImage(file=folderLocation + "audiencePole.png")
# audiencePolex = PhotoImage(file=folderLocation + "audiencePoleX.png")
# audiencePoleButton = Button(
#     topFrame,
#     image=audiencePole,
#     bd=0,
#     bg="black",
#     cursor="hand2",
#     activebackground="black",
#     width=180,
#     height=80,
#     command=audiencePoleLifeline,
# )
# audiencePoleButton.grid(row=0, column=1)

flipImage = PhotoImage(file=folderLocation + "flip the question.png")
flipImageX = PhotoImage(file=folderLocation + "flip the question x.png")
flipLifelineButton = Button(
    topFrame,
    image=flipImage,
    bd=0,
    bg="black",
    cursor="hand2",
    activebackground="black",
    width=180,
    height=80,
    command=flipLifeline,
)
flipLifelineButton.grid(row=0, column=1)


phoneImage = PhotoImage(file=folderLocation + "phoneAFriend.png")
phoneImageX = PhotoImage(file=folderLocation + "phoneAFriendX.png")
phoneLifelineButton = Button(
    topFrame,
    image=phoneImage,
    bd=0,
    bg="black",
    cursor="hand2",
    activebackground="black",
    width=180,
    height=80,
    command=phoneLifeline,
)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(file=folderLocation + "phone.png")
callButton = Button(
    root, bg="black", bd=0, activebackground="black", cursor="hand2", command=phoneclick
)
callButton.place(x=70, y=260)

images = [
    PhotoImage(file=folderLocation + "Picture0.png"),
    PhotoImage(file=folderLocation + "Picture1.png"),
    PhotoImage(file=folderLocation + "Picture2.png"),
    PhotoImage(file=folderLocation + "Picture3.png"),
    PhotoImage(file=folderLocation + "Picture4.png"),
    PhotoImage(file=folderLocation + "Picture5.png"),
    PhotoImage(file=folderLocation + "Picture6.png"),
    PhotoImage(file=folderLocation + "Picture7.png"),
    PhotoImage(file=folderLocation + "Picture8.png"),
    PhotoImage(file=folderLocation + "Picture9.png"),
    PhotoImage(file=folderLocation + "Picture10.png"),
    PhotoImage(file=folderLocation + "Picture11.png"),
    PhotoImage(file=folderLocation + "Picture12.png"),
    PhotoImage(file=folderLocation + "Picture13.png"),
    PhotoImage(file=folderLocation + "Picture14.png"),
    PhotoImage(file=folderLocation + "Picture15.png"),
]

amountlabel = Label(rightFrame, image=images[0], bg="black", bd=0)
amountlabel.grid(row=0, column=0)

layoutimage = PhotoImage(file=folderLocation + "lay.png")
layoutlabel = Label(bottomFrame, image=layoutimage, bg="black", bd=0)
layoutlabel.grid(row=0, column=0)

questionArea = Text(
    bottomFrame,
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    width=34,
    height=2,
    wrap="word",
    bd=0,
)
questionArea.place(x=70, y=10)

labelA = Label(
    bottomFrame, font=("arial", 16, "bold"), text="A:", bg="black", fg="white"
)
labelA.place(x=60, y=110)

optionButton1 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton1.place(x=100, y=100)

labelB = Label(
    bottomFrame, font=("arial", 16, "bold"), text="B:", bg="black", fg="white"
)
labelB.place(x=330, y=110)

optionButton2 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton2.place(x=370, y=100)

labelC = Label(
    bottomFrame, font=("arial", 16, "bold"), text="C:", bg="black", fg="white"
)
labelC.place(x=60, y=190)

optionButton3 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton3.place(x=100, y=180)

labelD = Label(
    bottomFrame, font=("arial", 16, "bold"), text="D:", bg="black", fg="white"
)
labelD.place(x=330, y=190)

optionButton4 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelA = Label(
    root, text="A", font=("arial", 20, "bold"), bg="black", fg="white"
)

progressbarB = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelB = Label(
    root, text="B", font=("arial", 20, "bold"), bg="black", fg="white"
)

progressbarC = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelC = Label(
    root, text="C", font=("arial", 20, "bold"), bg="black", fg="white"
)

progressbarD = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelD = Label(
    root, text="D", font=("arial", 20, "bold"), bg="black", fg="white"
)

optionButton1.bind("<Button-1>", select)
optionButton2.bind("<Button-1>", select)
optionButton3.bind("<Button-1>", select)
optionButton4.bind("<Button-1>", select)

resetQuestions()

root.mainloop()
=======
from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer
import random
from kbc_data import questions

folderLocation = "KBC Quiz Game/"
cheatMode = True

mixer.init()
mixer.music.load(folderLocation + "kbc.mp3")
mixer.music.play(-1)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def select(event):
    global questionNo

    mixer.music.set_volume(1)
    b = event.widget
    value = b["text"]
    resetButtons()
    if currentQuestion.check_answer(value):
        if questionNo == 14:

            def playagain():
                resetQuestions()
                root2.destroy()
                mixer.music.load(folderLocation + "kbc.mp3")
                mixer.music.play(-1)

            def on_closing():
                root2.destroy()
                root.destroy()

            mixer.music.stop()
            mixer.music.load(folderLocation + "Kbcwon.mp3")
            mixer.music.play()
            root2 = Toplevel()
            root2.overrideredirect(True)
            root2.grab_set()
            root2.config(bg="black")
            root2.geometry("500x400+140+30")
            root2.title("You won 1 million Pounds")
            centerimg = PhotoImage(file=folderLocation + "center.png")
            imgLabel = Label(
                root2,
                image=centerimg,
                bd=0,
            )
            imgLabel.pack(pady=30)

            winlabel = Label(
                root2,
                text="You Won",
                font=("arial", 40, "bold"),
                bg="black",
                fg="white",
            )
            winlabel.pack()

            happyimage = PhotoImage(file=folderLocation + "happy.png")
            happYLabel = Label(root2, image=happyimage, bg="black")
            happYLabel.place(x=400, y=280)

            happYLabel1 = Label(root2, image=happyimage, bg="black")
            happYLabel1.place(x=30, y=280)

            playagainButton = Button(
                root2,
                text="Play Again",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                cursor="hand2",
                activeforeground="white",
                command=playagain,
            )
            playagainButton.pack()

            closeButton = Button(
                root2,
                text="Close",
                font=("arial", 20, "bold"),
                bg="black",
                fg="white",
                bd=0,
                activebackground="black",
                cursor="hand2",
                activeforeground="white",
                command=on_closing,
            )
            closeButton.pack()

            root2.protocol("WM_DELETE_WINDOW", on_closing)
            root2.mainloop()

        changeQuestion()
        questionNo += 1
        amountlabel.config(image=images[questionNo])
    else:
        lose()


def lose():
    def tryagain():
        mixer.music.load(folderLocation + "kbc.mp3")
        mixer.music.play(-1)
        resetQuestions()
        root1.destroy()

    def on_closing():
        root1.destroy()
        root.destroy()

    mixer.music.stop()
    root1 = Toplevel()
    root1.overrideredirect(True)
    root1.grab_set()
    root1.config(bg="black")
    root1.geometry("500x400+140+30")
    root1.title("You won 0 Pound")
    img = PhotoImage(file=folderLocation + "center.png")
    imgLabel = Label(root1, image=img, bd=0)
    imgLabel.pack(pady=30)
    loselabel = Label(
        root1,
        text="You Lose",
        font=("arial", 40, "bold"),
        bg="black",
        fg="white",
    )
    loselabel.pack()
    sadimage = PhotoImage(file=folderLocation + "sad.png")
    sadlabel = Label(root1, image=sadimage, bg="black")
    sadlabel.place(x=400, y=280)
    sadlabel1 = Label(root1, image=sadimage, bg="black")
    sadlabel1.place(x=30, y=280)

    tryagainButton = Button(
        root1,
        text="Try Again",
        font=("arial", 20, "bold"),
        bg="black",
        fg="white",
        bd=0,
        activebackground="black",
        cursor="hand2",
        activeforeground="white",
        command=tryagain,
    )
    tryagainButton.pack()

    closeButton = Button(
        root1,
        text="Close",
        font=("arial", 20, "bold"),
        bg="black",
        fg="white",
        bd=0,
        activebackground="black",
        cursor="hand2",
        activeforeground="white",
        command=on_closing,
    )
    closeButton.pack()

    root1.protocol("WM_DELETE_WINDOW", on_closing)
    root1.mainloop()


def resetQuestions():
    global questionsDone, questionNo
    questionsDone = []
    questionNo = 0
    flipLifelineButton.config(state=NORMAL, image=flipImage)
    lifeline50Button.config(state=NORMAL, image=image50)
    # audiencePoleButton.config(state=NORMAL, image=audiencePole)
    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
    amountlabel.config(image=images[questionNo])
    changeQuestion()


def resetButtons():
    callButton.config(image="")

    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()


def changeQuestion():
    q = -1
    t = 0
    while q == -1 or q in questionsDone:
        q = random.randint(0, len(questions) - 1)
        t += 1
        if t > 1000:
            print("Out of Questions!")
            resetButtons()
            lose()
            return

    global currentQuestion
    currentQuestion = questions[q]
    questionsDone.append(q)
    questionData = currentQuestion.get_data()
    questionArea.delete(1.0, END)
    questionArea.insert(END, questionData["question"])
    optionButton1.config(text=questionData["options"][0])
    optionButton2.config(text=questionData["options"][1])
    optionButton3.config(text=questionData["options"][2])
    optionButton4.config(text=questionData["options"][3])


def lifeline50():
    if not cheatMode:
        lifeline50Button.config(image=image50x)
        lifeline50Button.config(state=DISABLED)

    questionData = currentQuestion.get_data()
    q = -1
    if questionData["correct_option"] == questionData["options"][0]:
        q = 0
    elif questionData["correct_option"] == questionData["options"][1]:
        q = 1
    elif questionData["correct_option"] == questionData["options"][2]:
        q = 2
    elif questionData["correct_option"] == questionData["options"][3]:
        q = 3
    else:
        print("Life-Line 50-50 did not find the Question.")

    r = -1
    while r == -1 or r == q:
        r = random.randint(0, 3)

    if r != 0 and q != 0:
        optionButton1.config(text="")
    if r != 1 and q != 1:
        optionButton2.config(text="")
    if r != 2 and q != 2:
        optionButton3.config(text="")
    if r != 3 and q != 3:
        optionButton4.config(text="")


# def audiencePoleLifeline():
#     if not cheatMode:
#         audiencePoleButton.config(image=audiencePolex)
#         audiencePoleButton.config(state=DISABLED)

#     progressbarA.place(x=580, y=190)
#     progressbarLabelA.place(x=580, y=320)

#     progressbarB.place(x=620, y=190)
#     progressbarLabelB.place(x=620, y=320)

#     progressbarC.place(x=660, y=190)
#     progressbarLabelC.place(x=660, y=320)

#     progressbarD.place(x=700, y=190)
#     progressbarLabelD.place(x=700, y=320)

#     questionData = currentQuestion.get_data()
#     q = -1
#     if questionData["correct_option"] == questionData["options"][0]:
#         q = 1
#     elif questionData["correct_option"] == questionData["options"][1]:
#         q = 2
#     elif questionData["correct_option"] == questionData["options"][2]:
#         q = 3
#     elif questionData["correct_option"] == questionData["options"][3]:
#         q = 4
#     else:
#         print("Life-Line 50-50 did not find the Question.")

#     r = random.randint(80, 95)

#     r1 = random.randint(20, 70)
#     r2 = random.randint(20, 70)
#     r3 = random.randint(20, 70)
#     r4 = random.randint(20, 70)

#     if q != 1:
#         progressbarA.config(value=r1)
#     else:
#         progressbarA.config(value=r)
#     if q != 2:
#         progressbarB.config(value=r2)
#     else:
#         progressbarB.config(value=r)
#     if q != 3:
#         progressbarC.config(value=r3)
#     else:
#         progressbarC.config(value=r)
#     if q != 4:
#         progressbarD.config(value=r4)
#     else:
#         progressbarD.config(value=r)


def flipLifeline():
    if not cheatMode:
        flipLifelineButton.config(image=flipImageX, state=DISABLED)
    changeQuestion()


def phoneLifeline():
    mixer.music.stop()
    mixer.music.load(folderLocation + "calling.mp3")
    mixer.music.play()

    if not cheatMode:
        phoneLifelineButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)


def phoneclick():
    mixer.music.load(folderLocation + "kbc.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    answer = "The Answer is " + currentQuestion.get_data()["correct_option"]
    print(answer)
    engine.say(answer)
    engine.runAndWait()


root = Tk()
root.geometry("1270x652+0+0")
root.resizable(0, 0)
root.title("TRIVIA QUIZ")
root.config(bg="black")

leftFrame = Frame(root, bg="black", padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg="black", padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg="black", pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg="black", pady=15)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg="black")
bottomFrame.grid(row=2, column=0)

centreImage = PhotoImage(file=folderLocation + "center.png")
logoLabel = Label(
    middleFrame, image=centreImage, bd=0, width=300, height=200, bg="black"
)
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file=folderLocation + "50-50.png")
image50x = PhotoImage(file=folderLocation + "50-50-X.png")
lifeline50Button = Button(
    topFrame,
    image=image50,
    bd=0,
    bg="black",
    cursor="hand2",
    activebackground="black",
    width=180,
    height=80,
    command=lifeline50,
)
lifeline50Button.grid(row=0, column=0)

# audiencePole = PhotoImage(file=folderLocation + "audiencePole.png")
# audiencePolex = PhotoImage(file=folderLocation + "audiencePoleX.png")
# audiencePoleButton = Button(
#     topFrame,
#     image=audiencePole,
#     bd=0,
#     bg="black",
#     cursor="hand2",
#     activebackground="black",
#     width=180,
#     height=80,
#     command=audiencePoleLifeline,
# )
# audiencePoleButton.grid(row=0, column=1)

flipImage = PhotoImage(file=folderLocation + "flip the question.png")
flipImageX = PhotoImage(file=folderLocation + "flip the question x.png")
flipLifelineButton = Button(
    topFrame,
    image=flipImage,
    bd=0,
    bg="black",
    cursor="hand2",
    activebackground="black",
    width=180,
    height=80,
    command=flipLifeline,
)
flipLifelineButton.grid(row=0, column=1)


phoneImage = PhotoImage(file=folderLocation + "phoneAFriend.png")
phoneImageX = PhotoImage(file=folderLocation + "phoneAFriendX.png")
phoneLifelineButton = Button(
    topFrame,
    image=phoneImage,
    bd=0,
    bg="black",
    cursor="hand2",
    activebackground="black",
    width=180,
    height=80,
    command=phoneLifeline,
)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(file=folderLocation + "phone.png")
callButton = Button(
    root, bg="black", bd=0, activebackground="black", cursor="hand2", command=phoneclick
)
callButton.place(x=70, y=260)

images = [
    PhotoImage(file=folderLocation + "Picture0.png"),
    PhotoImage(file=folderLocation + "Picture1.png"),
    PhotoImage(file=folderLocation + "Picture2.png"),
    PhotoImage(file=folderLocation + "Picture3.png"),
    PhotoImage(file=folderLocation + "Picture4.png"),
    PhotoImage(file=folderLocation + "Picture5.png"),
    PhotoImage(file=folderLocation + "Picture6.png"),
    PhotoImage(file=folderLocation + "Picture7.png"),
    PhotoImage(file=folderLocation + "Picture8.png"),
    PhotoImage(file=folderLocation + "Picture9.png"),
    PhotoImage(file=folderLocation + "Picture10.png"),
    PhotoImage(file=folderLocation + "Picture11.png"),
    PhotoImage(file=folderLocation + "Picture12.png"),
    PhotoImage(file=folderLocation + "Picture13.png"),
    PhotoImage(file=folderLocation + "Picture14.png"),
    PhotoImage(file=folderLocation + "Picture15.png"),
]

amountlabel = Label(rightFrame, image=images[0], bg="black", bd=0)
amountlabel.grid(row=0, column=0)

layoutimage = PhotoImage(file=folderLocation + "lay.png")
layoutlabel = Label(bottomFrame, image=layoutimage, bg="black", bd=0)
layoutlabel.grid(row=0, column=0)

questionArea = Text(
    bottomFrame,
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    width=34,
    height=2,
    wrap="word",
    bd=0,
)
questionArea.place(x=70, y=10)

labelA = Label(
    bottomFrame, font=("arial", 16, "bold"), text="A:", bg="black", fg="white"
)
labelA.place(x=60, y=110)

optionButton1 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton1.place(x=100, y=100)

labelB = Label(
    bottomFrame, font=("arial", 16, "bold"), text="B:", bg="black", fg="white"
)
labelB.place(x=330, y=110)

optionButton2 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton2.place(x=370, y=100)

labelC = Label(
    bottomFrame, font=("arial", 16, "bold"), text="C:", bg="black", fg="white"
)
labelC.place(x=60, y=190)

optionButton3 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton3.place(x=100, y=180)

labelD = Label(
    bottomFrame, font=("arial", 16, "bold"), text="D:", bg="black", fg="white"
)
labelD.place(x=330, y=190)

optionButton4 = Button(
    bottomFrame,
    text="",
    font=("arial", 18, "bold"),
    bg="black",
    fg="white",
    cursor="hand2",
    bd=0,
    activebackground="black",
    activeforeground="white",
)
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelA = Label(
    root, text="A", font=("arial", 20, "bold"), bg="black", fg="white"
)

progressbarB = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelB = Label(
    root, text="B", font=("arial", 20, "bold"), bg="black", fg="white"
)

progressbarC = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelC = Label(
    root, text="C", font=("arial", 20, "bold"), bg="black", fg="white"
)

progressbarD = Progressbar(root, orient=VERTICAL, mode="determinate", length=120)
progressbarLabelD = Label(
    root, text="D", font=("arial", 20, "bold"), bg="black", fg="white"
)

optionButton1.bind("<Button-1>", select)
optionButton2.bind("<Button-1>", select)
optionButton3.bind("<Button-1>", select)
optionButton4.bind("<Button-1>", select)

resetQuestions()

root.mainloop()
>>>>>>> 559e058cf8387bbcd3d736fed70a186287805f14:KBC Quiz Game/kbc_lokesh.py
