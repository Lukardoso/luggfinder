from flask import render_template, Blueprint


supplier_bp = Blueprint('supplier', __name__)


@supplier_bp.route('/suppliers/<supplier>')
def home(supplier):

    suppliers_avaible = {"gvexpress"} # Set temporário, estes dados virão do banco de dados

    if supplier in suppliers_avaible:
        return render_template("supplier_pages/supplier.html", title="Supplier")

    else:
        return "Fornecedor não cadastrado"