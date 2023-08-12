from luggfinder import db



class User(db.Model):
    re = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"RE: {self.re} | Name: {self.name}"


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name}"


class Process(db.Model):
    process = db.Column(db.String(10), primary_key=True, nullable=False)
    date = db.Column(db.String(10)) # format = yyyy-mm-dd
    name = db.Column(db.String(20))
    pnr = db.Column(db.String(6))
    process_type = db.Column(db.String(3))
    fault_station = db.Column(db.String(3))
    process_reason = db.Column(db.Integer)
    cost = db.Column(db.Float(5)) # format = 00.00
    supplier = db.Column(db.Integer, db.ForeignKey('supplier.id'))

    # Secondary Data:
    address = db.Column(db.String(50))
    city = db.Column(db.String(30))
    cost_approvment = db.Column(db.Boolean, nullable=False, default=False)
    number_of_bags = db.Column(db.Integer)


    def __repr__(self) -> str:
        return f"Process: {self.process} | Name: {self.name} | PNR: {self.pnr}"