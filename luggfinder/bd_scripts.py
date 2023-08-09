from luggfinder.db_models import *
from luggfinder import app
from luggfinder.config import *



def create_tables():
        db.create_all()


def drop_tables():
        db.drop_all()


def query(table):
    q = table.query.all()

    [print(i) for i in q]

    return q


def clear_table(table):    
    q = query(table)
    
    for i in q:
        db.session.delete(i)
        db.session.commit()
    

# Executtion:
with app.app_context():
    query(Process)
    clear_table(Process)