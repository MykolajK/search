'''
    An application that allows you to search in various search engines, video hosts, free photo studios and also
    open social networks and google services from one window.
    The libraries tkinter, webbrowser and pillow need to be installed in addition.
    ============================================================================================================
    Додаток, який дозволяє здійснюввати пошук у різних пошукових системах, відеохостингах, безплатних фотостоках
    а також відкривати соціальні мережі та сервіси google з одного вікна.
    Використано бібліотеки tkinter, webbrowser та pillow, яку необхідно встановити додатково. 
'''
# python 3.7.1 Windows 7
from tkinter import*
from tkinter import ttk
from PIL import ImageTk
import webbrowser

def openn(url):
    webbrowser.open(url)

def search(url):
    webbrowser.open(url+message.get().replace(' ', '+'))

def clear():
    search_entry.delete(0, END)

buttons ={"width": 20, "bg": '#DDA0DD'}

    
root = Tk()
root.title('Search')
root.geometry("670x455")

frame_top = Frame(root, relief=RIDGE, bg='#FFC0CB', bd=3) # RAISED FLAT

button = Button(frame_top, buttons)
button['text'] = 'Clear'
button['command'] = clear
button.pack(side=BOTTOM, anchor=NE, pady=5, padx=5) # RIGHT

search_label =  Label(frame_top, width=12, bg='#FFC0CB', font='14', fg='#0046D9', text='What to find?', anchor=E)
search_label.pack(side=LEFT, pady=3)

message = StringVar()

search_entry = Entry(frame_top, width=58, relief=RAISED, font='Arial 13', bg='#DDA0DD',  textvariable=message)
search_entry.pack(side=LEFT, padx=5)
search_entry.focus()
frame_top.grid(row=0, column=0,padx=5, pady=5)

p = ttk.Panedwindow (root, orient=HORIZONTAL)

f1 = ttk.Labelframe(p, text='Video')

button1 = Button(f1, buttons)
button1['text'] = 'Youtube'
button1['command'] = lambda: search('https://www.youtube.com/results?search_query=')
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = Button(f1, buttons)
button2['text'] = 'Vimeo'
button2['command'] = lambda: search('https://vimeo.com/search?q=')
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = Button(f1, buttons )
button3['text'] = 'Dailymotion'
button3['command'] = lambda: search('https://www.dailymotion.com/search/')
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = Button(f1, buttons )
button4['text'] = 'Rutube'
button4['command'] = lambda: search('https://rutube.ru/search/?query=')
button4.grid(row=1, column=1, padx=5, pady=5)


f2 = ttk.Labelframe(p, text='Site')
button1 = Button(f2, buttons)
button1['text'] = 'Google'
button1['command'] = lambda: search('https://www.google.com/search?q=')
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = Button(f2,buttons)
button2['text'] = 'Bing'
button2['command'] = lambda: search('https://www.bing.com/search?q=')
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = Button(f2, buttons)
button3['text'] = 'Yahoo'
button3['command'] = lambda: search('https://search.yahoo.com/search?p=')
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = Button(f2, buttons)
button4['text'] = 'Meta'
button4['command'] = lambda: search('https://search.meta.ua/search.asp?q=')
button4.grid(row=1, column=1, padx=5, pady=5)

p.add (f1)
p.add (f2)
p.grid(row=2, column=0, padx=4)


p2 = ttk.Panedwindow (root, orient=HORIZONTAL, width=650)
frame1 = ttk.Labelframe(p2, text='Free Images')

button1 = Button(frame1, buttons)
button1['text'] = 'freestockimages'
button1['command'] = lambda: openn('https://www.freestockimages.ru/photo')
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = Button(frame1, buttons)
button2['text'] = 'pixabay'
button2['command'] = lambda: search('https://pixabay.com/en/photos/')
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = Button(frame1, buttons)
button3['text'] = 'firestock'
button3['command'] = lambda: search('https://www.firestock.ru/?s=')
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = Button(frame1, buttons)
button4['text'] = 'Dreamstime'
button4['command'] = lambda: openn('https://www.dreamstime.com/free-photos')
button4.grid(row=1, column=1, padx=5, pady=5)

button5 = Button(frame1, buttons)
button5['text'] = 'freeimages'
button5['command']  = lambda: search('https://www.freeimages.com/search/')
button5.grid(row=2, column=0, padx=5, pady=5)

button6 = Button(frame1, buttons)
button6['text'] = 'morguefile'
button6['command'] = lambda: search('https://morguefile.com/photos/morguefile/1/pop')
button6.grid(row=2, column=1, padx=5, pady=5)

button7 = Button(frame1, buttons)
button7['text'] = 'stockvault'
button7['command'] = lambda: search('https://www.stockvault.net/free-photos')
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(frame1, buttons) 
button8['text'] = 'stocksnap'
button8['command'] = lambda: search('https://stocksnap.io/search/')
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(frame1, buttons) 
button9['text'] = 'Life of Pix'
button9['command'] = lambda: search('https://www.lifeofpix.com/search/')
button9.grid(row=4, column=0, padx=5, pady=5)

button10 = Button(frame1, buttons) 
button10['text'] = 'world-photo'
button10['command'] = lambda: openn('https://world-photo.ru/besplatniy-photobank/skachat-foto/')
button10.grid(row=4, column=1, padx=5, pady=5)

button11 = Button(frame1, buttons) 
button11['text'] = 'IM Free'
button11['command'] = lambda: openn('http://www.imcreator.com/free')
button11.grid(row=5, column=0, padx=5, pady=5)

button12 = Button(frame1, buttons) 
button12['text'] = 'more...'
button12['command'] = lambda: openn('https://www.adme.ru/tvorchestvo-fotografy/70-luchshih-resursov-s-besplatnymi-fotografiyami-975760/')
button12.grid(row=5, column=1, padx=5, pady=5)



frame2 = ttk.Labelframe(p2, text='Server')
im1 = ImageTk.PhotoImage(file="G+.png")
button11 = Button(frame2, image=im1, bg='#DDA0DD', command=lambda: openn('https://plus.google.com/u/0/?tab=mX'))
button11.grid(row=0, column=0, padx=5, pady=5)

im3 = ImageTk.PhotoImage(file="blogger.png")
button33 = Button(frame2, image=im3, bg='#DDA0DD', command=lambda: openn('https://draft.blogger.com/blogger.g?rinli=1&pli=1&blogID=7909549478613659286#reading'))
button33.grid(row=0, column=1, padx=5, pady=5)

im4 = ImageTk.PhotoImage(file="drive.png")
button44 = Button(frame2, image=im4, bg='#DDA0DD', command=lambda: openn('https://drive.google.com/drive/my-drive'))
button44.grid(row=0, column=2, padx=5, pady=5)

im5 = ImageTk.PhotoImage(file="doc.png")
button51 = Button(frame2, image=im5, bg='#DDA0DD', command=lambda: openn('https://docs.google.com/document/u/0/'))
button51.grid(row=0, column=3, padx=5, pady=5)

im6 = ImageTk.PhotoImage(file="dropbox.png")
button52 = Button(frame2, image=im6, bg='#DDA0DD', command=lambda: search('https://www.dropbox.com/'))
button52.grid(row=0, column=4, padx=5, pady=5)

im7 = ImageTk.PhotoImage(file="evernote.png")
button53 = Button(frame2, image=im7, bg='#DDA0DD', command=lambda: openn('https://www.evernote.com/client/web?login=true#?an=true&n=5da6c198-5c46-4e6b-934c-f820fe1d9ec1&s=s335&'))
button53.grid(row=1, column=0, padx=5, pady=5)

im8 = ImageTk.PhotoImage(file="facebook.png")
button54 = Button(frame2, image=im8, bg='#DDA0DD', command=lambda: openn('https://www.facebook.com/')) 
button54.grid(row=1, column=1, padx=5, pady=5)

im9 = ImageTk.PhotoImage(file="gmail.png")
button55 = Button(frame2, image=im9, bg='#DDA0DD', command=lambda: openn('https://mail.google.com/mail/u/0/#inbox')) 
button55.grid(row=1, column=2, padx=5, pady=5)

im10 = ImageTk.PhotoImage(file="instagram.png")
button65 = Button(frame2, image=im10, bg='#DDA0DD', command=lambda: search('https://www.instagram.com/')) 
button65.grid(row=1, column=3, padx=5, pady=5)

im11 = ImageTk.PhotoImage(file="pinterest.png")
button75 = Button(frame2, image=im11, bg='#DDA0DD', command=lambda: openn('https://www.pinterest.com/')) 
button75.grid(row=1, column=4, padx=5, pady=5)


im12 = ImageTk.PhotoImage(file="reddit.png")
button64 = Button(frame2, image=im12, bg='#DDA0DD', command=lambda: openn('https://www.reddit.com/')) 
button64.grid(row=2, column=0, padx=5, pady=5)

im13 = ImageTk.PhotoImage(file="tvitter.png")
button66 = Button(frame2, image=im13, bg='#DDA0DD', command=lambda: openn('https://twitter.com/')) 
button66.grid(row=2, column=1, padx=5, pady=5)

im14 = ImageTk.PhotoImage(file="Wikipedia.png")
button67 = Button(frame2, image=im14, bg='#DDA0DD', command=lambda: search('https://uk.wikipedia.org/wiki/')) 
button67.grid(row=2, column=2, padx=5, pady=5)

im15 = ImageTk.PhotoImage(file="translate.png")
button67 = Button(frame2, image=im15, bg='#DDA0DD', command=lambda: openn('https://translate.google.com.ua/')) 
button67.grid(row=2, column=3, padx=5, pady=5)

im16 = ImageTk.PhotoImage(file="keep.png")
button67 = Button(frame2, image=im16, bg='#DDA0DD', command=lambda: openn('https://keep.google.com/u/0/')) 
button67.grid(row=2, column=4, padx=5, pady=5)

im17 = ImageTk.PhotoImage(file="github.png")
button67 = Button(frame2, image=im17, bg='#DDA0DD', command=lambda: openn('https://github.com/enterprise')) 
button67.grid(row=3, column=0, padx=5, pady=5)

p2.add(frame1)
p2.add(frame2)
p2.grid(row=3, column=0, padx=4, pady=5)

root.mainloop()
