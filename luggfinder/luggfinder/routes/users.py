from luggfinder.db_models import Process, db
from flask import render_template, Blueprint, request, redirect, url_for


user_bp = Blueprint('user', __name__)


@user_bp.route('/user')
def home():
    query = Process.query.all()
    
    return render_template("user_pages/user.html", 
                            title="User", 
                            query=query
                            )


@user_bp.route('/update_process', methods=['POST'])
def update_process():
    json_data = request.get_json()

    for i in json_data:
        update_process = Process.query.filter_by(process=json_data[i]["process"]).first();

        if update_process:
            update_process.date = json_data[i]["date"]
            update_process.name = json_data[i]["name"]
            update_process.pnr = json_data[i]["pnr"]
            update_process.process_type = json_data[i]["process_type"]
            update_process.fault_station = json_data[i]["fault_station"]
            update_process.process_reason = json_data[i]["process_reason"]
            update_process.cost = json_data[i]["cost"]
            update_process.supplier = json_data[i]["supplier"]

            db.session.commit()

    return "received"


# @user_bp.route('/user/new_process')
# def new_process():
#     add_process = Process(
#             process = json_data[i]["process"],
#             date = json_data[i]["date"],
#             name = json_data[i]["name"],
#             pnr = json_data[i]["pnr"],
#             process_type = json_data[i]["process_type"],
#             fault_station = json_data[i]["fault_station"],
#             process_reason = json_data[i]["process_reason"],
#             cost = json_data[i]["cost"],
#             supplier = json_data[i]["supplier"]
#             )

#     db.session.add(add_process)


@user_bp.route('/delete/<process>')
def delete_process(process):
    to_delete = Process.query.filter_by(process=process.upper()).first();
    print(to_delete)
    db.session.delete(to_delete)
    db.session.commit()

    return redirect(url_for('user.home'))