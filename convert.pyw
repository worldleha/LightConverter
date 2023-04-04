import ffmpy
import tkinter
import tkinter.filedialog
import tkinter.ttk
import tkinter.messagebox
import windnd
import os
import re
innerm=None
brlabel3=None
brtext=None
brtypebox=None
outputpath=None
comvalue=None
fileset={}
outputtype=(".mp4",".avi",".wav",".flv",".ogg",".m4s")


def is_m4s(em):
    print(em[-4:])
    if em[-4:] in outputtype:
        return True
    else:
        return False

def convert(path):

    ffexe = ffmpy.FFmpeg(inputs=fileset,outputs={path: '-c:v h264_nvenc'})
    ffexe.run()

def selectpath():
    path=tkinter.filedialog.askdirectory()
    outputpath.set(path)
    
def filein(file):
       for i in file:
            filepath=i.decode('gbk')
            if is_m4s(filepath):
               
                if filepath not in fileset:
                    fileset[filepath]=None
                    File_item(innerm,filepath)
                    
            else:
                print("unknowntype")

def outprint():
    try:
        path=(outputpath.get()+'/'+brtext.get('1.0','end')+brtypebox.get()).replace("\n",'')
        if os.path.exists(path):
            boolean=tkinter.messagebox.askquestion(title = 'convert',message='文件已存在是否覆盖？')
            if boolean:
                os.remove(path)
                convert(path)
                tkinter.messagebox.askquestion(title = 'convert',message='成功！')
        else:
            convert(path)
            tkinter.messagebox.askquestion(title = 'convert',message='成功！')
    except:
        result=tkinter.messagebox.askquestion(title = 'convert',message='失败！')
        
class File_item(tkinter.Frame):
    
    def __init__(self,master=None,text="ex"):
        self.text=text
        self.textlist=[os.path.basename(text),os.path.splitext(text)[1]]
        self.item_frame=tkinter.Frame(master=master,width=180,height=20,bg="white")
        self.item_frame.pack(side=tkinter.TOP,anchor=tkinter.N)
        self.item_label=tkinter.Label(master=self.item_frame,text=self.textlist[0],fg="black",bg="white")
        self.item_label.place(x=0,y=0)
        self.item_button=tkinter.Button(master=self.item_frame,bg="white",image=image_d,width=20,height=16,command=self.filedel)
        self.item_button.place(x=154,y=0)
    def filedel(self):
        fileset.pop(self.text)
        self.item_frame.destroy()
        
window=tkinter.Tk()
window.title("Light转换器")
window.geometry("400x400+%d+%d"%(window.winfo_screenwidth()//2-200,window.winfo_screenheight()//2-200))
window.resizable(0,0)
window.iconbitmap("img/start.ico")
outputpath=tkinter.StringVar()
outputpath.set("video")
comvalue=tkinter.StringVar()

topframe=tkinter.Frame(master=window,width=400,height=200)
topframe.pack()
image_p=tkinter.PhotoImage(file="img/vid.gif")
image_d=tkinter.PhotoImage(file="img/del.gif")
image_put=tkinter.Label(master=topframe,width=400,height=200,image=image_p)
image_put.pack()
#建立拖放
inputwin=windnd.hook_dropfiles(topframe,func=filein)

bottomframe=tkinter.Frame(master=window,width=400,height=200)
bottomframe.pack(side=tkinter.BOTTOM)

bleftframe=tkinter.Frame(master=bottomframe,width=200,height=200,bg="white")
bleftframe.pack(side=tkinter.LEFT,expand=1,anchor=tkinter.W)
innerl=tkinter.Frame(master=bleftframe,width=10,height=180,bg="white")
innerl.pack(side=tkinter.LEFT)
innerm=tkinter.Frame(master=bleftframe,width=180,height=180,bg="white")
innerm.pack(side=tkinter.LEFT)
innerr=tkinter.Frame(master=bleftframe,width=10,height=180,bg="white")
innerr.pack(side=tkinter.LEFT)

    

brightframe=tkinter.Frame(master=bottomframe,width=200,height=200,bg="white")
brightframe.pack(side=tkinter.LEFT)
brlabel1=tkinter.Label(master=brightframe,text="路径: ")
brlabel1.place(x=10,y=10)
brlabel2=tkinter.Label(master=brightframe,width=22,font = 'Helvetica -9 bold',textvariable=outputpath)
brlabel2.place(x=50,y=12)
brlabel1=tkinter.Label(master=brightframe,text="名称: ")
brlabel1.place(x=10,y=40)

brtext=tkinter.Text(master=brightframe,font= 'Helvetica -12 bold',width=12,height=1)
brtext.place(x=50,y=42)

brtext.insert("end", "video")

#print(brtext.get('1.0','end'))

brtypebox=tkinter.ttk.Combobox(master=brightframe,width=4,textvariable=comvalue)
brtypebox["values"]=outputtype
brtypebox.current(0)
brtypebox.place(x=140,y=40)

brbutton1=tkinter.Button(master=brightframe,text="更改路径",width=10,command=selectpath)
brbutton1.place(x=36,y=100)


brbutton3=tkinter.Button(master=brightframe,width=12,height=1,text="导出",command=outprint)
brbutton3.place(x=30,y=150)
window.mainloop()


'''

'''
