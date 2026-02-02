from models.product_model import ProductModel
from errors.handler import NotFoundError



def get_all_product():
    products = ProductModel.load_product()
    return products

def get_product_by_name(name):
    products = get_all_product()
    product = next((i for i in products if i['name'] == name), None)

    if not product:
        raise NotFoundError('produk tidak ditemukan')
    
    return product



def filter_produk_by_name(key_search):
    products = get_all_product()
    filter_produk = list(filter(lambda x: key_search.lower() in x['produk'].lower(), products))

    if not filter_produk:
        raise NotFoundError('produk tidak ditemukan')

    return filter_produk

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