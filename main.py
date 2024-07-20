from flask import Flask, render_template_string
import random
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route("/")
def hello_world():
    return '<h1>Selamat Datang di Situs Web Saya!</h1> <a href="/random_fact">View a random fact!</a>, <p><a href="/generate-password">Generator Kata Sandi</a></p>'

@app.route("/about")
def about():
    return """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>Tentang Kami</h1>
            <p>Ini adalah halaman tentang kami. Kami adalah tim yang fantastis!</p>
        </body>
    </html>
    """

facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route('/generate-password')
def generate_password_page():
    password = generate_password()
    return render_template_string('''
        <h1>Kata Sandi Acak Anda:</h1>
        <p>{{ password }}</p>
        <p><a href="/generate-password">Buat Kata Sandi Baru</a></p>
        <p><a href="/">Kembali ke Beranda</a></p>
    ''', password=password)


app.run(debug=True)

