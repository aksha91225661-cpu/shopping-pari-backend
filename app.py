from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/scrape', methods=['GET'])
def scrape_products():
    query = request.args.get('q', 'watches').lower().strip()
    
    # Dynamic lines matching list generator (Line 1, Line 2, Line 3, Line 4)
    results = []
    
    # 4 distinct variants for different rows
    variants = [
        {"suffix": "Premium Stealth Edition", "price_mult": 1.2},
        {"suffix": "Classic Retro Design", "price_mult": 0.95},
        {"suffix": "Sport Ultra Lightweight", "price_mult": 0.75},
        {"suffix": "Casual Multi-Color Pack", "price_mult": 0.55}
    ]

    # Keyword-based high quality public images setup to avoid broken elements
    img_map = {
        "bottle": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500",
        "watch": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
        "shoe": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
        "shirt": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500",
        "phone": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500",
        "saree": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=500",
        "glass": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=500"
    }

    # Find closest match img key loop
    selected_img = "https://images.unsplash.com/photo-1536935338788-846bb9981813?w=500" # General global item photo
    for key, url in img_map.items():
        if key in query:
            selected_img = url
            break

    # Build response format matrix rows
    for i, var in enumerate(variants):
        base_val = random.randint(450, 1200) * var["price_mult"]
        p_name = f"{query.capitalize()} {var['suffix']}"

        # Randomize one site availability logic conditionally to mock "Not Available" seamlessly if required
        is_meesho_avail = True if i != 3 else False 

        row_data = {
            "name": p_name,
            "img": selected_img,
            "amz_p": int(base_val * 1.10),
            "flp_p": int(base_val * 0.98),
            "msh_p": int(base_val * 0.88) if is_meesho_avail else 0, # 0 means Not Available
            "amz_r": f"{round(4.1 + (i*0.1), 1)} ⭐",
            "flp_r": f"{round(4.0 + (i*0.1), 1)} ⭐",
            "msh_r": f"{round(3.8 + (i*0.1), 1)} ⭐",
            "amz_d": "Tomorrow",
            "flp_d": "In 2 Days",
            "msh_d": "In 3-5 Days"
        }
        results.append(row_data)

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
