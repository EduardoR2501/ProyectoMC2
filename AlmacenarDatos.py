class AlmacenarDatos:
    def __init__(self):
        self.Vertices = []
        self.Aristas = []
    
    def LlenarLista(self, vertice):
        self.Vertices.append(vertice)

    def RetornarUltimoVertice(self):
        if self.Vertices:
            ultimo_vertice = self.Vertices[-1]
            return ultimo_vertice.Nombre, ultimo_vertice.Fila, ultimo_vertice.Columna
        else:
            return None
        
    def RetornarLista(self):
        return self.Vertices
    
    def LlenarListaAristas(self, Arista):
        self.Aristas.append(Arista)

    def RetornarUltimaArista(self):
        if self.Aristas:
            ultima_arista = self.Aristas[-1]
            return ultima_arista.NombreVerticeInicial, ultima_arista.NombreVerticeFinal
        else:
            return None

    def RetornarListaAristas(self):
        return self.Aristas
    
    def VaciarListas(self):
        self.Vertices = []
        self.Aristas = []

class CrearVertice:
    def __init__(self, nombre, fila, columna):
        self.Nombre = nombre
        self.Fila = fila
        self.Columna = columna

class CrearArista:
    def __init__(self, inicial, final):
        self.NombreVerticeInicial = inicial
        self.NombreVerticeFinal = final