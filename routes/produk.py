from flask import  Blueprint, jsonify, request
from services.produk_service import get_all_product,filter_produk_by_name, create_product, remove_product
from errors.handler import ValidationError
from utils.jwt_generate import login_required
from schemas.product_schema import ProductSchema






bp_produk = Blueprint('produk', __name__, url_prefix='/produk')
schema = ProductSchema()

@bp_produk.route('/')
def products():
    name = request.args.get('q')
    if name:
        product = filter_produk_by_name(name)
        return jsonify({
            'success' : True,
            'message' : 'get product',
            'data' : product
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
def delete_produk(id):
    
    hapus_produk = remove_product(id)

    return jsonify({
        'success' : True,
        'message' : 'produk berhasil dihapus',
        'data' : hapus_produk
    }), 200