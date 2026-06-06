from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Real matching products database for generating rows like 1000107093_8.jpg
PRODUCTS_MATRIX = {
    "watches": [
        {
            "name": "Fire-Boltt Gladiator Smartwatch",
            "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
            "amz_p": 1499, "flp_p": 1599, "msh_p": 1349,
            "amz_r": "4.2 ⭐", "flp_r": "4.3 ⭐", "msh_r": "4.0 ⭐",
            "amz_d": "Tomorrow", "flp_d": "In 2 Days", "msh_d": "In 4 Days"
        },
        {
            "name": "Casio Vintage Digital Watch",
            "img": "https://images.unsplash.com/photo-1547996160-81dfa63595aa?w=500",
            "amz_p": 1695, "flp_p": 1715, "msh_p": 1550,
            "amz_r": "4.5 ⭐", "flp_r": "4.4 ⭐", "msh_r": "4.1 ⭐",
            "amz_d": "In 2 Days", "flp_d": "Tomorrow", "msh_d": "In 3 Days"
        },
        {
            "name": "Fastrack Reflex Beat Band",
            "img": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=500",
            "amz_p": 999, "flp_p": 899, "msh_p": 799,
            "amz_r": "3.9 ⭐", "flp_r": "4.0 ⭐", "msh_r": "3.8 ⭐",
            "amz_d": "Tomorrow", "flp_d": "In 3 Days", "msh_d": "In 5 Days"
        }
    ],
    "shoes": [
        {
            "name": "Air Jordan 1 Retro High",
            "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
            "amz_p": 14999, "flp_p": 14250, "msh_p": 15100,
            "amz_r": "4.8 ⭐", "flp_r": "4.7 ⭐", "msh_r": "4.3 ⭐",
            "amz_d": "In 3 Days", "flp_d": "In 2 Days", "msh_d": "In 6 Days"
        },
        {
            "name": "Ultraboost 22 Running Shoes",
            "img": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500",
            "amz_p": 8999, "flp_p": 9499, "msh_p": 8500,
            "amz_r": "4.6 ⭐", "flp_r": "4.5 ⭐", "msh_r": "4.2 ⭐",
            "amz_d": "Tomorrow", "flp_d": "In 2 Days", "msh_d": "In 4 Days"
        },
        {
            "name": "Nike Air Max Casual Sneaker",
            "img": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=500",
            "amz_p": 4500, "flp_p": 4299, "msh_p": 3999,
            "amz_r": "4.3 ⭐", "flp_r": "4.4 ⭐", "msh_r": "4.0 ⭐",
            "amz_d": "In 2 Days", "flp_d": "Tomorrow", "msh_d": "In 3 Days"
        }
    ],
    "shirts": [
        {
            "name": "Dennis Lingo Slim Fit Denim Shirt",
            "img": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500",
            "amz_p": 699, "flp_p": 649, "msh_p": 599,
            "amz_r": "4.1 ⭐", "flp_r": "4.0 ⭐", "msh_r": "3.9 ⭐",
            "amz_d": "Tomorrow", "flp_d": "In 2 Days", "msh_d": "In 3 Days"
        },
        {
            "name": "Roadster Casual Checkered Shirt",
            "img": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500",
            "amz_p": 499, "flp_p": 520, "msh_p": 450,
            "amz_r": "4.0 ⭐", "flp_r": "4.2 ⭐", "msh_r": "3.8 ⭐",
            "amz_d": "In 2 Days", "flp_d": "Tomorrow", "msh_d": "In 4 Days"
        }
    ]
}

@app.route('/api/scrape', methods=['GET'])
def scrape_products():
    query = request.args.get('q', 'watches').lower()
    
    # Matching category selector key logic
    category_key = "watches"
    if "shoe" in query: category_key = "shoes"
    elif "shirt" in query: category_key = "shirts"
    
    # Retrieve complete array matching list of diverse design models
    data_list = PRODUCTS_MATRIX.get(category_key, PRODUCTS_MATRIX["watches"])
    
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
