from luggfinder.db_models import Process, db
from flask import render_template, Blueprint


user_bp = Blueprint('user', __name__)


@user_bp.route('/user')
def home():
    query = Process.query.all()
    suppliers = ["", "GvExpress", "Três Company", "Voucher"]

    return render_template("user_pages/user.html", 
                            title="User", 
                            query=query,
                            suppliers=suppliers)