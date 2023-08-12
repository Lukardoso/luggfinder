from luggfinder.db_models import Process, db

from flask import render_template, Blueprint, request
from datetime import datetime


common_bp = Blueprint('common', __name__)

@common_bp.route('/')
def home():
    return render_template("home.html", title="Home")


@common_bp.route('/json/wt', methods=['POST'])
def from_worldtracer():
    json_data = request.get_json()
    data = json_data["mainData"]
    month = json_data["month"]

    if not Process.query.filter_by(process=data["Process"]).first():

        # Adapting data to fit frontend:
        date = datetime.strptime(data["Data"], "%d%b%y").strftime("%Y-%m-%d")
        
        p_type = data["Tipo"]
        if p_type == "Delayed":
            p_type = "AHL"
        elif p_type == "Damaged":
            p_type = "DPR"
        else:
            p_type = ""    
        
        
        add_process = Process(
            process = data["Process"],
            date = date,
            name = data["Nome"].lower() + " " + data["Sobrenome"].lower(),
            pnr = data["PNR"].upper(),
            process_type = p_type,
            fault_station = data["FS"],
            process_reason = data["RL"],
            cost = data["Custo"],
            supplier = ""
        )

        db.session.add(add_process)
        db.session.commit()

    return "\n200 - Ok\n"