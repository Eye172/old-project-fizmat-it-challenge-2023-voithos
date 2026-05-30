import sys
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageFont, ImageFilter
from pygame import mixer
import wikipedia
import googletrans
from googletrans import Translator
from pytube import YouTube
import moviepy.editor as me

x=0
mixer.init()
tf = True
tf1 = False
tf2 = False
tf3 = False
tf4 = False

def openfile():
    song = filedialog.askopenfilename(initialdir = 'tracks/', title = "Выберите файл", filetypes = (("mp3 Files","*.mp3"),))
    song_box.insert(END, song)
def openfiles():
    files = filedialog.askopenfilenames(initialdir = 'tracks/', title = "Выберите файлы", filetypes = (("mp3 Files","*.mp3"),))
    for file in files:
        song_box.insert(END, file)
def pause():
    global x
    x += 1
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
    song_state['text'] = '< Воспроизведение >'
def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = '< Остановлено >'
def next_song():
    next_s = song_box.curselection()
    next_s = next_s[0] + 1
    song = song_box.get(next_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last = None)   
def back_song():
    back_s = song_box.curselection()
    back_s = back_s[0] - 1
    song = song_box.get(back_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(back_s)
    song_box.selection_set(back_s, last = None)
def clear():
    mixer.music.stop()
    song_box.delete(0, END)
    
def vol(v):
    mixer.music.set_volume(float(int(v)/100))
    
def perevod1():
    translator = Translator()
    p1 = translator.translate(text=e3.get(), src=e1.get(), dest=e2.get())
    l5['text'] = p1.text
    
def perevod2():
    translator = Translator()
    p1 = translator.translate(text=e4.get())
    l7['text'] = p1.text
    
def eye():
    global ew1, ew2, ew3
    w = ew1.get()
    sp = w.split()
    q1 = sp[0]
    q2 = int(sp[1])
    q3 = sp[2]
    wikipedia.set_lang(q3)
    look = wikipedia.summary(q1, sentences=q2)
    ew2.insert(0, look)
    lw2['text'] = look
    
def linker():
    link = e_link.get()
    qwertys = YouTube(link)
    w = qwertys.streams.all()
    w[0].download()

def open_img():
    global u, l_img2, img
    filepath = filedialog.askopenfilename()
    img = Image.open(filepath)
    s=filepath.split("/")
    u=ImageTk.PhotoImage(file=s[-1])
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
def BLUR():
    global u, l_img2, img
    img = img.filter(ImageFilter.BLUR)
    img.save("user_image_BLUR.jpg")
    u=ImageTk.PhotoImage(file="user_image_BLUR.jpg")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
    
def DETAIL():
    global u, l_img2, img
    img = img.filter(ImageFilter.DETAIL)
    img.save("user_image_DETAIL.jpg")
    u=ImageTk.PhotoImage(file="user_image_DETAIL.jpg")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
def CONTOUR():
    global u, l_img2, img
    img = img.filter(ImageFilter.CONTOUR)
    img.save("user_image_CONTOUR.jpg")
    u=ImageTk.PhotoImage(file="user_image_CONTOUR.jpg")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
def EMBOSS():
    global u, l_img2, img
    img = img.filter(ImageFilter.EMBOSS)
    img.save("user_image_EMBOSS.jpg")
    u=ImageTk.PhotoImage(file="user_image_EMBOSS.jpg")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
def SMOOTH():
    global u, l_img2, img
    img = img.filter(ImageFilter.SMOOTH)
    img.save("user_image_SMOOTH.jpg")
    u=ImageTk.PhotoImage(file="user_image_SMOOTH.jpg")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
def EDGE_ENHANCE():
    global u, l_img2, img
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    img.save("user_image_EDGE_ENHANCE.jpg")
    u=ImageTk.PhotoImage(file="user_image_EDGE_ENHANCE.jpg")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
def SHARPEN():
    global u, l_img2, img
    img = img.filter(ImageFilter.SHARPEN)
    img.save("user_image_SHARPEN.jpg")
    u=ImageTk.PhotoImage(file="user_image_SHARPEN.jpg")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
def custom_filter():
    global u, l_img2, e1_img, e2_img, e3_img, img
    q1=int(e1_img.get())
    q2=int(e2_img.get())
    q3=int(e3_img.get())
    source=img
    width,height=source.size
    result=Image.new("RGBA",(width,height))
    for w in range(width):
        for h in range(height):
            r,g,b=source.getpixel((w, h))
            result.putpixel((w,h),(q1-r,q2-g,q3-b,255))
    result.save("user_image_custom_filter.png")
    u=ImageTk.PhotoImage(file="user_image_custom_filter.png")
    l_img2=Label(image=u)
    l_img2.image=u
    l_img2.grid(column=2, row=0)
    
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
    root.config(menu = menushka)
    menushka1 = Menu(menushka)
    menushka2 = Menu(menushka)
    menushka3 = Menu(menushka)
    menushka4 = Menu(menushka)
    menushka5 = Menu(menushka)
    menushka1.add_command(label = "Аудиоплеер", command = openia1)
    menushka2.add_command(label = "Переводчик", command = openia2)
    menushka3.add_command(label = "Википедия", command = openia3)
    menushka4.add_command(label = "Фильтр изображений", command = openia4)
    menushka5.add_command(label = "Выход", command = death)
    menushka.add_cascade(label = "Аудиоплеер", menu = menushka1)
    menushka.add_cascade(label = "Переводчик", menu = menushka2)
    menushka.add_cascade(label = "Википедия", menu = menushka3)
    menushka.add_cascade(label = "Фильтр изображений", menu = menushka4)
    menushka.add_cascade(label = "Выход", menu = menushka5)
    root.mainloop()
    
def openia1():
    global tf, tf1, tf2, tf3, tf4
    global song_state, song_box, scale, e_link
    global root1
    tf1 = True
    if tf:
        root.destroy()
        tf = False
    elif tf2:
        root2.destroy()
        tf2 = False
    elif tf3:
        root3.destroy()
        tf3 = False
    elif tf4:
        root4.destroy()
        tf4 = False
    root1 = Tk()
    root1.title("Voithos")
    master_frame = Frame(root1)
    master_frame.pack()
    info_frame = Frame(master_frame)
    control_frame = Frame(master_frame)
    file_frame = Frame(master_frame)
    song_state = Label(info_frame, width = 60, text = "< Остановлено >", font = "Comfortaa 8 bold")
    song_box = Listbox(info_frame, width = 60, selectbackground = "purple")
    back_button = Button(control_frame, text = "Предыдущий", bg="Purple", command = back_song, foreground = "White")
    forward_button = Button(control_frame, text = "Следующий", bg="Purple", command = next_song, foreground = "White")
    play_button = Button(control_frame, text = "Воспроизвести", bg="Green", command = play, foreground = "White")
    pause_button = Button(control_frame, text = "Пауза", bg="Yellow", command = pause, foreground = "Purple")
    stop_button = Button(control_frame, text = "Остановить", bg="Red", command = stop, foreground = "White")
    clear_button = Button(file_frame, text = "Очистить список", command = clear)
    openfile_button = Button(file_frame, text = "Открыть один файл", bg="Lightgray", command = openfile)
    openfiles_button = Button(file_frame, text = "Открыть несколько файлов", bg="Gray", command = openfiles, foreground = "White")
    openia_button = Button(file_frame, text = "<- Назад", bg="Gray", command = openia, foreground = "White")
    vidownload_button = Button(file_frame, text = "Скачать", bg="Lightgreen", command = linker)
    e_link = Entry(file_frame)
    scale = Scale(file_frame, variable = DoubleVar(), command = vol)
    info_frame.grid(row = 0, column = 0)
    control_frame.grid(row = 1, column = 0)
    file_frame.grid(row = 0, column = 5)
    song_state.grid(row = 0, column = 0)
    song_box.grid(row = 1, column = 0)
    back_button.grid(row = 0, column = 0)
    forward_button.grid(row = 0, column = 1)
    play_button.grid(row = 0, column = 2)
    pause_button.grid(row = 0, column = 3)
    stop_button.grid(row = 0, column = 4)
    clear_button.grid(row = 3, column = 0)
    openfile_button.grid(row = 1, column = 0)
    openfiles_button.grid(row = 0, column = 0)
    openia_button.grid(row = 7, column = 0)
    vidownload_button.grid(row = 5, column = 0)
    e_link.grid(row = 4, column = 0)
    scale.grid(row = 6, column = 0)
    
def openia2():
    global tf, tf1, tf2, tf3, tf4
    global e1, e2, e3, e4, l5, l7
    global root2
    tf2 = True
    if tf:
        root.destroy()
        tf = False
    elif tf1:
        root1.destroy()
        tf1 = False
    elif tf3:
        root3.destroy()
        tf3 = False
    elif tf4:
        root4.destroy()
        tf4 = False
    mixer.music.stop()
    root2 = Tk()
    root2.title("Voithos")
    l0 = Label(text="Введите переводимый язык и язык перевода в формате en, ru и.т.д.", bg="Gray", foreground="White")
    l1 = Label(text="Переводимый язык :")
    l2 = Label(text="Язык перевода :")
    l3 = Label(text="--->")
    l4 = Label(text="===>")
    l5 = Label(text="    ")
    l6 = Label(text="    ")
    l7 = Label(text="Переводчик сам определяющий язык :", bg="Gray", foreground="White")
    e1 = Entry()
    e2 = Entry()
    e3 = Entry()
    e4 = Entry()
    b0 = Button(text = "Перевести", command = perevod1)
    b1 = Button(text = "Перевести", command = perevod2)
    l0.grid(row=0 ,column=1 )
    l1.grid(row=1 ,column=0 )
    l2.grid(row=1 ,column=2 )
    l3.grid(row=2 ,column=1 )
    e1.grid(row=2 ,column=0 )
    e2.grid(row=2 ,column=2 )
    e3.grid(row=3 ,column=0 )
    l4.grid(row=6 ,column=1 )
    b0.grid(row=4 ,column=1 )
    l6.grid(row=5 ,column=1 )
    l5.grid(row=3 ,column=2 )
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
    lw1 = Label(text="WIKIPEDIA", font="Comfortaa 20 bold")
    lw2 = Label(text="Time...")
    lw2['wraplength'] = 500
    ew1 = Entry()
    ew2 = Entry()
    bw = Button(text="Найти", command=eye)
    openia_button = Button(text="<- Назад", command=openia, bg="Gray" , foreground="White")
    lw1.grid(row=0, column=2)
    ew1.grid(row=2, column=0)
    ew2.grid(row=2, column=3)
    lw2.grid(row=3, column=2)
    bw.grid(row=4, column=2)
    openia_button.grid(row=5, column=2)
    root3.mainloop()
    
def openia4():
    global tf, tf1, tf2, tf3, tf4
    global root4
    global e1_img, e2_img, e3_img
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
    root4 = Tk()
    root4.title("Voithos")
    b_img = Button(text="Загрузить изображение", command=open_img)
    f1_button = Button(text="BLUR", command=BLUR)
    f2_button = Button(text="DETAIL", command=DETAIL)
    f3_button = Button(text="CONTOUR", command=CONTOUR)
    f4_button = Button(text="EMBOSS", command=EMBOSS)
    f5_button = Button(text="SMOOTH", command=SMOOTH)
    f6_button = Button(text="EDGE_ENHANCE", command=EDGE_ENHANCE)
    f7_button = Button(text="SHARPEN", command=SHARPEN)
    f8_button = Button(text="CUSTOM FILTER (R,G,B)", command=custom_filter)
    e1_img = Entry()
    e2_img = Entry()
    e3_img = Entry()
    openia_button = Button(text="<- Назад", bg="Gray" , foreground="White", command=openia)
    f1_button.grid(row=0,column=0)
    f2_button.grid(row=1,column=0)
    f3_button.grid(row=2,column=0)
    f4_button.grid(row=3,column=0)
    f5_button.grid(row=4,column=0)
    f6_button.grid(row=5,column=0)
    f7_button.grid(row=6,column=0)
    f8_button.grid(row=7,column=0)
    e1_img.grid(row=1,column=1)
    e2_img.grid(row=1,column=2)
    e3_img.grid(row=1,column=3)
    b_img.grid(row=0,column=4)
    openia_button.grid(row=10,column=0)
    root4.mainloop()
    
def death():
    sys.exit()
    
    
root = Tk()
root.title("Voithos")
menushka = Menu(root)
root.config(menu = menushka)
menushka1 = Menu(menushka)
menushka2 = Menu(menushka)
menushka3 = Menu(menushka)
menushka4 = Menu(menushka)
menushka5 = Menu(menushka)
menushka1.add_command(label = "Аудиоплеер", command = openia1)
menushka2.add_command(label = "Переводчик", command = openia2)
menushka3.add_command(label = "Википедия", command = openia3)
menushka4.add_command(label = "Фильтр изображений", command = openia4)
menushka5.add_command(label = "Выход", command = death)
menushka.add_cascade(label = "Аудиоплеер", menu = menushka1)
menushka.add_cascade(label = "Переводчик", menu = menushka2)
menushka.add_cascade(label = "Википедия", menu = menushka3)
menushka.add_cascade(label = "Фильтр изображений", menu = menushka4)
menushka.add_cascade(label = "Выход", menu = menushka5)
root.mainloop()