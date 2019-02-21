from flask import Flask, render_template, url_for
app = Flask(__name__)

houses = [
    { 
        'house_code' : '201호',
        'house_size' : '9평',
        'room_count' : 1,
        'house_prpt' : '3달(3,4,5) 관리비를 미리 선납함'
    },
    { 
        'house_code' : '202호',
        'house_size' : '10평',
        'room_count' : 2,
        'house_prpt' : '인테리어 안되어 있음'
    },
    { 
        'house_code' : '203호',
        'house_size' : '12평',
        'room_count' : 2,
        'house_prpt' : '현재 세입자가 착함'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', houses=houses)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)