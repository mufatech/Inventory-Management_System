# routes/add_item.py
from flask import render_template, request, redirect, url_for, flash
from app import app, db, 
from app.models.item import Item
from flask_login import login_user
from datetime import datetime

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        quantity = float(request.form.get('quantity'))
        price = float(request.form.get('price'))

        # Calculate Stock value based on the initial quantity
        stock_value = price * quantity

        new_item = Item(item_name=item_name, quantity=quantity, price=price, stock_value=stock_value)
        db.session.add(new_item)
        db.session.commit()
        
        return redirect(url_for('index')
