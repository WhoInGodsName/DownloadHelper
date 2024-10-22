import threading
import tkinter
from pytubefix import YouTube
from tkinter import *
import os
from moviepy.editor import VideoFileClip, AudioFileClip

def DownloadYTVid(url, res, root, downloading_label):
    downloading_label.config(text="Downloading...")  # Update the label text

    def download_video():
        try:
            yt = YouTube(url)
            
            # Download video stream
            video_stream = yt.streams.filter(res=res, progressive=False, file_extension='mp4').first()
            audio_stream = yt.streams.filter(only_audio=True).first()
            
            

            video_path = video_stream.download(output_path="YT_Downloads", filename="video.mp4")
            audio_path = audio_stream.download(output_path="YT_Downloads", filename="audio.mp4")

            # Update paths using os.path.join
            video_path = os.path.join("YT_Downloads", "video.mp4")
            audio_path = os.path.join("YT_Downloads", "audio.mp4")

            # Check if files exist
            if not os.path.exists(video_path) or not os.path.exists(audio_path):
                downloading_label.config(text="Download failed. Files not found.")
                return

            # Update label after successful download
            downloading_label.config(text="Download complete! \n Merging video and audio...")

            # Merging video and audio using MoviePy
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)
            
           

            final_clip = video_clip.set_audio(audio_clip)
            output_path = os.path.join("YT_Downloads", video_stream.default_filename)
            final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

            downloading_label.config(text="Merge complete! Video saved.")
            
            os.remove(video_path)
            os.remove(audio_path)

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
