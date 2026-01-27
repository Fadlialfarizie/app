from flask import  Blueprint, jsonify, request, abort
from services.produk_service import get_all_product,get_product_by_name, create_product


bp_produk = Blueprint('produk', __name__, url_prefix='/produk')


@bp_produk.route('/')
def products():
    name = request.args.get('name')
    if name:
        product = get_product_by_name(name)
        return jsonify({
            'success' : True,
            'message' : 'get product',
            'data' : product
        })
    return jsonify({
        'success' : True,
        'message' : 'get product',
        'data' : get_all_product()
    })

@bp_produk.route('/', methods=['POST'])
def add_product():
    produk = request.json

    if not produk:
        abort(401, 'data request kosong')
    
    new_produk = create_product(produk)

    return jsonify({
        'success' : True,
        'message' : 'produk berhasil ditambahkan',
        'data' : new_produk
    })
    