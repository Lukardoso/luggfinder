from flask import render_template, Blueprint


supplier_bp = Blueprint('supplier', __name__)


@supplier_bp.route('/<supplier>')
def home(supplier):
    return render_template("supplier_pages/supplier.html", title="Supplier")