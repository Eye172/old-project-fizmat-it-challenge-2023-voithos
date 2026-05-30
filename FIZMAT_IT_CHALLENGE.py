from tkinter import *
from pygame import mixer
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from pytube import YouTube
import sys
import wikipedia
import googletrans
from googletrans import Translator
import moviepy.editor as me



x=0
mixer.init()
tf=True
tf1=False
tf2=False
tf3=False
tf4=False

def openfile():
    song = filedialog.askopenfilename(initialdir='tracks/', title="Выберите файл!", filetypes=(("mp3 Files", "*.mp3"),))
    song_box.insert(END, song)

def openfiles():
    files = filedialog.askopenfilenames(initialdir='tracks/', title="Выберите файл!", filetypes=(("mp3 Files", "*.mp3"),))
    for file in files:
        song_box.insert(END, file)

def pause():
    global x
    x+=1
    if x%2==0:
        mixer.music.unpause()
        song_state['text'] = "< Воспроизведение >"
    else:
        mixer.music.pause()
        song_state['text'] = "< Пауза >"

def play():
    song = song_box.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
    song_state['text'] = "< Воспроизведение >"

def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "< Остановлено >"

def next_song():
    next_s = song_box.curselection()
    next_s = next_s[0] + 1
    song = song_box.get(next_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)

def back_song():
    back_s = song_box.curselection()
    back_s = back_s[0] - 1
    song = song_box.get(back_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(back_s)
    song_box.selection_set(back_s, last=None)

def clear():
    song_box.delete(0,END)

def vol(v):
    mixer.music.set_volume(float(int(v)/100))

def perevod1():
    translator = Translator()
    p1= translator.translate(text=e3.get() , src=e1.get(), dest=e2.get())
    l5['text']=p1.text
    
def perevod2():
    translator = Translator()
    p1= translator.translate(text=e4.get())
    l7['text']=p1.text

def open_img():
    global l_img2, e_text1, label1
    filepath = filedialog.askopenfilename()
    img = Image.open(filepath)
    s=filepath.split("/")
    u=ImageTk.PhotoImage(file=s[-1])
    l_img2=Button(image=u)
    l_img2.image=u
    l_img2.grid(column=0, row=0)
    e_text1.insert(0, pytesseract.image_to_string(img))
    label1['text']=pytesseract.image_to_string(img)
    
def eye():
    global ew1, ew2, lw2
    w=ew1.get()
    sp=w.split()
    q1=sp[0]
    q2=int(sp[1])
    q3=sp[2]
    wikipedia.set_lang(q3)
    look=wikipedia.summary(q1, sentences=q2) 
    ew2.insert(0, look)
    lw2['text']=look
    
def linker():
    link=e_link.get()
    qwertys=YouTube(link)
    w=qwertys.streams.all()
    i=0
    w[i].download()

def openia():
    global tf, tf1, tf2, tf3, tf4
    global root
    tf=True
    if tf1:
        root1.destroy()
        tf1=False
    elif tf2:
        root2.destroy()
        tf2=False
    elif tf3:
        root3.destroy()
        tf3=False
    elif tf4:
        root4.destroy()
        tf4=False
    mixer.music.stop()
    root = Tk()
    root.title("Voithos")
    menushka = Menu(root)
    root.config(menu=menushka)
    work_menushka1=Menu(menushka)
    work_menushka1.add_command(label="Аудиоплеер", command = openia1)
    work_menushka2=Menu(menushka)
    work_menushka2.add_command(label="Переводчик", command = openia2)
    work_menushka3=Menu(menushka)
    work_menushka3.add_command(label="Википедия", command = openia3)
    work_menushka4=Menu(menushka)
    work_menushka4.add_command(label="Текст с изображения", command = openia4)
    work_menushka5=Menu(menushka)
    work_menushka5.add_command(label="Выход", command = dead)
    menushka.add_cascade(label="Аудиоплеер", menu=work_menushka1)
    menushka.add_cascade(label="Переводчик", menu=work_menushka2)
    menushka.add_cascade(label="Википедия", menu=work_menushka3)
    menushka.add_cascade(label="Текст с изображения", menu=work_menushka4)
    menushka.add_cascade(label="Выход", menu=work_menushka5)
    img=ImageTk.PhotoImage(file="menu_bg_2.jpg")
    l_img=Label(image=img) 
    l_img.grid(row=0,column=0)
    l1972=Label(text="Изображение было нарисовано нейросетью Dream от WOMBO")
    l1972.grid(row=1,column=0)
    root.mainloop()
    
def openia1():
    global tf, tf1, tf2, tf3, tf4
    global song_state, song_box, scale, e_link
    global root1
    tf1=True
    if tf2:
        root2.destroy()
        tf2=False
    elif tf3:
        root3.destroy()
        tf3=False
    elif tf4:
        root4.destroy()
        tf4=False
    elif tf:
        root.destroy()
        tf=False
    root1 = Tk()
    root1.title("Voithos")
    master_frame = Frame(root1)
    master_frame.pack()
    info_frame = Frame(master_frame)
    info_frame.grid(row=0, column=0)
    controls_frame = Frame(master_frame)
    controls_frame.grid(row=1, column=0)
    back_button=Button(controls_frame, text="Предыдущий", bg="Purple", command=back_song, foreground="White")
    back_button.grid(row=0, column=0)
    forward_button=Button(controls_frame, text="Следующий",bg="Purple", command=next_song, foreground="White")
    forward_button.grid(row=0, column=1)
    play_button=Button(controls_frame, text="Воспроизвести", bg="Green", command=play, foreground="White")
    play_button.grid(row=0, column=2)
    pause_button=Button(controls_frame, text="Пауза", bg="Yellow", command=pause, foreground="Purple")
    pause_button.grid(row=0, column=3)
    stop_button=Button(controls_frame, text="Остановить", bg="Red", command=stop, foreground="White")
    stop_button.grid(row=0, column=4)
    file_frame = Frame(master_frame)
    file_frame.grid(row=0, column=5)
    openfile_button=Button(file_frame, text="Открыть один файл", bg="Lightgray", command=openfile, foreground="White")
    openfile_button.grid(row=1, column=0)
    openfolder_button=Button(file_frame, text="Открыть несколько файлов", bg="Gray", command=openfiles, foreground="White")
    openfolder_button.grid(row=0, column=0)
    clear_button=Button(file_frame, text="Очистить список", command=clear)
    clear_button.grid(row=3, column=0)
    song_state = Label(info_frame, width=60, text="< Остановлено >", font="Comfortaa 8 bold")
    song_state.grid(row=0, column=0)
    song_box = Listbox(info_frame, width=60, selectbackground="purple")
    song_box.grid(row=1, column=0)
    openia_button=Button(file_frame, text="<- Назад", bg="Gray", command=openia, foreground="White")
    openia_button.grid(row=7,column=0)
    e_link=Entry(file_frame)
    e_link.grid(row=4, column=0)
    b_download=Button(file_frame, text="Скачать", command=linker, bg="Lightgray")
    b_download.grid(row=5,column=0)
    variant=DoubleVar()
    scale=Scale(file_frame, variable=variant, command=vol)
    scale.grid(row=6, column=0)
    root1.mainloop()

def openia2():
    global tf, tf1, tf2, tf3, tf4
    global e1, e2, e3, e4, l5, l7
    global root2
    tf2=True
    if tf1:
        root1.destroy()
        tf1=False
    elif tf3:
        root3.destroy()
        tf3=False
    elif tf4:
        root4.destroy()
        tf4=False
    elif tf:
        root.destroy()
        tf=False
    mixer.music.stop()
    root2=Tk()
    root2.title("Voithos")
    l0=Label(text="Введите переводимый язык и язык перевода в формате en, ru и.т.д.", bg="Gray", foreground="White")
    l1=Label(text="Переводимый язык :")
    l2=Label(text="Язык перевода :")
    l3=Label(text="--->")
    l5=Label(text="    ")
    l6=Label(text="===>")
    l7=Label(text="    ") 
    l8=Label(text="Переводчик сам определяющий язык :", bg="Gray", foreground="White")
    e1=Entry()
    e2=Entry()
    e3=Entry()
    e4=Entry()
    b0=Button(text="Перевести", command=perevod1)
    b1=Button(text="Перевести", command=perevod2)
    l0.grid(row=0 ,column=1 )
    l1.grid(row=1 ,column=0 )
    l2.grid(row=1 ,column=2 )
    l3.grid(row=2 ,column=1 )
    e1.grid(row=2 ,column=0 )
    e2.grid(row=2 ,column=2)
    e3.grid(row=3 ,column=0 )
    l5.grid(row=3 ,column=2 )
    b0.grid(row=4 ,column= 1)
    l8.grid(row=5 ,column=1 )
    l6.grid(row=6 ,column=1 )
    l7.grid(row=6 ,column=2 )
    e4.grid(row=6 ,column=0 )
    b1.grid(row=7 ,column=1 )
    openia_button=Button(text="<- Назад", command=openia, bg="Gray" , foreground="White")
    openia_button.grid(row=8,column=1)
    root2.mainloop()
    
def openia3():
    global tf, tf1, tf2, tf3, tf4
    global ew1, ew2, lw2
    global root3
    tf3=True
    if tf2:
        root2.destroy()
        tf2=False
    elif tf1:
        root1.destroy()
        tf1=False
    elif tf4:
        root4.destroy()
        tf4=False
    elif tf:
        root.destroy()
        tf=False
    mixer.music.stop()
    root3=Tk()
    root3.title("Voithos")
    lw1=Label(text="WIKIPEDIA", font="Comfortaa 20 bold")
    lw2=Label(text="Time...")
    lw2['wraplength']=500
    ew1=Entry()
    ew2=Entry()
    lw1.grid(row=0 ,column=2)
    ew1.grid(row=2 ,column=0)
    ew2.grid(row=2 ,column=3)
    lw2.grid(row=3 ,column=2)
    bw=Button(text="Найти", command=eye)
    bw.grid(row=4, column=2)
    openia_button=Button(text="<- Назад", command=openia, bg="gray" , foreground="White")
    openia_button.grid(row=5,column=2)
    root3.mainloop()

def openia4():
    global tf, tf1, tf2, tf3, tf4
    global root4
    global e_text1, label1
    tf4=True
    if tf2:
        root2.destroy()
        tf2=False
    elif tf3:
        root3.destroy()
        tf3=False
    elif tf1: 
        root1.destroy()
        tf1=False
    elif tf:
        root.destroy()
        tf=False
    mixer.music.stop()
    root4=Tk()
    root4.title("Voithos")
    b_img=Button(text="Загрузить изображение", command=open_img)
    b_img.grid(row=1, column=0)
    e_text1=Entry()
    e_text1.grid(row=3, column=0)
    label1=Label(text="Time...") 
    label1.grid(row=2, column=0)
    openia_button=Button(text="<- Назад", command=openia)
    openia_button.grid(row=4,column=0)
    root4.mainloop()
    
def dead():
    sys.exit()


root = Tk()
root.title("Voithos")

menushka = Menu(root)
root.config(menu=menushka)
work_menushka1=Menu(menushka)
work_menushka1.add_command(label="Аудиоплеер", command = openia1)
work_menushka2=Menu(menushka)
work_menushka2.add_command(label="Переводчик", command = openia2)
work_menushka3=Menu(menushka)
work_menushka3.add_command(label="Всевидящее око <()>", command = openia3)
work_menushka4=Menu(menushka)
work_menushka4.add_command(label="Текст с изображения", command = openia4)
work_menushka5=Menu(menushka)
work_menushka5.add_command(label="Выход", command = dead)
menushka.add_cascade(label="Аудиоплеер", menu=work_menushka1)
menushka.add_cascade(label="Переводчик", menu=work_menushka2)
menushka.add_cascade(label="Википедия", menu=work_menushka3)
menushka.add_cascade(label="Текст с изображения", menu=work_menushka4)
menushka.add_cascade(label="Выход", menu=work_menushka5)
img=ImageTk.PhotoImage(file="menu_bg_2.jpg")
l_img=Label(image=img)
l_img.grid(row=0,column=0)
l1972=Label(text="Изображение было нарисовано нейросетью Dream от WOMBO")
l1972.grid(row=1,column=0)
root.mainloop()