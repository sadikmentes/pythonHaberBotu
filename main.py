import tkinter
import feedparser
from tkinter import  *
import webview

def defaultColor():
    btnSonDakika.config(bg="light blue")
    btnDunya.config(bg="light blue")
    btnEkonomi.config(bg="light blue")
    btnTeknoloji.config(bg="light blue")
def clearFrame():
    for  widget in frameHaberler.winfo_children():
        widget.destroy()

def openUrl(event) :
    webview.create_window(event.widget.cget("text"),event.widget.cget("text"))
    webview.start()

def haberEkle(haberler):
    haberCount = 0

    for haber in haberler.entries:
        haberCount =  haberCount + 1
        if haberCount > 2 :
            break

        Label(frameHaberler, bg="light green", text=haber.title, anchor="w", font=my_font, fg="dark blue").pack(
            side=TOP, fill="x")
        lblLink = Label(frameHaberler, bg="green", text=haber.link, anchor="w", font=my_font, fg="blue", cursor="hand2")
        lblLink.pack(side=TOP, fill="x")
        lblLink.bind("<Button-1>", openUrl)
        Label(frameHaberler, bg="green", text="-", anchor="c", font=my_font, fg="green", cursor="hand2").pack(side=TOP,
                                                                                                              fill="x")

def sonDakikaCommand():

   clearFrame()
   defaultColor()
   btnSonDakika.config(bg="blue")
   for url in sonDakikaUrl:
       haberler = feedparser.parse(url)
       haberEkle(haberler)

def dunyaCommand():
    clearFrame()
    defaultColor()
    btnDunya.config(bg="blue")
    for url in dunyaUrl:
        haberler = feedparser.parse(url)
        haberEkle(haberler)

def ekonomiCommand():
    clearFrame()
    defaultColor()
    btnEkonomi.config(bg="blue")
    for url in ekonomiUrl:

        haberler = feedparser.parse(url)
        haberEkle(haberler)

def teknolojiCommand():
    defaultColor()
    clearFrame()
    btnTeknoloji.config(bg="blue")
    for url in teknolojiUrl:
        haberler = feedparser.parse(url)
        haberEkle(haberler)


my_font = "Arial", "14", "bold italic"
window = tkinter.Tk()
window.title("Haber Bot Programı")
window.geometry("1000x600")

frameHaberler = Frame(window,height=600)
frameButton = Frame(window,relief=RAISED,bg="green",bd=2)

btnSonDakika = Button(frameButton,text="Son DAKİKA",font=my_font,bg="white",command=sonDakikaCommand)
btnDunya = Button(frameButton,text="Dünya",font=my_font,bg="white",command=dunyaCommand)
btnEkonomi = Button(frameButton,text="Ekonomi",font=my_font,bg="white",command=ekonomiCommand)
btnTeknoloji= Button(frameButton,text="Teknoloji",font=my_font,bg="white",command=teknolojiCommand)


btnSonDakika.grid(row=0,column=0,sticky="ew",padx=5,pady=15)
btnDunya.grid(row=1,column=0,sticky="ew",padx=5,pady=15)
btnEkonomi.grid(row=2,column=0,sticky="ew",padx=5,pady=15)
btnTeknoloji.grid(row=3,column=0,sticky="ew",padx=5,pady=15)

frameButton.grid(row=0,column=0,sticky ="ns")
frameHaberler.grid(row=0,column=1,sticky ="nsew")

sonDakikaUrl = ["https://www.milliyet.com.tr/rss/rssnew/sondakikarss.xml","https://www.ensonhaber.com/rss/ensonhaber.xml","https://www.gzt.com/rss","https://www.sozcu.com.tr/feeds-son-dakika"]
dunyaUrl = ["https://www.cnnturk.com/feed/rss/dunya/news","https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml","https://feeds.bbci.co.uk/turkce/rss.xml","https://www.mynet.com/haber/rss/kategori/dunya/"]
ekonomiUrl = ["https://www.cnnturk.com/feed/rss/ekonomi/news","https://www.milliyet.com.tr/rss/rssnew/siyasetrss.xml","https://haberglobal.com.tr/rss/ekonomi"]
teknolojiUrl=["https://www.cnnturk.com/feed/rss/bilim-teknoloji/news","https://haberglobal.com.tr/rss/bilim-teknoloji","https://www.mynet.com/haber/rss/kategori/teknoloji/"]
window.mainloop()


