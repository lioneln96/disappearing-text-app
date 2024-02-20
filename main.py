import tkinter as tk
import threading
import time


def start_timer(text_area, timer_thread, timer_running):
    timer_running.set(True)
    for i in range(7, 0, -1):
        if not timer_running.get():
            return
        time.sleep(1)
    clear_text(text_area, timer_running)


def reset_timer(event, text_area, timer_thread, timer_running):
    if not timer_running.get():
        timer_thread = threading.Thread(target=start_timer, args=(text_area, timer_thread, timer_running))
        timer_thread.start()


def clear_text(text_area, timer_running):
    text_area.delete(1.0, tk.END)
    timer_running.set(False)


window = tk.Tk()
window.title("Most Dangerous Writing App")
window.geometry("800x600")
window.configure(bg="#000022")

input_frame = tk.Frame(window, bg="#000022")
input_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

text_font = ("Orbitron", 16)

text_area = tk.Text(input_frame, bg="#000022", fg="#FFFFFF", font=text_font, insertbackground="#FFFFFF", selectbackground="#4444FF", wrap=tk.WORD, height=5, width=40)  # White text on dark blue background, centered text
text_area.pack(expand=True, fill=tk.BOTH)

text_area.focus()

timer_thread = None
timer_running = False

window.bind("<Key>", reset_timer)

window.mainloop()


