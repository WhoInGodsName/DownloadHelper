import tkinter
from pytubefix import YouTube
from tkinter import *
from tkinter import ttk

def DownloadYTVid(url, res):
    try:
        YouTube("https://www.youtube.com/watch?v=1U2CPg42_OM").streams.first().download(output_path="YT_Downloads")
    except Exception as e:
        print(f"Please try again, may have been invalid URL.  ERROR : {e}")
     
def main():
    root = Tk()  # create a root widget
    root.title("Download Helper")
    root.configure(background="white")
    root.minsize(300, 300)  # width, height
    root.maxsize(300, 300)
    root.geometry("300x300")  # width x height + x + y
    
    tkinter.Label(root, text="URL").grid(row=0, column=2)
    e1 = tkinter.Entry(root)
    e1.grid(row=0, column=4)
    
    tkinter.Button(root, 
          text='Download', 
          command=DownloadYTVid(e1.get(), 1)).grid(row=4, 
                                    column=2, 
                                    sticky=tkinter.W, 
                                    pady=4)

    root.mainloop()
    DownloadYTVid("https://www.youtube.com/watch?v=1U2CPg42_OM", 1)


if __name__ == "__main__":
    main()