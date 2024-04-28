import tkinter as tk
from AlmacenarDatos import CrearArista

class VentanaCrearArista:
    def __init__(self):
        self.ConfiguracionInicial()
        self.CreandoEspacios()

    def RecibirInstancia(self, instancia):
        self.AlmacenarDatos = instancia
    
    def ConfiguracionInicial(self):
        self.VentanaInterfaz = tk.Tk()
        self.VentanaInterfaz.title("Datos para vértice")
        self.ancho_ventana = 300
        self.alto_ventana = 230
        self.ancho_pantalla = self.VentanaInterfaz.winfo_screenwidth()
        self.alto_pantalla = self.VentanaInterfaz.winfo_screenheight()
        self.posicion_x = (self.ancho_pantalla - self.ancho_ventana) // 2
        self.posicion_y = (self.alto_pantalla - self.alto_ventana) // 2
        self.VentanaInterfaz.geometry(f"{self.ancho_ventana}x{self.alto_ventana}+{self.posicion_x}+{self.posicion_y}")

    def CreandoEspacios(self):
        self.etiqueta_vertice_inicial = tk.Label(master=self.VentanaInterfaz, text="Ingrese el nombre del vértice INICIAL:")
        self.etiqueta_vertice_inicial.pack(padx=20, pady=(20, 0))
        self.campo_vertice_inicial = tk.Entry(master=self.VentanaInterfaz, width=30)
        self.campo_vertice_inicial.pack(padx=20, pady=(0, 10))
        self.etiqueta_vertice_final = tk.Label(master=self.VentanaInterfaz, text="Ingrese el nombre del vértice FINAL:")
        self.etiqueta_vertice_final.pack(padx=20, pady=(20, 0))
        self.campo_vertice_final = tk.Entry(master=self.VentanaInterfaz, width=30)
        self.campo_vertice_final.pack(padx=20, pady=(0, 10))
        self.BotonSubirArchivo = tk.Button(master=self.VentanaInterfaz, text="Agregar arista", command=self.DevolverDatos)
        self.BotonSubirArchivo.pack(padx=20, pady=(20, 0))

    def DevolverDatos(self):
        self.Inicial = self.campo_vertice_inicial.get()
        self.Final = self.campo_vertice_final.get()
        self.AlmacenarDatos.LlenarListaAristas(CrearArista(self.Inicial, self.Final))
        self.VentanaInterfaz.destroy()
        self.VentanaInterfaz.quit()

    def Iniciar(self):
        self.VentanaInterfaz.mainloop()