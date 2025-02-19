import pyqrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Initialize the main window
window = Tk()
window.geometry('300x400')
window.title('QR Code Generator')

qr_file_name = 'qrcode.png'

def display_qrcode(image_path):
    img = Image.open(image_path)
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    
    img_label.config(image=img)
    img_label.image = img

def create_qrcode():
    qr_content = qr_input.get()
    qr = pyqrcode.create(qr_content)
    qr.png(qr_file_name, scale=6)
    
    display_qrcode(qr_file_name)
    
    # Show the download button
    download_button.pack()

def download_qrcode():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_image = Image.open(qr_file_name)
        qr_image.save(file_path)
        Label(window, text='QR Code saved successfully').pack()

# Input field for QR code content
qr_input = StringVar()
Label(window, text='Let’s Create QR Code', font='arial 15').pack()
Entry(window, textvariable=qr_input, font='arial 15').pack()

# Label to display the QR code
img_label = Label(window)
img_label.pack()

# Button to create QR code
Button(window, text='Create', bg='lightgreen', command=create_qrcode).pack()

# Button to download QR code
download_button = Button(window, text='Download', bg='lightblue', command=download_qrcode)
download_button.pack()
download_button.pack_forget()

# Start the main loop
window.mainloop()