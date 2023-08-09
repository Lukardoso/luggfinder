from luggfinder.db_models import *
from luggfinder import app
from luggfinder.config import *

from pathlib import Path


PATH = Path("instance", "unittest.db")

DATA = {
        "process": "GVRAD12200",
        "cost": 123.50,
        "date": "09/07/2023",
        "FS": "CNF",
        "name": "KENIA FREITAS",
        "PNR": "GNRBXX",
        "qntBags": 2,
        "RL": 26,
        "type": "AHL",
        "supplier": "Gv Express"
    }



def create_db():
    if PATH.exists():
        PATH.unlink()
        
    with app.app_context():
        db.create_all()


def populate():
    with app.app_context():
        process_1 = Process(
            process = DATA["process"],
            date = DATA["cost"],
            name = DATA["name"],
            pnr = DATA["PNR"],
            number_of_bags = DATA["qntBags"],
            process_type = DATA["type"],
            fault_station = DATA["FS"],
            process_reason = DATA["RL"],
            cost = DATA["cost"],
            supplier = DATA["supplier"]
            )


        db.session.add(process_1)
        db.session.commit()


def query_all():
    with app.app_context():
        q = Process.query.all()

    return q       


def tests(test_name, test):
        try:
            test()
            print(f"{test_name} - Passed")
        except:
            print(f"{test_name} - Failed")



if __name__=="__main__" and app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///unittest.db":
    print("\n--- Running tests now...\n")

    tests("Creating DB", create_db)    
    tests("Populating DB", populate)    
    tests("Querying DB", query_all)    

    print("\n--- All tests are finished.\n")

else:
    print('\nYou are not in development mode!\n')