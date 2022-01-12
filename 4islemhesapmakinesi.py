import tkinter as tk

def topla():
    if value1.get().isdigit() and value2.get().isdigit():
        v1 = float(value1.get())
        v2 = float(value2.get())
        sonuc.configure(text=str(v1+v2))

def cikar():
    if value1.get().isdigit() and value2.get().isdigit():
        v1 = float(value1.get())
        v2 = float(value2.get())
        sonuc.configure(text=str(v1-v2))

def carpma():
    if value1.get().isdigit() and value2.get().isdigit():
        v1 = float(value1.get())
        v2 = float(value2.get())
        sonuc.configure(text=str(v1*v2))

def bolme():
    if value1.get().isdigit() and value2.get().isdigit():
        v1 = float(value1.get())
        v2 = float(value2.get())
        sonuc.configure(text=str(v1/v2))

window = tk.Tk()
window.title('Proje Ödevi')
genislik = window.winfo_screenwidth()//2-150
yukseklik = window.winfo_screenwidth()//2-460
window.geometry("300x230+{}+{}".format(genislik, yukseklik))

sonuc = tk.Label(window, text="Sonuc", font="Courier 15 bold", width=30, justify="center")
sonuc.place(x=-35, y=20)
value1=tk.Entry(window, font="Courier 14 bold", width=15, justify="right")
value1.place(x=70, y=50)
value2=tk.Entry(window, font="Courier 14 bold", width=15, justify="right")
value2.place(x=70, y=80)

button1 = tk.Button(window, text="+", font="Courier 14 bold", width=4, command=topla)
button1.place(x=20, y=130)

button2 = tk.Button(window, text="-", font="Courier 14 bold", width=4, command=cikar)
button2.place(x=90, y=130)

button3 = tk.Button(window, text="*", font="Courier 14 bold", width=4, command=carpma)
button3.place(x=160, y=130)

button4 = tk.Button(window, text="/", font="Courier 14 bold", width=4, command=bolme)
button4.place(x=230, y=130)

value1.focus()
window.mainloop()