
class Curso():
    
    def __init__(self, id=None, nombre = None, creditos=None, tipologia=None, sede=None) -> None:
        self.id = id 
        self.nombre = nombre
        self.creditos = creditos
        self.tipologia = tipologia
        self.sede = sede
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'nombre' : self.nombre, 
            'creditos' : self.creditos, 
            'tipologia':self.tipologia,
            'sede':self.sede
        }
        
        