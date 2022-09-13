class Grupo():
    
    def __init__(self, id=None, numero = None, id_profesor=None, horario=None, lugar=None,idCurso=None) -> None:
        self.id = id 
        self.numero = numero
        self.id_profesor = id_profesor
        self.horario = horario
        self.lugar = lugar
        self.idCurso= idCurso
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'numero' : self.numero, 
            'id_profesor' : self.id_profesor, 
            'horario':self.horario,
            'lugar':self.lugar,
            'self.idCurso': self.idCurso
        }