import tkinter as tk
import random
import qrcode
from PIL import Image, ImageTk
from pynput import mouse, keyboard
import sys
import ctypes

# List of funny messages
messages = [
    "You've been working too much, time for a break, so I decided to break. Go grab some coffee whilst I'm having a dump of memory.",
    "Oops! Something went wrong... Just kidding, everything's fine. Take a deep breath.",
    "Error 404: Motivation not found. Please try again later.",
    "System overload! Too many tabs open. Time to close some and relax.",
    "Blue Screen of Relaxation: Take a moment to stretch and unwind.",
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
    else:
        show_message()
        progress = 0
    progress_var.set(f"{progress}% complete")
    root.after(200, update_progress)

# Show a random message
def show_message():
    message = random.choice(messages)
    label_message.config(text=message)
    qr_img = generate_qr_code("https://www.google.co.uk/search?q=BSOD")
    qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_img)
    label_qr.config(image=qr_photo)
    label_qr.image = qr_photo

# Function to quit the application
def quit_app(event=None, *args, **kwargs):
    root.destroy()

# Function to handle screensaver arguments
def handle_arguments():
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == '/s':
            start_screensaver()
        elif sys.argv[1].lower() == '/c':
            configure_screensaver()
        elif sys.argv[1].lower() == '/p':
            preview_screensaver()
    else:
        start_screensaver()

# Function to start the screensaver
def start_screensaver():
    global root
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
    global progress
    progress = 0
    global progress_var
    progress_var = tk.StringVar()
    progress_var.set(f"{progress}% complete")
    label_progress = tk.Label(root, textvariable=progress_var, font=("Segoe UI", 24), fg="white", bg='#0078D7')
    label_progress.pack(side='top', anchor='w', padx=100, pady=10)

    # Create a label to display the funny message
    global label_message
    label_message = tk.Label(root, text="", font=("Segoe UI", 20), fg="white", bg='#0078D7', wraplength=1200, justify="center")
    label_message.pack(side='top', anchor='w', padx=100, pady=10)

    # Create a label to display the QR code
    global label_qr
    label_qr = tk.Label(root, bg='#0078D7')
    label_qr.pack(side='top', anchor='w', padx=100, pady=10)
    show_message()

    # Create a label to display the humorous message next to the QR code
    qr_message_text = "For more information and helpful tips scan this QR code."
    label_qr_message = tk.Label(root, text=qr_message_text, font=("Segoe UI", 14), fg="white", bg='#0078D7')
    label_qr_message.pack(side='top', anchor='w', padx=100, pady=10)

    # Start updating progress
    update_progress()

    # Set up listeners for mouse and keyboard events
    listener_mouse = mouse.Listener(on_click=quit_app)
    listener_keyboard = keyboard.Listener(on_press=quit_app)

    listener_mouse.start()
    listener_keyboard.start()

    root.mainloop()

# Function to configure the screensaver (optional)
def configure_screensaver():
    print("No configuration available.")

# Function to preview the screensaver (optional)
def preview_screensaver():
    print("Preview not implemented.")

# Function to make other monitors black
def make_other_monitors_black():
    user32 = ctypes.windll.user32
    screens = user32.GetSystemMetrics(80)
    for i in range(1, screens):
        hdc = user32.GetDC(None)
        user32.FillRect(hdc, ctypes.byref(ctypes.wintypes.RECT(0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))), 0)
        user32.ReleaseDC(None, hdc)

# Main function
if __name__ == "__main__":
    make_other_monitors_black()
    handle_arguments()