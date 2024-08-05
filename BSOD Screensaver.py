import tkinter as tk
import random
import qrcode
from PIL import Image, ImageTk
from pynput import mouse, keyboard

# List of funny messages
messages = [
    "You've been working too much, time for a break, so I decided to break. Go grab some coffee whilst I'm having a dump of memory.",
    "Oops! Something went wrong... Just kidding, everything's fine. Take a deep breath.",
    "Error 404: Motivation not found. Please try again later.",
    "System overload! Too many tabs open. Time to close some and relax.",
    "Blue Screen of Relaxation: Take a moment to stretch and unwind.",
    "Your computer needs a nap. Please wait while it dreams of electric sheep.",
    "Time for a coffee break! Your computer will be back shortly.",
    "Oops! I did it again. Just kidding, everything's under control.",
    "Your computer is feeling blue. Give it a moment to recover.",
    "Taking a quick break to recharge. Be back soon!",
    "Your computer is on a coffee break. Please wait...",
    "Oops! Something went wrong. Don't worry, it's not your fault.",
    "Your computer is having a moment. Please be patient.",
    "Time to stretch! Your computer will be back shortly.",
    "Your computer is taking a quick nap. Please wait...",
    "Oops! Your computer needs a moment to catch its breath.",
    "Your computer is feeling a bit overwhelmed. Please wait...",
    "Time for a quick break! Your computer will be back soon.",
    "Your computer is taking a short break. Please be patient.",
    "Oops! Your computer needs a moment to relax.",
    "Your computer is on a quick coffee break. Please wait...",
    "Oops! Something went wrong. Please be patient.",
    "Your computer is taking a moment to unwind. Please wait...",
    "Time for a quick stretch! Your computer will be back shortly.",
    "Your computer is feeling a bit tired. Please wait...",
    "Oops! Your computer needs a moment to recover.",
    "Your computer is taking a short nap. Please wait...",
    "Time for a quick break! Your computer will be back soon.",
    "Your computer is feeling a bit blue. Please wait...",
    "Oops! Your computer needs a moment to catch its breath.",
    "Your computer is taking a quick coffee break. Please wait...",
    "Oops! Something went wrong. Please be patient.",
    "Your computer is taking a moment to relax. Please wait...",
    "Time for a quick stretch! Your computer will be back shortly.",
    "Your computer is feeling a bit overwhelmed. Please wait...",
    "Oops! Your computer needs a moment to recover.",
    "Your computer is taking a short break. Please wait...",
    "Time for a quick break! Your computer will be back soon.",
    "Your computer is feeling a bit tired. Please wait...",
    "Oops! Your computer needs a moment to unwind.",
    "Your computer is taking a quick nap. Please wait...",
    "Oops! Something went wrong. Please be patient.",
    "Your computer is taking a moment to catch its breath. Please wait...",
    "Time for a quick stretch! Your computer will be back shortly.",
    "Your computer is feeling a bit blue. Please wait...",
    "Oops! Your computer needs a moment to relax.",
    "Your computer is taking a quick coffee break. Please wait...",
    "Oops! Something went wrong. Please be patient.",
    "Your computer is taking a moment to unwind. Please wait...",
    "Time for a quick break! Your computer will be back soon.",
    "Your computer is feeling a bit overwhelmed. Please wait...",
    "Oops! Your computer needs a moment to recover.",
    "Your computer is taking a short nap. Please wait...",
    "Time for a quick stretch! Your computer will be back shortly.",
    "Your computer is feeling a bit tired. Please wait...",
    "Oops! Your computer needs a moment to catch its breath.",
    "Your computer is taking a quick coffee break. Please wait...",
    "Oops! Something went wrong. Please be patient.",
    "Your computer is taking a moment to relax. Please wait...",
    "Time for a quick break! Your computer will be back soon.",
    "Your computer is feeling a bit blue. Please wait...",
    "Oops! Your computer needs a moment to unwind.",
    "Your computer is taking a short break. Please wait...",
    "Time for a quick stretch! Your computer will be back shortly.",
    "Your computer is feeling a bit overwhelmed. Please wait...",
    "Oops! Your computer needs a moment to recover.",
    "Your computer is taking a quick nap. Please wait...",
    "Time for a quick break! Your computer will be back soon.",
    "Your computer is feeling a bit tired. Please wait...",
    "Oops! Your computer needs a moment to catch its breath.",
    "Your computer is taking a quick coffee break. Please wait...",
    "Oops! Something went wrong. Please be patient.",
    "Your computer is taking a moment to relax. Please wait...",
    "Time for a quick stretch! Your computer will be back shortly.",
    "Your computer is feeling a bit blue. Please wait...",
    "Oops! Your computer needs a moment to unwind.",
    "Your computer is taking a short break. Please wait...",
    "Time for a quick break! Your computer will be back soon.",
    "Your computer is feeling a bit overwhelmed. Please wait...",
    "Oops! Your computer needs a moment to recover.",
    "Your computer is taking a quick nap. Please wait...",
    "Time for a quick stretch! Your computer will be back shortly.",
    "Your computer is feeling a bit tired. Please wait...",
    "Oops! Your computer needs a moment to catch its breath.",
    "Your computer is taking a quick coffee break. Please wait...",
    "Oops! Something went wrong. Please be patient.",
    "Your computer is taking a moment to relax. Please wait..."
]

# Generate a QR code
def generate_qr_code(message):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Update the progress text
def update_progress():
    global progress
    if progress < 100:
        progress += 1
        progress_var.set(f"{progress}% complete")
        root.after(400, update_progress)  # Update progress every 100ms
    else:
        show_message()
        progress = 0
        progress_var.set(f"{progress}% complete")
        root.after(400, update_progress)

# Show a random message
def show_message():
    message = random.choice(messages)
    label_message.config(text=message)
    qr_img = generate_qr_code("https://www.google.co.uk/search?q=how+to+stop+working+too+much")
    qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_img)
    label_qr.config(image=qr_photo)
    label_qr.image = qr_photo

# Create the main window
root = tk.Tk()
root.title("BSOD Screensaver")
root.attributes('-fullscreen', True)
root.configure(bg='#0078D7')  # Windows 11 BSOD blue color

# Create a label to display the sad face emoji
label_emoji = tk.Label(root, text=":(", font=("Segoe UI", 288), fg="white", bg='#0078D7')
label_emoji.pack(side='top', anchor='w', padx=100, pady=10)

# Create a label to display the main message
label_main = tk.Label(root, text="Your device ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.", font=("Segoe UI", 24), fg="white", bg='#0078D7', wraplength=1200, justify="center")
label_main.pack(side='top', anchor='w', padx=100, pady=10)

# Create a label to display the progress text
progress = 0
progress_var = tk.StringVar()
progress_var.set(f"{progress}% complete")
label_progress = tk.Label(root, textvariable=progress_var, font=("Segoe UI", 24), fg="white", bg='#0078D7')
label_progress.pack(side='top', anchor='w', padx=100, pady=10)

# Create a label to display the funny message
label_message = tk.Label(root, text="", font=("Segoe UI", 20), fg="white", bg='#0078D7', wraplength=1200, justify="center")
label_message.pack(side='top', anchor='w', padx=100, pady=10)

# Create a label to display the QR code
label_qr = tk.Label(root, bg='#0078D7')
label_qr.pack(side='top', anchor='w', padx=100, pady=10)
show_message()

# Create a label to display the humorous message next to the QR code
qr_message_text = "For more information and helpful tips on how to avoid work search Google.com\nIn the meantime do not touch keybord or mouse to keep this screen on."
label_qr_message = tk.Label(root, text=qr_message_text, font=("Segoe UI", 14), fg="white", bg='#0078D7')
label_qr_message.pack(side='top', anchor='w', padx=100, pady=10)

# Function to quit the application
def quit_app(event=None, *args, **kwargs):
    root.destroy()

# Start updating progress
update_progress()

# Set up listeners for mouse and keyboard events
listener_mouse = mouse.Listener(on_click=quit_app)
listener_keyboard = keyboard.Listener(on_press=quit_app)

listener_mouse.start()
listener_keyboard.start()

root.mainloop()