from flask import  Blueprint, jsonify, request, abort
from services.produk_service import get_all_product,get_product_by_name, create_product
from marshmallow import ValidationError
from schemas.product_schema import ProductSchema



bp_produk = Blueprint('produk', __name__, url_prefix='/produk')
schema = ProductSchema()

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
    try:
        produk_valid = schema.load(request.json)
    except ValidationError as e:
        raise ValueError(e.messages)

    new_produk = create_product(produk_valid)

    return jsonify({
        'success' : True,
        'message' : 'produk berhasil ditambahkan',
        'data' : new_produk
    })
    