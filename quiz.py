import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "Care este cel mai mare ocean din lume?",
     "options": ["Oceanul Atlantic", "Oceanul Indian", "Oceanul Pacific", "Oceanul Arctic"],
     "answer": "Oceanul Pacific"},
    {"question": "Care este capitala Franței?",
     "options": ["Londra", "Berlin", "Madrid", "Paris"],
     "answer": "Paris"},
    {"question": "Câte planete sunt în sistemul nostru solar?",
     "options": ["7", "8", "9", "10"],
     "answer": "8"},
    {"question": "Care este simbolul chimic pentru apă?",
     "options": ["H2O", "O2", "CO2", "HO"],
     "answer": "H2O"}
]

current_question = 0
score = 0
remaining_time = 15

def check_answer(selected_option):
    global current_question, score, remaining_time
    root.after_cancel(timer_id)

    if questions[current_question]["options"][selected_option] == questions[current_question]["answer"]:
        score += 1
        messagebox.showinfo("Răspuns Corect!", "Felicitări! Răspunsul este corect.")
    else:
        messagebox.showerror("Răspuns Greșit", f"Răspunsul corect era: {questions[current_question]['answer']}")

    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        show_score()

def load_question():
    global remaining_time
    question_label.config(text=questions[current_question]["question"])

    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option, state="normal")

    remaining_time = 15
    update_timer()

def show_score():
    question_label.config(text=f"Scorul tău final este: {score}/{len(questions)}")
    for button in option_buttons:
        button.config(state="disabled")
    timer_label.config(text="")

def update_timer():
    global remaining_time, timer_id

    if remaining_time > 0:
        timer_label.config(text=f"Timp rămas: {remaining_time} secunde")
        remaining_time -= 1
        timer_id = root.after(1000, update_timer)
    else:
        messagebox.showerror("Timp Expirat", f"Timpul s-a terminat! Răspunsul corect era: {questions[current_question]['answer']}")
        next_question()

def next_question():
    global current_question

    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        show_score()

root = tk.Tk()
root.title("Trivia Quiz")
root.geometry("400x300")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350, justify="center")
question_label.pack(pady=20)

timer_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
timer_label.pack(pady=5)

option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    option_buttons.append(button)

load_question()

timer_id = None

root.mainloop()