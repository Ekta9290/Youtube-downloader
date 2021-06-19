from pytube import YouTube
SAVE_PATH= "E:/"
link=input("Enter URL= ")
try:
    yt = YouTube(link)
except:
    print("Connection Error")   
video = yt.streams.first()
try:
    video.download(SAVE_PATH)
except:
    print("Some Error!")
print("Task Completed!")

