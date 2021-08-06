from tkinter import *
from tkinter import ttk
import data

print('data: ' + str(data.data))

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

my_table = ttk.Treeview(window)

 
my_table['columns'] = ('NOMBRE', 'TARJETA', 'DIRECCION')


my_table.column('#0', width=120, minwidth=50)
my_table.column('NOMBRE', anchor=W, width=120)
my_table.column('TARJETA', anchor=W, width=120)
my_table.column('DIRECCION', anchor=W, width=120)


my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
my_table.heading('TARJETA', text='TARJETA', anchor=W)
my_table.heading('DIRECCION', text='DIRECCION', anchor=W)





my_table.pack(pady=20, padx=20)


Nombre= StringVar()
Tarjeta= StringVar()
Direccion = StringVar()
precio = StringVar()

registro = "NAVIPORTANS"

    
def show_users():
    fila = 0 
    print(fila)
    print('data resultado: ' + str(data.data))
    for user in data.data:
        registro = user
        print('variable registro: ' + str(registro))
        title1 = Label(frame_title, 
              text=registro, 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
        title1.place(x=25, y=10)
       
        fila = fila + 1 

def crear_contenido():
   
    nombre = entry_nombre.get()
    tarjeta = entry_tarjeta.get()
    direccion= entry_direccion.get()
  
   
    demo_db = data.MyDatabase()

    demo_db.insert_db(nombre, tarjeta, direccion)
    demo_db.read_db()
    show_users()
    

frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=120)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)


title = Label(frame_navbar, 
              text="Bienvenido",
              font=("Century Gothic", "14"))
title.place(x=250, y=40)


title1 = Label(frame_title, 
              text=registro, 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Envios a cualquier parte del pais.", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=25, y=50)


frame_form = Frame(frame_options, width=350, height=450, bg="black")
frame_form.place(x=25, y=5)
label_nombre = Label(frame_form, 
              text="Nombre completo:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#FA8072")
label_nombre.place(x=30, y=30)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_nombre.place(x=30, y=70)

label_tarjeta = Label(frame_form, 
              text="Número de tarjeta:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#FA8072")
label_tarjeta.place(x=30, y=100)
entry_tarjeta = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_tarjeta.place(x=30, y=140)

label_direccion = Label(frame_form, 
              text="Dirección:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#FA8072")
label_direccion.place(x=30, y=170)
entry_direccion = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_direccion.place(x=30, y=210)


button_agregar = Button(frame_form, text="CREATE/INSERTAR", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_contenido)
button_agregar.place(x=110, y=350)
button_agregar = Button(frame_form, text="READ/LEER", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_contenido)
button_agregar.place(x=120, y=400)

window.mainloop()