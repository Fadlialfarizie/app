import json
import os


class ProductModel:
    DEFAULT_PATH = 'data/product.json'

    @staticmethod
    def load_product(path=None):
        path = path or ProductModel.DEFAULT_PATH

        try:
            with open(path, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("gagal memuat data produk cek data json")
    
    @staticmethod
    def save_produk_json(data, path=None):
        path = path or ProductModel.DEFAULT_PATH

        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)