from ast import Lambda
from cProfile import label
from logging import root
from sys import dont_write_bytecode
import time
import tkinter
from pytubefix import YouTube
from tkinter import *
from tkinter import ttk
import os


def DownloadYTVid(url, res, root):
    downloading_label = tkinter.Label(root, text="Downloading...")
    downloading_label.place(x=100, y=150)  # Now place it after creating the label
    
    def remove_label():
        downloading_label.destroy()  # Function to destroy label after download
    try:
        
        yt = YouTube(url).streams.first().download(output_path="YT_Downloads")
        root.after(1000, remove_label)
        
    except Exception as e:
        print(f"Please try again, may have been invalid URL.  ERROR : {e}")

def OpenFolder(path):
    os.startfile(path)
     
def main():
    root = Tk()  # create a root widget
    root.title("Download Helper")
    root.configure(background="white")
    root.minsize(300, 300)  # width, height
    root.maxsize(300, 300)
    root.geometry("300x300")  # width x height + x + y
    
    x = tkinter.Label(root, text="URL").grid(row=0, column=2)
    e1 = tkinter.Entry(root)
    e1.grid(row=0, column=4)
    
    tkinter.Button(root, 
          text='Download', 
          command=lambda: DownloadYTVid(e1.get(), 1, root)).grid(row=4, 
                                    column=2, 
                                    sticky=tkinter.W, 
                                    pady=4)
    
    print(e1.get())
    print(e1.get())
    tkinter.Button(root, 
          text='Open Folder', 
          command = lambda: OpenFolder("YT_Downloads")).grid(row=4, 
                                    column=3, 
                                    sticky=tkinter.W, 
                                    pady=4)

    root.mainloop()
    tkinter.mainloop()
    #DownloadYTVid("https://www.youtube.com/watch?v=1U2CPg42_OM", 1)


if __name__ == "__main__":
    main()