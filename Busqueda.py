class BusquedaEnAnchura:
    def __init__(self, instancia, lista, tipo):
        self.AlmacenarDatos = instancia
        self.ListaAristas = lista
        self.TipoBusqueda = tipo
        self.Vertices = []
        self.ListaConexiones = []
        self.NuevasAristas = []
        self.VerticesTotales = []
        self.VerticeAnterior = ""
        self.BuscarTodosLosVertices()

    def BuscarTodosLosVertices(self):
        for i in self.ListaAristas:
            if len(self.Vertices) > 0:
                if i.NombreVerticeInicial not in self.Vertices:
                    self.Vertices.append(i.NombreVerticeInicial)
                if i.NombreVerticeFinal not in self.Vertices:
                    self.Vertices.append(i.NombreVerticeFinal)
            else:
                self.Vertices.append(i.NombreVerticeInicial)
                self.Vertices.append(i.NombreVerticeFinal)
        
        self.Vertices.sort()
        for k in self.Vertices:
            self.VerticesTotales.append(str(k))

        print("Vetices:   " + str(self.Vertices))
        
        self.DefinirConexiones()
        
    def DefinirConexiones(self):
        for i in self.Vertices:
            ListaTemporal = []
            for j in self.ListaAristas:
                if str(i) == str(j.NombreVerticeInicial):
                    ListaTemporal.append(j.NombreVerticeFinal)
                if str(i) == str(j.NombreVerticeFinal):
                    ListaTemporal.append(j.NombreVerticeInicial)
            self.ListaConexiones.append(ConexionVertices(i, ListaTemporal))
        
        if str(self.TipoBusqueda) == "A": 
            self.CrearListaParaGrafoAnchura(str(self.Vertices[0]), None)
        elif str(self.TipoBusqueda) == "P": 
            self.CrearListaParaGrafoProfundidad(self.Vertices[0])



    def BuscarArista(self, vertice):
        for i in self.NuevasAristas:
            if str(i.NombreVerticeInicial) == str(vertice) or str(i.NombreVerticeFinal) == str(vertice):
                return False
        return True 
    
    def BuscarAristaInicial(self, vertice_i, vertice_f):
        for i in self.NuevasAristas:
            if (i.NombreVerticeInicial == vertice_i and i.NombreVerticeFinal == vertice_f) or (i.NombreVerticeInicial == vertice_f and i.NombreVerticeFinal == vertice_i):
                return False 
        return True 
    
    def CrearListaParaGrafoAnchura(self, Vertice_Inicial, Vertice_Anterior):
        print("Algoritmo Anchura")
        VerticeInicial = Vertice_Inicial
        VerticeAnterior = Vertice_Anterior
        print("El vertice inicial es:  " + str(VerticeInicial) + " -- El vertice final es: " + str(VerticeAnterior))
        ListaConexionesTemporal = []
        for conexion in self.ListaConexiones:
            if conexion.Vertice == VerticeInicial:
                for vecino in conexion.Lista:
                    ListaConexionesTemporal.append(vecino)
        ListaConexionesTemporal.sort()
        ListaTemporal = []
        for vecino in ListaConexionesTemporal:
            if self.BuscarAristaInicial(str(VerticeInicial), str(vecino)):
                if self.BuscarArista((str(vecino))):
                    print(VerticeInicial, vecino)
                    self.NuevasAristas.append(CrearNuevasAristas(VerticeInicial, vecino))
                    ListaTemporal.append(str(vecino))
        ListaTemporal.sort()
        for vecino in ListaTemporal:
            VerticeInicial2 = vecino
            ListaConexionesTemporal2 = []
            for conexion in self.ListaConexiones:
                if conexion.Vertice == VerticeInicial2:
                    for vecino in conexion.Lista:
                        ListaConexionesTemporal2.append(vecino)
            ListaConexionesTemporal2.sort()
            for vecino in ListaConexionesTemporal2:
                if self.BuscarArista((str(vecino))):
                    for q in ListaTemporal:
                        if q == VerticeInicial2:
                            Posicion = ListaTemporal.index(q)
                    self.CrearListaParaGrafoAnchura(str(ListaTemporal[int(Posicion)]), str(vecino))
    
    
    def CrearListaParaGrafoProfundidad(self, VerticeInicial, visitados=None):
        if visitados is None:
            visitados = set()

        VerticeInicial = str(VerticeInicial)
        visitados.add(VerticeInicial)

        for conexion in self.ListaConexiones:
            if conexion.Vertice == VerticeInicial:
                Lista = sorted(conexion.Lista)
                for vecino in Lista:
                    vecino = str(vecino)
                    if vecino not in visitados:
                        self.NuevasAristas.append(CrearNuevasAristas(VerticeInicial, vecino))
                        self.CrearListaParaGrafoProfundidad(vecino, visitados)






    
    def DevolverNuevasAristas(self):
        return self.NuevasAristas
    
    def DevolverVertices(self):
        return self.VerticesTotales

    
class ConexionVertices:
    def __init__(self, vertice, lista):
        self.Vertice = vertice
        self.Lista = lista

class CrearNuevasAristas:
    def __init__(self, inicial, final):
        self.NombreVerticeInicial = inicial
        self.NombreVerticeFinal = final