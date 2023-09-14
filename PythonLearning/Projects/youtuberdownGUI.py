from tkinter import *
from pytube import YouTube

# initalize tkinter
root = Tk()
root.geometry("400x350") # 400x 350 pixel box
root.title("Youtube Video Downloader")

# a adjusted version of old downloader
def Download():
    youtubeObject = YouTube(link.get())
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    # youtubeObject = youtubeObject.streams.filter(res="720p") # gets a 720p resolution
    try:
        youtubeObject.download()
    except:
        print("An error has occured while downloading")
    
    print("Download is completed successfully")

# Welcomes users
Label(root, text="Welcome to Youtube Downloader", font="Consolas 15 bold")
instructionStr = StringVar()
instructionStr.set("Enter Link Below")
Entry(root, textvariable=instructionStr, width=40).pack(pady=10)
link = StringVar()
# Entry widget for the link
Entry(root, textvariable=link, width=40).pack(pady=10)
Button(root, text="Download Video", command=Download).pack()
root.mainloop()




# def download():
#     # using try and except to execute program without errors
#     try:
#         myVar.set("Downloading...")
#         root.update()
#         YouTube(link.get()).streams.first().download()
#         link.set("Video downloaded successfully")
#     except Exception as e:
#         myVar.set("Mistake")
#         root.update()
#         link.set("Enter Correct Link")

# myVar = StringVar()
# myVar.set("Enter the link below")
# # declaring StringVar type variable
# link = StringVar()
# # created the Entry widget to get the link
# Entry(root, textvariable=link, width=40).pack(pady=10)
# # created and called the download function to download video
# Button(root, text="Download video", command=download).pack()
# # running the mainloop
# root.mainloop()