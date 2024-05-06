# İçeri Aktarma
from flask import Flask, render_template,request, redirect
# Veritabanı kütüphanesini içe aktarma
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# SQLite ile bağlantı kurma 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# DB oluşturma
db = SQLAlchemy(app )

#Görev #1. DB tablosu oluşturma











# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    # DB nesnelerini görüntüleme
    # Görev #2. DB'deki nesneleri index.html'de görüntüleme
    

    return render_template('index.html',
                           #kartlar = kartlar

                           )

# Kartla sayfayı çalıştırma
@app.route('/card/<int:id>')
def card(id):
    # Görev #2. Id'ye göre doğru kartı görüntüleme
    

    return render_template('card.html', card=card)

# Sayfayı çalıştırma ve kart oluşturma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Görev #2. Verileri DB'de depolamak için bir yol oluşturma
        




        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
