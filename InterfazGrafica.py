import customtkinter as ctk
import tkinter
import tkinter as tk
from SolicitarDatosVertice import *
from SolicitarDatosAristas import *
from AlmacenarDatos import *
from Busqueda import *

class InterfazGrafica:
    def __init__(self):
        self.ConfiguracionInicial()
        self.CrearCuadros()
        self.CrearBotones()
        self.dibujar_cuadricula()
        self.AlmacenamientoDeDatos = AlmacenarDatos()

    def ConfiguracionInicial(self):
        self.VentanaInterfaz = ctk.CTk()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        self.VentanaInterfaz.resizable(0, 0)
        self.VentanaInterfaz.title("Grafos")
        self.ancho_ventana = 1200
        self.alto_ventana = 675
        self.ancho_pantalla = self.VentanaInterfaz.winfo_screenwidth()
        self.alto_pantalla = self.VentanaInterfaz.winfo_screenheight()
        self.posicion_x = (self.ancho_pantalla - self.ancho_ventana) // 2
        self.posicion_y = (self.alto_pantalla - self.alto_ventana) // 2
        self.VentanaInterfaz.geometry(f"{self.ancho_ventana}x{self.alto_ventana}+{self.posicion_x}+{self.posicion_y}")

    def CrearCuadros(self):
        self.ContenedorEntrada = ctk.CTkFrame(master=self.VentanaInterfaz, width=450, height=615, corner_radius=10)
        self.ContenedorEntrada.place(x=30, y=30)
        self.TituloEntrada = ctk.CTkLabel(master=self.ContenedorEntrada, text="Grafo original")
        self.TituloEntrada.place(relx=0.5, y=20, anchor="center")
        self.lienzo_entrada = tk.Canvas(self.ContenedorEntrada, width=500, height=690)
        self.lienzo_entrada.place(x=25, y=50)
        self.ContenedorSalida = ctk.CTkFrame(master=self.VentanaInterfaz, width=450, height=615, corner_radius=10)
        self.ContenedorSalida.place(x=720, y=30)
        self.TituloSalida = ctk.CTkLabel(master=self.ContenedorSalida, text="Grafo resultante")
        self.TituloSalida.place(relx=0.5, y=20, anchor="center")
        self.lienzo_salida = tk.Canvas(self.ContenedorSalida, width=505, height=690)
        self.lienzo_salida.place(x=25, y=50)
        self.ContenedorDatos = ctk.CTkFrame(master=self.VentanaInterfaz, width=200, height=350, corner_radius=10)
        self.ContenedorDatos.place(x=500, y=187)
        self.TituloTextBox = ctk.CTkLabel(master=self.ContenedorDatos, text="Vertices                Aristas")
        self.TituloTextBox.place(relx=0.5, y=20, anchor="center")
        self.TextBoxSalida1 = tkinter.Text(self.ContenedorDatos, highlightthickness=0, width=14, height=24, state="disabled")
        self.TextBoxSalida1.place(x=6, y=40)
        self.TextBoxSalida2 = tkinter.Text(self.ContenedorDatos, highlightthickness=0, width=14, height=24, state="disabled")
        self.TextBoxSalida2.place(x=126, y=40)

    def AgregarTextoVertices(self, texto):
        self.TextBoxSalida1.configure(state="normal")
        self.TextBoxSalida1.insert("end", texto)
        self.TextBoxSalida1.configure(state="disabled")

    def AgregarTextoAristas(self, texto):
        self.TextBoxSalida2.configure(state="normal")
        self.TextBoxSalida2.insert("end", texto)
        self.TextBoxSalida2.configure(state="disabled")

    def CrearBotones(self):
        self.BotonAgregarVertice = ctk.CTkButton(master=self.VentanaInterfaz, text="Agregar vertice", corner_radius=5, command=self.ObtenerDatosVertice)
        self.BotonAgregarVertice.place(x=529, y=30)
        self.BotonAgregarArista = ctk.CTkButton(master=self.VentanaInterfaz, text="Agregar arista", corner_radius=5, command=self.ObtenerDatosArista)
        self.BotonAgregarArista.place(x=529, y=80)
        self.BotonLimpiar = ctk.CTkButton(master=self.VentanaInterfaz, text="Limpiar", corner_radius=5, command=self.Limpiar)
        self.BotonLimpiar.place(x=529, y=130)
        self.BotonAnchura = ctk.CTkButton(master=self.VentanaInterfaz, text="Buscar en anchura", corner_radius=5, command=self.AlgoritmoAnchura)
        self.BotonAnchura.place(x=529, y=565)
        self.BotonProfundidad = ctk.CTkButton(master=self.VentanaInterfaz, text="Buscar en profundidad", corner_radius=5, command=self.AlgoritmoProundidad)
        self.BotonProfundidad.place(x=529, y=615)

    def dibujar_cuadricula(self):
        for y in range(0, 700, 50):
            self.lienzo_entrada.create_line(0, y, 500, y, fill="gray")
            self.lienzo_salida.create_line(0, y, 500, y, fill="gray")
            numero_fila = y // 50  # Calcular el número de fila
            if numero_fila == 0:
                self.lienzo_entrada.create_text(20, y + 25, text=str(numero_fila), anchor="w", fill="black")
                self.lienzo_salida.create_text(20, y + 25, text=str(numero_fila), anchor="w", fill="black")
            else:
                self.lienzo_entrada.create_text(20, y + 25, text=str(numero_fila), anchor="w", fill="blue")
                self.lienzo_salida.create_text(20, y + 25, text=str(numero_fila), anchor="w", fill="blue")
        for x in range(0, 500, 50):
            self.lienzo_entrada.create_line(x, 0, x, 700, fill="gray")
            self.lienzo_salida.create_line(x, 0, x, 700, fill="gray")
            numero_columna = x // 50
            if numero_columna != 0:
                self.lienzo_entrada.create_text(x + 25, 15, text=str(numero_columna), anchor="n", fill="red")
                self.lienzo_salida.create_text(x + 25, 15, text=str(numero_columna), anchor="n", fill="red")

    def Limpiar(self):
        self.lienzo_entrada.delete("all")
        self.lienzo_salida.delete("all")
        self.dibujar_cuadricula()
        self.AlmacenamientoDeDatos.VaciarListas()
        self.PosicionVerticeX = 17
        self.PosicionVerticeY = 17
        self.TextBoxSalida1.configure(state="normal")
        self.TextBoxSalida2.configure(state="normal")
        self.TextBoxSalida1.delete(1.0, "end")
        self.TextBoxSalida2.delete(1.0, "end")
        self.TextBoxSalida1.configure(state="disabled")
        self.TextBoxSalida2.configure(state="disabled")

    def LimpiarSalida(self):
        self.lienzo_salida.delete("all")
        self.dibujar_cuadricula()
        
    def ObtenerDatosVertice(self):
        Datos =  VentanaCrearVertice()
        Datos.RecibirInstancia(self.AlmacenamientoDeDatos)
        Datos.Iniciar()
        Nombre, Fila, Columna = self.AlmacenamientoDeDatos.RetornarUltimoVertice()
        self.AgregarVertice(int(Columna), int(Fila), str(Nombre))
        Texto = str(Nombre) + " (" + str(Fila) + ", " + str(Columna) + ")\n"
        self.AgregarTextoVertices(Texto)

    def ObtenerDatosArista(self):
        Datos = VentanaCrearArista()
        Datos.RecibirInstancia(self.AlmacenamientoDeDatos)
        Datos.Iniciar()
        VerticeInicial, VerticeFinal = self.AlmacenamientoDeDatos.RetornarUltimaArista()
        ListaVertices = self.AlmacenamientoDeDatos.RetornarLista()
        for i in ListaVertices:
            if str(i.Nombre) == str(VerticeInicial):
                FilaIncial = i.Fila
                ColumnaInicial = i.Columna
                break
        for j in ListaVertices:
            if str(j.Nombre) == str(VerticeFinal):
                FilaFinal = j.Fila
                ColumnaFinal = j.Columna
                break

        X0 = (int(ColumnaInicial) * 50) + 25
        Y0 = (int(FilaIncial) * 50) + 25
        X1 = (int(ColumnaFinal) * 50) + 25
        Y1 = (int(FilaFinal) * 50) + 25
        
        self.DibujarArista(X0, Y0, X1, Y1)

        Texto = VerticeInicial + " - " + VerticeFinal + "\n"
        self.AgregarTextoAristas(Texto)
    
    def AgregarVertice(self, x, y, nombre):
        X = ((50*x)+17)
        Y = ((50*y)+17)
        self.lienzo_entrada.create_oval(int(X), int(Y), int(X)+15, int(Y)+15, outline="black", fill="black")
        self.lienzo_entrada.create_text(X-5, Y-5, text=nombre, fill="green")

    def DibujarArista(self, x1, y1, x2, y2):
        self.lienzo_entrada.create_line(x1, y1, x2, y2, fill="black", width=5)
    
    def AlgoritmoAnchura(self):
        self.LimpiarSalida()
        ListaAristas = self.AlmacenamientoDeDatos.RetornarListaAristas()
        BuscarEnAnchura = BusquedaEnAnchura(self.AlmacenamientoDeDatos, ListaAristas, "A")
        NuevaLista = BuscarEnAnchura.DevolverNuevasAristas()
        Vertices = BuscarEnAnchura.DevolverVertices()
        ListaDeVertices = self.AlmacenamientoDeDatos.RetornarLista()

        for k in NuevaLista: 
            for l in ListaDeVertices:
                if str(k.NombreVerticeInicial) == str(l.Nombre):
                    ColumnaInicial = l.Columna
                    FilaInicial = l.Fila
            for m in ListaDeVertices:
                if str(k.NombreVerticeFinal) == str(m.Nombre):
                    ColumnaFinal = m.Columna
                    FilaFinal = m.Fila

            X0 = (int(ColumnaInicial) * 50) + 25
            Y0 = (int(FilaInicial) * 50) + 25
            X1 = (int(ColumnaFinal) * 50) + 25
            Y1 = (int(FilaFinal) * 50) + 25
            self.DibujarAristaSalida(X0, Y0, X1, Y1)

        for i in ListaDeVertices:
            if i.Nombre in Vertices:
                self.DibujarVerticeSalida(int(i.Columna), int(i.Fila), str(i.Nombre))

    def AlgoritmoProundidad(self):
        self.LimpiarSalida()
        ListaAristas = self.AlmacenamientoDeDatos.RetornarListaAristas()
        BuscarEnProfundidad = BusquedaEnAnchura(self.AlmacenamientoDeDatos, ListaAristas, "P")
        NuevaLista = BuscarEnProfundidad.DevolverNuevasAristas()
        Vertices = BuscarEnProfundidad.DevolverVertices()
        ListaDeVertices = self.AlmacenamientoDeDatos.RetornarLista()

        for k in NuevaLista:
            for l in ListaDeVertices:
                if str(k.NombreVerticeInicial) == str(l.Nombre):
                    ColumnaInicial = l.Columna
                    FilaInicial = l.Fila
            for m in ListaDeVertices:
                if str(k.NombreVerticeFinal) == str(m.Nombre):
                    ColumnaFinal = m.Columna
                    FilaFinal = m.Fila

            X0 = (int(ColumnaInicial) * 50) + 25
            Y0 = (int(FilaInicial) * 50) + 25
            X1 = (int(ColumnaFinal) * 50) + 25
            Y1 = (int(FilaFinal) * 50) + 25
            self.DibujarAristaSalida(X0, Y0, X1, Y1)

        for i in ListaDeVertices:
            if i.Nombre in Vertices:
                self.DibujarVerticeSalida(int(i.Columna), int(i.Fila), str(i.Nombre))

    def DibujarVerticeSalida(self, x, y, nombre):
        X = ((50*x)+17)
        Y = ((50*y)+17)
        self.lienzo_salida.create_oval(int(X), int(Y), int(X)+15, int(Y)+15, outline="black", fill="blue")
        self.lienzo_salida.create_text(X-5, Y-5, text=nombre, fill="green")

    def DibujarAristaSalida(self, x1, y1, x2, y2):
        self.lienzo_salida.create_line(x1, y1, x2, y2, fill="red", width=5)

    def Iniciar(self):
        self.VentanaInterfaz.mainloop()

Interfaz = InterfazGrafica()
Interfaz.Iniciar()