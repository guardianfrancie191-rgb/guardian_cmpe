import tkinter as tk
from PIL import Image, ImageTk
import random
import winsound
import os

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Guess the System Unit Parts")
root.geometry("1100x950")

# ---------------- DATA ----------------
questions = [
    {"image": "images/cpu.png", "answer": "CPU"},
    {"image": "images/ram.png", "answer": "RAM"},
    {"image": "images/gpu.png", "answer": "GPU"},
    {"image": "images/motherboard.png", "answer": "Motherboard"},
    {"image": "images/powersupply.png", "answer": "Power Supply"},
    {"image": "images/cmos.png", "answer": "CMOS Battery"},
    {"image": "images/harddrive.png", "answer": "Hard Drive"},
    {"image": "images/fan.png", "answer": "Cooling Fan"},
    {"image": "images/soundcard.png", "answer": "Sound Card"},
    {"image": "images/heatsink.png", "answer": "Heatsink"},
]

choices = [
    "CPU", "RAM", "GPU", "Motherboard", "Power Supply",
    "CMOS Battery", "Hard Drive", "Cooling Fan",
    "Sound Card", "Heatsink"
]

random.shuffle(questions)

current_question = 0
score = 0
total_time = 300
timer_id = None

# ---------------- FUNCTIONS ----------------
def play_sound(file):
    if os.path.exists(file):
        winsound.PlaySound(file, winsound.SND_ASYNC)

def show_intro():
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(
        frame,
        text="GUESS THE SYSTEM UNIT PARTS by Francie Guardian BSECE 1-4",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        frame,
        text=(
            "Instructions:\n\n"
            "• You will see images of System Unit parts\n"
            "• Choose the correct answer\n"
            "• You have 5 minutes to finish the quiz\n"
            "• Total questions: 10\n\n"
            "Good luck!"
        ),
        font=("Arial", 18),
        justify="center"
    ).pack(pady=20)

    tk.Button(
        frame,
        text="START QUIZ",
        font=("Arial", 20, "bold"),
        width=15,
        command=start_quiz
    ).pack(pady=30)

def start_quiz():
    global score, current_question, total_time
    score = 0
    current_question = 0
    total_time = 300
    random.shuffle(questions)

    build_quiz_ui()
    load_question()
    update_timer()

def update_timer():
    global total_time, timer_id

    if total_time > 0:
        minutes = total_time // 60
        seconds = total_time % 60
        timer_label.config(text=f"Time Left: {minutes:02}:{seconds:02}")
        total_time -= 1
        timer_id = root.after(1000, update_timer)
    else:
        show_results()

def load_question():
    answer.set(None)
    result_label.config(text="")
    next_btn.config(state="disabled")

    img = Image.open(questions[current_question]["image"])
    img = img.resize((350, 350))
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

def check_answer():
    global score

    if answer.get() is None:
        return

    if answer.get() == questions[current_question]["answer"]:
        score += 1
        result_label.config(text="Correct!", fg="green")
        play_sound("sounds/correct.wav")
    else:
        result_label.config(
            text=f"Wrong! Answer: {questions[current_question]['answer']}",
            fg="red"
        )
        play_sound("sounds/wrong.wav")

    score_label.config(text=f"Score: {score} / {len(questions)}")
    next_btn.config(state="normal")

def next_question():
    global current_question

    current_question += 1
    if current_question >= len(questions):
        show_results()
    else:
        load_question()

def show_results():
    if timer_id:
        root.after_cancel(timer_id)

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="QUIZ FINISHED",
        font=("Arial", 36, "bold")
    ).pack(pady=30)

    tk.Label(
        root,
        text=f"Final Score: {score} / {len(questions)}",
        font=("Arial", 26)
    ).pack(pady=20)

    tk.Button(
        root,
        text="Play Again",
        font=("Arial", 18),
        command=show_intro
    ).pack(pady=10)

    tk.Button(
        root,
        text="Exit",
        font=("Arial", 18),
        command=root.quit
    ).pack(pady=10)

def build_quiz_ui():
    global timer_label, score_label, image_label
    global answer, result_label, next_btn

    for widget in root.winfo_children():
        widget.destroy()

    main_frame = tk.Frame(root)
    main_frame.pack(expand=True)

    timer_label = tk.Label(main_frame, font=("Arial", 22, "bold"))
    timer_label.pack(pady=5)

    score_label = tk.Label(
        main_frame,
        text=f"Score: {score} / {len(questions)}",
        font=("Arial", 18)
    )
    score_label.pack(pady=5)

    tk.Label(
        main_frame,
        text="What system unit part is this?",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    content = tk.Frame(main_frame)
    content.pack()

    image_label = tk.Label(content)
    image_label.grid(row=0, column=0, padx=50)

    choices_frame = tk.Frame(content)
    choices_frame.grid(row=0, column=1, sticky="w")

    answer = tk.StringVar(value=None)

    for c in choices:
        tk.Radiobutton(
            choices_frame,
            text=c,
            variable=answer,
            value=c,
            font=("Arial", 18)
        ).pack(anchor="w", pady=4)

    result_label = tk.Label(main_frame, font=("Arial", 20))
    result_label.pack(pady=10)

    btn_frame = tk.Frame(main_frame)
    btn_frame.pack(pady=20)

    tk.Button(
        btn_frame,
        text="SUBMIT",
        font=("Arial", 18, "bold"),
        width=10,
        command=check_answer
    ).pack(side="left", padx=20)

    next_btn = tk.Button(
        btn_frame,
        text="NEXT",
        font=("Arial", 18, "bold"),
        width=10,
        command=next_question,
        state="disabled"
    )
    next_btn.pack(side="left", padx=20)

# ---------------- START ----------------
show_intro()
root.mainloop()
