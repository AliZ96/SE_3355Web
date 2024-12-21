from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# Veritabanı modeli
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
   

@app.context_processor
def inject_categories():
    category_counts = {category: Product.query.filter_by(category=category).count() for category in ["Televizyon", "Tablet", "Laptop", "Monitör", "Kulaklık"]}
    return dict(category_counts=category_counts)

@app.route('/')
def home():
    featured_products = []
    for category in ["Televizyon", "Tablet", "Laptop", "Monitör", "Kulaklık"]:
        products_in_category = Product.query.filter_by(category=category).all()
        if products_in_category:
            featured_products.extend(random.sample(products_in_category, min(len(products_in_category), 2)))
    return render_template('home.html', featured_products=featured_products)

@app.route('/category/<category_name>')
def category(category_name):
    category_products = Product.query.filter_by(category=category_name).all()
    return render_template('category.html', category_name=category_name, products=category_products)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    search_results = []
    if query:
        search_results = Product.query.filter(
            Product.name.ilike(f'%{query}%') |  # Ürün ismi
            Product.description.ilike(f'%{query}%') |  # Ürün açıklaması
            Product.city.ilike(f'%{query}%') |  # Şehir adı
            Product.category.ilike(f'%{query}%') |  # Kategori
            db.cast(Product.price, db.String).ilike(f'%{query}%')  # Fiyat kısmî eşleşme
        ).all()
    return render_template('search.html', search_results=search_results, query=query)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
