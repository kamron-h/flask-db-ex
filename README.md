# Flask Fruit Basket App

This Flask application provides an interface to manage two fruit baskets, `basket_a` and `basket_b`. It allows users to view unique fruits in each basket, update the baskets, and view combined unique fruits from both baskets.

## Features

- **Update Basket A**: Adds a new fruit to `basket_a` and displays the unique fruits in comparison to `basket_b`.
- **View Unique Fruits**: Displays the unique fruits of `basket_a` in comparison to `basket_b`, the reverse, and the unique elements of both combined.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone [the-repository-link]
   cd [repository-name]
2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install Required Packages:**:
   ```bash
   pip install -r requirements.txt
4. **Run the Flask App:**:
   ```bash
   export FLASK_APP=app  # On Windows, use `set FLASK_APP=app`
   export FLASK_ENV=development  # On Windows, use `set FLASK_ENV=development`
   flask run

This will start the Flask development server, and the app will be accessible at http://127.0.0.1:5000/.

## Usage
- Update Basket A: Navigate to http://127.0.0.1:5000/api/update_basket_a to add a new fruit to basket_a and view the unique fruits in basket_a compared to basket_b.
- View Unique Fruits: Navigate to http://127.0.0.1:5000/api/unique to view the unique fruits in each basket and the combined unique fruits from both baskets.
