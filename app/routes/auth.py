from flask import redirect,render_template,url_for,request,session,flash,Blueprint
from app.models.user import Users
from app import db
auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=Users.query.filter_by(username=username).first()
        if user and user.password==password:
            session['user']=username
            return redirect(url_for('tasks.view_tasks'))
        else:
             flash("Invalid username or Password",'danger')
    return render_template("login.html")

@auth_bp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        if password!=confirm_password:
            flash("Passwords do not match",'danger')
            
        else:
            user_info=Users(username=username,password=password)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for("auth.login"))

    return render_template("signup.html")