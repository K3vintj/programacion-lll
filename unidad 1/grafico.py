from tkinter import Button,Label, Frame, Tk

ventana = Tk()
ventana.title("Ejemplo 2 Frames")
ventana.geometry("1000x700")

titulo = Label(ventana, text="facturacion", font=("Arial", 24), bg="gray69")
titulo.pack(side="top", fill="x", pady=10)

frame1 = Frame(ventana, bg="gray31", height=200)
frame1.pack(side="top", fill='x')
frame1.pack_propagate(False)  # Evita que cambie de tamaño

frame2 = Frame(ventana, bg="gray63", height=300)
frame2.pack(side="top", fill='x')
frame2.pack_propagate(False)

frame3 = Frame(ventana, bg="gray31", height=200)
frame3.pack(side="top", fill='x')
frame3.pack_propagate(False)


ventana.mainloop()
