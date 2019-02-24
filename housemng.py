from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd525a4aaf7179ce92137d211eab0584b'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} 관리자 등록이 되었습니다.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='관리자등록', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@aaa.com' and form.password.data =='1111':
            flash(f'{form.email.data}님이 로그인 되었습니다.', 'success')
            return redirect(url_for('home'))
        else:
            flash('로그인이 실패했습니다. 메일주소나 비밀번호를 확인하세요.', 'danger')
    return render_template('login.html', title='로그인', form=form)

if __name__ == "__main__":
    app.run(debug=True)