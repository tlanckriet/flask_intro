from flask import render_template, redirect, url_for, request, flash
from run import app, db
from app.models import User

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            flash('Username is required!')
            return redirect(url_for('register'))
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        
        if user:
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('User does not exist. Please register first.')
            return redirect(url_for('register'))
    
    return render_template('login.html')
