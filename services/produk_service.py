from models.product_model import ProductModel
from errors.handler import NotFoundError, ValidationError
import math



def get_all_product():
    products = ProductModel.load_product()
    return products

def get_product_by_id(id):
    products = get_all_product()
    product = next((i for i in products if i['id'] == id), None)

    if not product:
        raise NotFoundError('produk tidak ditemukan')
    
    return product



def filter_produk_by_name(key_search):
    products = get_all_product()
    filter_produk = [i for i in products if key_search.lower() in i['produk'].lower()]

    if not filter_produk:
        raise NotFoundError('produk tidak ditemukan')

    return filter_produk



def paginate_produk(data_query):
    products = get_all_product()
    search = data_query.get('search')

    if search:
        products = filter_produk_by_name(search)
    
    sort_key = data_query.get('sort', 'id')

    if sort_key not in products[0]:
        raise ValidationError('sort key tidak valid')
    
    order = data_query.get('order', 'desc')
    reverse = order == 'desc'
    

    products = sorted(products, key=lambda x : x[sort_key], reverse=reverse )

    total_produk = len(products)
    limit = int(data_query.get('limit'))
    page = int(data_query.get('page'))
    
    if not page or not limit:
        raise ValidationError('page/limit kosong')

    if limit < 1 or page < 1:
        raise ValidationError('page/limit tidak boleh kurang dari 1')

    total_page = math.ceil(total_produk/limit)
    start = (page - 1) * limit
    end = start + limit 

    product_page = products[start:end]

    return {
        'data' : product_page,
        'pagination' : {
            'page' : page,
            'limit' : limit,
            'total_page' : total_page
        }
    }




    



def create_product(data_product):
    all_product =get_all_product()
    product = data_product
    if not product:
        raise ValueError('data produk kosong')
    
    required_fields = ('produk', 'harga', 'stok')

    if not all(field in product for field in required_fields):
        raise ValueError('from produk harus lengkap')
    
    if product['harga'] < 0:
        raise ValueError('harga tidak boleh minus')
    
    if product['stok'] < 0:
        raise ValueError('stok tidak boleh minus')
    
    if not all_product:
        id = 1
    else:
        id = max(i['id'] for i in all_product) + 1

    
    new_produk = {
        'id' : id,
        'produk' : product['produk'],
        'harga' : product['harga'],
        'stok' : product['stok']
    }

    all_product.append(new_produk)

    ProductModel.save_produk_json(all_product)
    return new_produk

def remove_product(id):
    products = get_all_product()

    produk_dihapus = get_product_by_id(id)

    delete_produk = list(filter(lambda x: x['id'] != id, products))

    ProductModel.save_produk_json(delete_produk)

    return produk_dihapus

    