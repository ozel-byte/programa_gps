from tkinter import *
from tkinter import ttk


from leer_archivo import gpgga
root = Tk()
root.title('GPS TAREA')
root
x_ventana = (root.winfo_screenwidth() // 2) - 780 // 2
y_ventana = (root.winfo_screenheight() // 2 ) - 400 // 2
print(x_ventana)
print(y_ventana)
posicion = "780x400"+"+"+str(x_ventana)+"+"+str(y_ventana)
root.geometry(posicion)
frm = ttk.Frame(root)
frm.pack(fill="x")

table = ttk.Treeview(frm,show="headings",height=620)

table['columns'] = ('hrs','latitud','longitud')
table.column("#0",width=0,stretch=NO)
table.column("hrs",anchor=CENTER,width=80)
table.column("latitud",anchor=CENTER,width=80)
table.column("longitud",anchor=CENTER,width=80)

table.heading("#0",text="",anchor=CENTER)
table.heading("hrs",text="Horas",anchor=CENTER)
table.heading("latitud",text="latitud",anchor=CENTER)
table.heading("longitud",text="longitud",anchor=CENTER)

for x in range(0,len(gpgga)):
    hrs = gpgga[x].hrs()
    latitud = gpgga[x].conversion_grados_min_sec_latitud()
    longitud = gpgga[x].conversion_grados_min_sec_longitud()
    table.insert(parent='',index='end',iid=x,text='',values=(hrs,latitud,longitud))
table.pack(fill="x")

root.mainloop()