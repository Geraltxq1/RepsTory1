from tkinter import *

def suma(): #Funcion para la operacion de suma 
    numero1 = int(txt1.get()) # Obtener el valor del primer entry
    numero2 = int(txt2.get()) # Obtener el valor del segundo entry
    suma = numero1 + numero2
    return total.set(suma) # Retorna el resultado en el entry total

def resta(): 
    Num1 = int(txt1.get())
    Num2 = int(txt2.get() )
    resta = Num1 - Num2    
    return  total.set(resta)

def multi():
    Num1 = int(txt1.get())
    Num2 = int(txt2.get())
    multi = Num1 * Num2
    return total.set(multi)

def mod ():
    Num1 = int(txt1.get())
    Num2 = int(txt2.get())    
    mod = Num1 / Num2
    return total.set(mod)


#Inicializacion de la ventana 
ventana = Tk() # Se inicializa el marco del obtejo o ventana
ventana.title("Calculadora Clasica") # Titulo de la Ventana 
ventana.geometry("500x500") # Tamaño de la ventana 
ventana.resizable(False,False) # Que no se pueda modificar el tamaño de la ventana 
ventana.config(bg="Orange") # Color de fondo de la ventana

#Definicion de etiquetas 
lbl1 = Label (ventana, text = "Numero 1:", bg="gray", font=("arial"))
lbl1.pack(padx=5,pady=3, ipadx=5, ipady=5, fill= X) # Posicion de la etiqueta 

# Ipad para comodar el texto dentro del label 
#Identificacion del priemer entry
txt1 = Entry(ventana, font=("arial", 12))
txt1.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

#Definicion de etiquetas 
lbl2 = Label (ventana, text = "Numero 2:", bg="gray", font=("arial"))
lbl2.pack(padx=5,pady=3, ipadx=5, ipady=5, fill= X) # Posicion de la etiqueta 

# Ipad para comodar el texto dentro del label 
#Identificacion del priemer entry
txt2 = Entry(ventana, font=("arial", 12))
txt2.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)




btnmod = Button(ventana, text= "Dividir", bg= "yellow", font = ("Arial", 12), command= mod) 
btnmod .pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

btnmulti = Button(ventana, text= "Multiplicar", bg= "yellow", font = ("Arial", 12), command= multi) 
btnmulti.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

btnrestar = Button(ventana, text= "Restar", bg= "yellow", font = ("Arial", 12), command= resta) 
btnrestar.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

btnsumar = Button(ventana, text= "Sumar", bg = "yellow", font = ("Arial",12), command =suma)
btnsumar.pack(padx=5, pady=3, ipadx=5, ipady=5, fill=X)

# Tomar dimensiones del boton, acomodar en la venrana el texto en la caja 

# Label y ENtry para el resultado
lblresult = Label(ventana, text= "Total:", bg = "lightblue",fg = "red", font = ("arial",12))

total = StringVar() # Variable para el resultado

txtresult = Entry (ventana, state = "disable", font =("arial",12), textvariable=total)
txtresult.pack(padx=5, pady=3, ipadx=10, ipady=10, fill=X)
ventana.mainloop() #Cierre de la ventana Principal



