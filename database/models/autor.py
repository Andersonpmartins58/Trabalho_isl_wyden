from peewee import Model, CharField
from database.database import db 

class Autor(Model):
    nome = CharField()
    livro = CharField()
    
    class Meta: 
        database = db