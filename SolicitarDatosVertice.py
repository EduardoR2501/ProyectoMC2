import tkinter as tk
from AlmacenarDatos import CrearVertice

class VentanaCrearVertice:
    def __init__(self):
        self.ConfiguracionInicial()
        self.CreandoEspacios()

    def RecibirInstancia(self, instancia):
        self.AlmacenarDatos = instancia
    
    def ConfiguracionInicial(self):
        self.VentanaInterfaz = tk.Tk()
        self.VentanaInterfaz.title("Datos para vértice")
        self.ancho_ventana = 300
        self.alto_ventana = 350
        self.ancho_pantalla = self.VentanaInterfaz.winfo_screenwidth()
        self.alto_pantalla = self.VentanaInterfaz.winfo_screenheight()
        self.posicion_x = (self.ancho_pantalla - self.ancho_ventana) // 2
        self.posicion_y = (self.alto_pantalla - self.alto_ventana) // 2
        self.VentanaInterfaz.geometry(f"{self.ancho_ventana}x{self.alto_ventana}+{self.posicion_x}+{self.posicion_y}")

    def CreandoEspacios(self):
        self.etiqueta_nombre = tk.Label(master=self.VentanaInterfaz, text="Ingrese el nombre del vértice:")
        self.etiqueta_nombre.pack(padx=20, pady=(20, 0))
        self.campo_nombre = tk.Entry(master=self.VentanaInterfaz, width=30)
        self.campo_nombre.pack(padx=20, pady=(0, 10))

        self.etiqueta_fila = tk.Label(master=self.VentanaInterfaz, text="Ingrese la fila del vértice:")
        self.etiqueta_fila.pack(padx=20, pady=(20, 0))
        self.campo_fila = tk.Entry(master=self.VentanaInterfaz, width=30)
        self.campo_fila.pack(padx=20, pady=(0, 10))

        self.etiqueta_columna = tk.Label(master=self.VentanaInterfaz, text="Ingrese la columna del vértice:")
        self.etiqueta_columna.pack(padx=20, pady=(20, 0))
        self.campo_columna = tk.Entry(master=self.VentanaInterfaz, width=30)
        self.campo_columna.pack(padx=20, pady=(0, 10))

        self.BotonSubirArchivo = tk.Button(master=self.VentanaInterfaz, text="Agregar vértice", command=self.DevolverDatos)
        self.BotonSubirArchivo.pack(padx=20, pady=(20, 0))

    def DevolverDatos(self):
        self.nombre = self.campo_nombre.get()
        self.fila = self.campo_fila.get()
        self.columna = self.campo_columna.get()
        self.AlmacenarDatos.LlenarLista(CrearVertice(self.nombre, self.fila, self.columna))
        self.VentanaInterfaz.destroy()
        self.VentanaInterfaz.quit()

    def Iniciar(self):
        self.VentanaInterfaz.mainloop()