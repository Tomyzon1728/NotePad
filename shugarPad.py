
from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import askquestion,showinfo
filename=''
#---------------------------------------------------------------------------------
root = Tk()
root.title('Untitled Shugar-Notepad')
root.wm_iconbitmap('notepad.ico')
#---------------------------------------------------------------------------------
mcontent = Text(root,height = 42, width = 168, bg='#FFFACD')
mcontent.grid(row = 0, column = 0)
scrolly = Scrollbar (root, orient = 'vertical', command = mcontent.yview)
scrollx = Scrollbar (root, orient = 'horizontal', command = mcontent.xview)
scrolly.grid(row =0, column = 1, sticky = 'ns')
scrollx.grid(row = 1, column = 0, sticky ='ew')
mcontent.configure(yscrollcommand = scrolly.set)
mcontent.configure(xscrollcommand = scrollx.set)
#----------------------------------------------------------------------------------------
def newpage():
    global filename
    root.title('Untitled Shugar-Notepad')
    filename = None
    mcontent.delete(1.0,'end')
def openf():
    filename = askopenfilename(defaultextension = '.txt',filetypes = [('All Files','*.*'),('Text files','.txt')])
    if filename == '':
        filename = None
    else:
        o = open(filename).read()
        mcontent.insert('end',o)
        filename.close()
def save():
    global filename
    if filename=='':
             filename= asksaveasfilename(filetypes = [('All Files',('.txt'))])
             if filename=='':
                filename= None
             else:
                s = open(filename,'w')
                s.write(mcontent.get(1.0,'end'))
                filename.close()
    else:
            s = open(filename,'w')
            s.write(mcontent.get(1.0,'end'))
            filename.close()
def saveas():
    global filename
    filename= asksaveasfilename(filetypes = [('All Files',('.txt'))])
    if filename == '':
        filename = None
    else:
        s = open(filename,'w')
        s.write(mcontent.get(1.0,'end'))
        filename.close()
def pgst():
    pass
def printf():
    pass
def Quit():
    answer = askquestion(title='Quit?', message='Are you sure?')
    if answer=='yes':
        root.destroy()
#---------------------------------------------------------------------------------
def Undo():
    mcontent.edit_undo()
def Paste():
     mcontent.event_generate('<<Paste>>')
def Cut():
     mcontent.event_generate('<<Cut>>')
def Copy():
    mcontent.event_generate('<<Copy>>')
def Delete():
     #delt = askquestion(title='Quit?', message='Are you sure?')
     #if delt=='yes':
         #mcontent.delete(0,"end")
         pass
def findf():
    pass
def findn():
    pass
def rep():
    pass
def gt():
    pass
def selall():
    mcontent.tag_add(SEL,'1.0','end')
    mcontent.mark_set(INSERT,'1.0')
    mcontent.see(INSERT)
def td():
    pass

#--------------------------------------------------------------------------------------------------
def wordw():
    pass
def fontf():
    pass
#--------------------------------------------------------------------------------------------------
def sb():
    pass
def vh():
    pass
#-------------------------------------------------------------------------------
def abt():
    inf = showinfo(title=' About Shugarpad', message='This Product is Liscensed to Ajayi R.O')
    if inf=='yes':
        root.update()
        #---------------------------------------------------------------------------------
load = Image.open('file.png')
render = ImageTk.PhotoImage(load, master = root)
load1 = Image.open('cancel.png')
render1 = ImageTk.PhotoImage(load1, master = root)
load12 = Image.open('bnew.png')
render12 = ImageTk.PhotoImage(load12, master = root)
load13 = Image.open('save.png')
render13 = ImageTk.PhotoImage(load13, master = root)
load14 = Image.open('saveas.png')
render14 = ImageTk.PhotoImage(load14, master = root)
loads = Image.open('bexit.png')
renders = ImageTk.PhotoImage(loads, master = root)
loadp = Image.open('cprint.png')
renderp = ImageTk.PhotoImage(loadp, master = root)
loadcp = Image.open('bcopy.png')
rendercp = ImageTk.PhotoImage(loadcp, master = root)
loadps = Image.open('bpaste.png')
renderps = ImageTk.PhotoImage(loadps, master = root)
loadu = Image.open('bundo.png')
renderu = ImageTk.PhotoImage(loadu, master = root)        

menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'New',command=newpage, accelerator = 'Ctrl+N',image=render12, compound='left')
fileMenu.add_command(label = 'Open...',command=openf , accelerator = 'Ctrl+O',image=render, compound='left')
fileMenu.add_command(label = 'Save',command=save , accelerator = 'Ctrl+S',image=render13, compound='left')
fileMenu.add_command(label = 'Save As...',command=saveas,image=render14, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Page Setup...',command=pgst)
fileMenu.add_command(label = 'Print...',command=printf ,image=renderp, compound='left', accelerator = 'Ctrl+P')
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit',command=Quit,image=renders, compound='left')
menubar.add_cascade(label = 'File',menu = fileMenu,underline = 0)
root.config(menu = menubar)
#---------------------------------------------------------------------------------
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Undo',command=Undo , accelerator = 'Ctrl+Z',image=renderu, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Cut',command=Cut , accelerator = 'Ctrl+X')
fileMenu.add_command(label = 'Copy',command=Copy , accelerator = 'Ctrl+C',image=rendercp, compound='left')
fileMenu.add_command(label = 'Paste',command=Paste , accelerator = 'Ctrl+V',image=renderps, compound='left')
fileMenu.add_command(label = 'Delete',command=Delete , accelerator = '     Del',image=render1, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Find...',command=findf , accelerator = 'Ctrl+F')
fileMenu.add_command(label = 'Find Next',command=findn , accelerator = '       F3')
fileMenu.add_command(label = 'Replace...',command=rep , accelerator = 'Ctrl+H')
fileMenu.add_command(label = 'Go To',command=gt , accelerator = 'Ctrl+G')
fileMenu.add_separator()
fileMenu.add_command(label = 'Select All',command=selall , accelerator = 'Ctrl+A')
fileMenu.add_command(label = 'Time/Date',command=td , accelerator = '       F5')
menubar.add_cascade(label = 'Edit',menu = fileMenu, underline =0)
#---------------------------------------------------------------------------------
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Word Wrap',command=wordw)
fileMenu.add_command(label = 'Font...',command=fontf)
menubar.add_cascade(label = 'Format',menu = fileMenu, underline =0)
root.config(menu = menubar)
#---------------------------------------------------------------------------------
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Status Bar',command=sb)
menubar.add_cascade(label = 'View',menu = fileMenu, underline =0)
root.config(menu = menubar)
#---------------------------------------------------------------------------------
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'View Help',command=vh)
fileMenu.add_separator()
fileMenu.add_command(label = 'About',command=abt)
menubar.add_cascade(label = 'Help',menu = fileMenu, underline =0)
root.config(menu = menubar)
#---------------------------------------------------------------------------------
#stat = StringVar()
#statbar = Frame(mcontent)
root.mainloop()