import json
from datetime import datetime

class Database:

    def __init__(self,db):
        self.db = json.load(open(db))

    def inserir_ponto(self, status):
        self.dia = datetime.now().strftime("%B %Y, %d")
        self.hora = datetime.now().strftime("%H:%M")
        self.id = datetime.now().strftime("%D %H:%M")

        self.novoponto = { self.id: [self.dia, self.hora, status]}

        self.db.update(self.novoponto)

        with open("data.json", "w") as file:
            json.dump(self.db, file)

        print(self.dia, self.hora)
