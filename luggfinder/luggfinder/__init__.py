from luggfinder.config import *

from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


PATH = Path("instance", "unittest.db")


app = Flask(__name__)
app.config.from_object(Production)
CORS(app)

db = SQLAlchemy(app)


if not PATH.exists():    
    with app.app_context():
        db.create_all()



from luggfinder import db_models
from luggfinder.routes.common import common_bp
from luggfinder.routes.users import user_bp
from luggfinder.routes.suppliers import supplier_bp



app.register_blueprint(common_bp)
app.register_blueprint(user_bp)
app.register_blueprint(supplier_bp)