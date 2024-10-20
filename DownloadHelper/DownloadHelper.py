import threading
import tkinter
from pytubefix import YouTube
from tkinter import *
import os

def DownloadYTVid(url, res, root, downloading_label):
    downloading_label.config(text="Downloading...")  # Update the label text

    def download_video():
        try:
            yt = YouTube(url).streams.filter(res=res).first().download(output_path="YT_Downloads")
            downloading_label.config(text="Download complete!")  # Update label after successful download
        except Exception as e:
            downloading_label.config(text="Error occurred.")  # Update label if an error occurs
            print(f"Please try again, may have been invalid URL. ERROR: {e}")

    # Run the download in a separate thread
    threading.Thread(target=download_video).start()

def OpenFolder(path):
    os.startfile(path)

res = "360p"   
def SetRes(set_res):
    global res
    res = set_res

def main():
    root = Tk()  # create a root widget
    root.title("Download Helper")
    root.configure(background="white")
    root.minsize(300, 300)  # width, height
    root.maxsize(300, 300)
    root.geometry("300x300")  # width x height + x + y
    
    # URL Label and Entry
    tkinter.Label(root, text="URL").grid(row=0, column=2)
    e1 = tkinter.Entry(root)
    e1.grid(row=0, column=4)
    
    # Resolution Buttons
    tkinter.Button(root, text='360p', command=lambda: SetRes("360p")).place(x=0, y=60)
    tkinter.Button(root, text='720p', command=lambda: SetRes("720p")).place(x=50, y=60)
    tkinter.Button(root, text="1080p", command=lambda: SetRes("1080p")).place(x=90, y=60)

    # Label to show download status
    downloading_label = tkinter.Label(root, text="")
    downloading_label.place(x=100, y=150)

    # Download Button
    tkinter.Button(root, text='Download', 
                   command=lambda: DownloadYTVid(e1.get(), res, root, downloading_label)).grid(row=4, column=2, sticky=tkinter.W, pady=4)

    # Open Folder Button
    tkinter.Button(root, text='Open Folder', command=lambda: OpenFolder("YT_Downloads")).grid(row=4, column=3, sticky=tkinter.W, pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()
