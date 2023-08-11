from luggfinder.db_models import Process, db
from flask import render_template, Blueprint, request


user_bp = Blueprint('user', __name__)


@user_bp.route('/user')
def home():
    query = Process.query.all()
    
    return render_template("user_pages/user.html", 
                            title="User", 
                            query=query)


@user_bp.route('/data_from_user', methods=['POST'])
def data_from_user():
    json_data = request.get_json()

    for i in json_data:
        update_process = Process.query.filter_by(process=json_data[i]["process"]).first();

        update_process.date = json_data[i]["date"]
        update_process.name = json_data[i]["name"]
        update_process.pnr = json_data[i]["pnr"]
        update_process.process_type = json_data[i]["process_type"]
        update_process.fault_station = json_data[i]["fault_station"]
        update_process.process_reason = json_data[i]["process_reason"]
        update_process.cost = json_data[i]["cost"]
        update_process.supplier = json_data[i]["supplier"]

        db.session.commit()

    Process.query.all()

    return "received"
