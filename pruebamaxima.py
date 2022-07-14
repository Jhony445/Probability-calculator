#Author: Jonathan David Martinez Quistian

from cProfile import label
from cgitb import text
from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
from tkinter import *
import pandas as pd
import numpy as np
from numpy import mean

#ventana
ventana = Tk()
ventana.config(bg='lightgray')
ventana.geometry('1080x500')
ventana.iconbitmap("iconos/calculadora.ico")
ventana.title('Probability calculator')


#ventanas de area de trabajo
ventana.columnconfigure(0, weight = 50)
ventana.rowconfigure(0, weight= 50)
ventana.columnconfigure(0, weight = 1)
ventana.rowconfigure(1, weight= 1)

ventana.columnconfigure(1, weight = 25)
ventana.rowconfigure(0, weight= 50)


#frame area vista
frame1 = Frame(ventana, bg='gray26')
frame1.grid(column=0,row=0,sticky='nsew')
frame2 = Frame(ventana, bg='gray26')
frame2.grid(column=0,row=1,sticky='nsew')

frame3 = Frame(ventana, bg='#6A8B88')
frame3.grid(column=1,row=0,sticky='nsew')
frame4 = Frame(ventana, bg='#09FFCC')
frame4.grid(column=1,row=1,sticky='nsew')

#frame de botones
frame1.columnconfigure(0, weight = 1)
frame1.rowconfigure(0, weight= 1)

frame2.columnconfigure(0, weight = 1)
frame2.rowconfigure(0, weight= 1)
frame2.columnconfigure(1, weight = 1)
frame2.rowconfigure(0, weight= 1)

frame2.columnconfigure(2, weight = 1)
frame2.rowconfigure(0, weight= 1)

frame2.columnconfigure(3, weight = 2)
frame2.rowconfigure(0, weight= 1)

#lado derecho botones
frame4.columnconfigure(0, weight = 1)
frame4.rowconfigure(0, weight= 1)
frame4.columnconfigure(1, weight = 1)
frame4.rowconfigure(0, weight= 1)

frame4.columnconfigure(2, weight = 1)
frame4.rowconfigure(0, weight= 1)

frame4.columnconfigure(3, weight = 2)
frame4.rowconfigure(0, weight= 1)


# Boton para subir el archivo

def openFile():

	file = filedialog.askopenfilename(initialdir ='C:/',
											title='Select a file',
											filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))

	indica['text'] = file
	data_obtained = indica['text']
	try:
		ExcelFile = r'{}'.format(data_obtained)


		df = pd.read_excel(ExcelFile, dtype= {"Numeration": float})

	except ValueError:
		messagebox.showerror('Information', 'Incorrect format')
		return None
	except FileNotFoundError:
		messagebox.showerror('Information', 'Could not read file')
		return None
	pd.read_excel(ExcelFile)

	tabla['column'] = list(df.columns)
	tabla['show'] = "headings"

	for column in tabla['column']:
		tabla.heading(column, text= column)

	df_row = df.to_numpy().tolist()
	for row in df_row:
		tabla.insert('', 'end', values =row)


def clear():
	tabla.delete(*tabla.get_children())


#ver datos label derecho
mediaText = Label(frame3, text ='Datos agrupados', width=20).grid(column=0, row=0, pady=20, padx= 10)

mediaText = Label(frame3, text ='Average: ', width=20).grid(column=0, row=0, pady=20, padx= 10)
ingresa_nombre = Entry(frame3,  width=20, font = ('Arial',12))
ingresa_nombre.grid(column=1, row=0)

mediana = Label(frame3, text ='is: ', width=20).grid(column=0, row=1, pady=20, padx= 10)
ingresa_apellido = Entry(frame3, width=20, font = ('Arial',12))
ingresa_apellido.grid(column=1, row=1)

moda = Label(frame3, text ='is: ', width=20).grid(column=0, row=2, pady=20, padx= 10)
ingresa_edad = Entry(frame3,  width=20, font = ('Arial',12))
ingresa_edad.grid(column=1, row=2)

#tabla y area de la tabla

tabla = ttk.Treeview(frame1 , height=10)
tabla.grid(column=0, row=0, sticky='nsew')
tabla = ttk.Treeview(frame1 , height=10)
tabla.grid(column=0, row=0, sticky='nsew')


#Scrollbar vertical
ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
ladoy.grid(column = 1, row = 0, sticky='ns')

tabla.configure( yscrollcommand = ladoy.set)
#Estilo de la tabla
estilo = ttk.Style(frame1)
estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
estilo.configure(".",font= ('Arial', 14), foreground='black')
estilo.configure("Treeview", font= ('Helvetica', 12), foreground='black',  background='white')
estilo.map('Treeview',background=[('selected', 'lightgray')], foreground=[('selected','black')] )




#Botones
#boton para cargar archivo
boton1 = Button(frame2, text= 'Open', bg='lightgray', command= openFile)
boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)
#boton para ver los datos de archivo
boton2 = Button(frame2, text= 'Delete', bg='lightgray', command= clear)
boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

indica = Label(frame2, fg= 'white', bg='gray26'  )

#boton para calcular los datos del archivo
boton3 = Button(frame4, text= 'Calculate', bg='lightgray')
boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

ventana.mainloop()
