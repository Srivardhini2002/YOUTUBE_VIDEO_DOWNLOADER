from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from pytube import YouTube




root=Tk()
root.geometry("1366x768+0+0")
root.resizable(True,True)
root.state("zoomed")
root.title("YouTube Video Downloader")
root.config(bg="white")

icon=PhotoImage(file = 'tube.png')
root.iconphoto(False,icon)

url=StringVar()
quality=StringVar()
quality.set("720p")

mainFrame=Frame(root,bg="#FF0000")
mainFrame.place(x=200,y=50,width="966",height="600")

titleLabel=Label(mainFrame,bg="white",fg="#FF0000",text="YouTube video Downloader",font=("simsun",20,"bold"))
titleLabel.place(x=10,y=10,width="946",height="30")

urlLabel=Label(mainFrame,bg="#FF0000",fg="white",text="Paste the URL here   :",font=("tahoma",15))
urlLabel.place(x=10,y=100)

urlText=Entry(mainFrame,bg="white",textvariable=url,fg="#FF0000")
urlText.place(x=250,y=105,width="250",height="23")

resolution=ttk.Combobox(mainFrame,textvariable=quality,state="readonly")
resolution['values']=("1080p","720p","360p","240p","144p")
resolution.place(x=550,y=105,width="150")

#function for progressive bar

def bar():

    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100


#main function for downloading youtube video

def getting():

    link=url.get()
    qual=quality.get()
    
    try:
        video=YouTube(link)
        stream=video.streams.filter(progressive="True",file_extension="mp4",res=qual).first().download()
        nameLabel.config(text=video.title)
        resultLabel.config(text="Downloaded Successfully")
        bar()
    except:
        resultLabel.config(text="Can't Download")
        progress['value']=0



btnDownload=Button(mainFrame,command=getting,bg="white",fg="#FF0000",bd=0,text="DOWNLOAD",font=("calibri",16,"bold"))
btnDownload.place(x=350,y=175)

progress = ttk.Progressbar(mainFrame,orient='horizontal',mode='determinate',length=200)
progress.place(x=500,y=185)

naming=Label(mainFrame,bg="#FF0000",fg="white",text="Your Video          :",font=("tahoma",15))
naming.place(x=40,y=250)

nameLabel=Label(mainFrame,bg="white",text="",fg="#FF0000")
nameLabel.place(x=250,y=250,width=450)

resultLabel=Label(mainFrame,bg="white",text="",fg="#FF0000")
resultLabel.place(x=750,y=250,width=150)




root.mainloop()
