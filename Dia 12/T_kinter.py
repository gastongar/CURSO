from tkinter import *
from tkinter import Label


operador = ''

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar ():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado= str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


#iniciar tkinter

aplicacion =Tk()

#tamaño de la ventana
aplicacion.geometry('1320x630+0+0')

#evitar maximizar
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title("Dia 12-Facturacion")
#color de fondo
aplicacion.config(bg='burlywood1')


#panel superior

panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

#panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel Costos
panel_costos = Frame(panel_izquierdo, bd=1 , relief=FLAT, bg='azure4',padx=40)
panel_costos.pack(side=BOTTOM)

#panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text="COMIDA", font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="BEBIDAS", font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text="BEBIDAS", font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

#PANEL DERECHA
panel_derecha= Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()


# lista de prductos
lista_comidas = ['pollo','cordero','salmon','merluza','kebab','pizza1','pizza2','asado']
lista_bebidas = ['agua','soda','coca','vino_tinto','vino_blanco','birra','porron','fanta']
lista_postres = ['helado','frutas','torta','flan','pastel1','pastel2','budin','panqueque']


#Generar item comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador=0
for comida in lista_comidas:

    #crear Checkbutton

    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)


    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)


    contador +=1

#Generar item bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador=0
for bebida in lista_bebidas:



    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador] )
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)



    contador +=1




#Generar item postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador=0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador] )
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)





    contador +=1

#VARIABLES
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de Costos y Campos de Entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg= 'azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0, padx=41)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd= 1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1, padx=41)


etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg= 'azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0, padx=41)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd= 1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12, 'bold'),
                              bg= 'azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0, padx=41)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd= 1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1, padx=41)


etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg= 'azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2, padx=41)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd= 1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=41)

etiqueta_impuesto = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg= 'azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1, column=2, padx=41)

texto_impuesto = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd= 1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg= 'azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2, padx=41)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd= 1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3, padx=41)




## BOTONES
botones = ['total','recibo','guardar', 'resetear']
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold' ),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    boton.grid(row=0,
               column=columnas)
    columnas += 1


# PANEL RECIBO
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold' ),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)



#CALCULADORA
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7','8','9','+',
                       '4','5','6','-',
                       '1','2','3','x',
                       'CE','BORRAR','0','/']

botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg= 'azure4',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)


    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1

    columna +=1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))





#evitar que la pantalla se cierre
aplicacion.mainloop()

