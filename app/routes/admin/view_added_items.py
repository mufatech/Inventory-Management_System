# Import necessary modules
from flask import render_template, request
from app import app
from app.models.item import Item
from flask_login import login_required

# Define a route for viewing added items
@app.route('/view_added_items', methods=['GET'])
@login_required  # Use login_required to ensure only logged-in admins can access this page
def view_added_items():
    # Retrieve the page number from the request, default to 1 if not provided
    page = request.args.get('page', default=1, type=int)

    # Set the number of results per page
    per_page = 15  # You can adjust this to your desired number of results per page

    # Query added items with pagination
    added_items = Item.query.paginate(page=page, per_page=per_page, error_out=False)

    return render_template('admin/view_added_items.html', added_items=added_items)

