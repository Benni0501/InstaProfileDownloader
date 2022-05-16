import sys
import instaloader
import threading
import tkinter as tk
from tkinter import messagebox
import os
global entry


def getProfilePictureWorker():
    global entry
    username = entry.get()
    if(username == ""):
        messagebox.showerror("Error", "Es muss ein Benutzername angegeben werden!")
        button["state"] = "normal"
        entry["state"] = "normal"
    else:
        api = instaloader.Instaloader()
        print(username)
        try:
            api.download_profile(profile_name=username, profile_pic_only=True)
        except instaloader.exceptions.LoginRequiredException:
            messagebox.showerror("Error", "Benuzer wurde nicht gefunden!")
        except:
            messagebox.showerror("Error", "Ein Fehler ist aufgetreten!")
        else:
            messagebox.showinfo("Information", "Profil wurde heruntergeladen!")
        button["state"] = "normal"
        entry["state"] = "normal"

def getProfilePicture():
    entry["state"] = "disabled"
    button["state"] = "disabled"
    t = threading.Thread(target=getProfilePictureWorker)
    t.start()

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename


r = tk.Tk()
r.bind("<Return>", getProfilePicture)
r.geometry("300x70")
r.resizable(False, False)
r.title('Profilbild downloaden')
pathString = get_path('icon.ico')
r.iconbitmap(pathString)
entry = tk.Entry(width=50, justify=tk.CENTER)
button = tk.Button(r, text='Herunterladen', width=50, command=getProfilePicture)
exitButton = tk.Button(r, text='Beenden', width=50, command=r.destroy)
entry.focus()
entry.pack(expand=True)
button.pack(expand=True)
exitButton.pack(expand=True)

r.mainloop()
