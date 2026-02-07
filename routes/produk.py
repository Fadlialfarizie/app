from flask import  Blueprint, jsonify, request
from services.produk_service import get_all_product,filter_produk_by_name, create_product, remove_product, paginate_produk
from errors.handler import ValidationError
from utils.jwt_generate import login_required, role_required
from schemas.product_schema import ProductSchema



bp_produk = Blueprint('produk', __name__, url_prefix='/produk')
schema = ProductSchema()



@bp_produk.route('/')
def products():
    data_request = request.args
    if data_request:
        product = paginate_produk(data_request)
        return jsonify({
            'success' : True,
            'message' : 'product page',
            'data' : product["data"],
            'pagination' : product['pagination']
        })
    return jsonify({
        'success' : True,
        'message' : 'get product',
        'data' : get_all_product()
    }), 200

@bp_produk.route('/', methods=['POST'])
@login_required
def add_product():
    try:
        produk_valid = schema.load(request.json)
    except ValidationError as e:
        raise ValidationError(e.messages)

    new_produk = create_product(produk_valid)

    return jsonify({
        'success' : True,
        'message' : 'produk berhasil ditambahkan',
        'data' : new_produk
    }), 201

@bp_produk.route('/<int:id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_produk(id):
    
    hapus_produk = remove_product(id)

    return jsonify({
        'success' : True,
        'message' : 'produk berhasil dihapus',
        'data' : hapus_produk
    }), 200