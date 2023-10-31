import psycopg2
from itertools import zip_longest
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Database configuration
DATABASE_CONFIG = {
    'dbname': 'railway',
    'user': 'postgres',
    'password': '*c6Fc-dc53d-d6D-5AFadbeF3AfE**BB',
    'host': 'viaduct.proxy.rlwy.net',
    'port': '17654'
}


# Establish a connection to the database
def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch data from basket_a
    cursor.execute("SELECT * FROM basket_a")
    basket_a_items = cursor.fetchall()

    # Fetch data from basket_b
    cursor.execute("SELECT * FROM basket_b")
    basket_b_items = cursor.fetchall()

    cursor.close()
    conn.close()

    # Assuming you have a template to display the items
    return render_template('index.html', basket_a=basket_a_items, basket_b=basket_b_items)


@app.route('/api/baskets')
def baskets():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch data from basket_a
    cursor.execute("SELECT * FROM basket_a")
    basket_a_items = cursor.fetchall()

    # Fetch data from basket_b
    cursor.execute("SELECT * FROM basket_b")
    basket_b_items = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('baskets.html', basket_a=basket_a_items, basket_b=basket_b_items)


@app.route('/api/update_basket_a', methods=['GET'])
def update_basket_a():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert Cherry into basket_a
        cursor.execute("INSERT INTO basket_a (id, fruit_a) VALUES (5, 'Cherry')")
        conn.commit()

        # Fetch all fruits from basket_a
        cursor.execute("SELECT id, fruit_a FROM basket_a")
        fruits = cursor.fetchall()

        # Generate HTML content to display the fruits
        html_content = """
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Fruit Name</th>
                </tr>
            </thead>
            <tbody>
        """

        for fruit in fruits:
            html_content += f"<tr><td>{fruit[0]}</td><td>{fruit[1]}</td></tr>"

        html_content += "</tbody></table>"

        return html_content

    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()



# @app.route('/api/update_basket_a', methods=['POST'])
# def update_basket_a():
#     data = request.get_json()
#     item_id = data.get('id')  # Assuming you're sending the ID of the item to be updated
#     new_fruit = data.get('fruit_a')
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     try:
#         cursor.execute("UPDATE basket_a SET fruit_a = %s WHERE a = %s", (new_fruit, item_id))
#         conn.commit()
#         return jsonify({"message": "Basket A updated successfully!"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         cursor.close()
#         conn.close()


@app.route('/api/unique', methods=['GET'])
def unique_ele():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Fetch unique fruits from basket_a that are not in basket_b
        cursor.execute("SELECT fruit_a FROM basket_a WHERE fruit_a NOT IN (SELECT fruit_b FROM basket_b)")
        unique_a = cursor.fetchall()

        # Fetch unique fruits from basket_b that are not in basket_a
        cursor.execute("SELECT fruit_b FROM basket_b WHERE fruit_b NOT IN (SELECT fruit_a FROM basket_a)")
        unique_b = cursor.fetchall()

        # Fetch combined unique fruits from both baskets
        cursor.execute("SELECT fruit_a FROM basket_a UNION SELECT fruit_b FROM basket_b")
        combined_unique = cursor.fetchall()

        # Generate HTML content to display the results
        html_content = """
                <table border="1">
                    <thead>
                        <tr>
                            <th>Unique Fruits in Basket A (not in B)</th>
                            <th>Unique Fruits in Basket B (not in A)</th>
                            <th>Combined Unique Fruits</th>
                        </tr>
                    </thead>
                    <tbody>
                """

        for a, b, combined in zip_longest(unique_a, unique_b, combined_unique, fillvalue=("N/A",)):
            html_content += f"<tr><td>{a[0] if a else 'N/A'}</td><td>{b[0] if b else 'N/A'}</td><td>{combined[0]}</td></tr>"

        html_content += "</tbody></table>"

        return html_content

    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()


# @app.route('/api/unique', methods=['GET'])
# def unique_ele():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     try:
#         # Fetch unique items from basket_a that are not in basket_b
#         cursor.execute("SELECT fruit_a FROM basket_a EXCEPT SELECT fruit_b FROM basket_b")
#         unique_from_a = cursor.fetchall()
#
#         # Fetch unique items from basket_b that are not in basket_a
#         cursor.execute("SELECT fruit_b FROM basket_b EXCEPT SELECT fruit_a FROM basket_a")
#         unique_from_b = cursor.fetchall()
#
#         unique_items = [item[0] for item in unique_from_a] + [item[0] for item in unique_from_b]
#         return jsonify({"unique_items": unique_items}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         cursor.close()
#         conn.close()


if __name__ == '__main__':
    app.run()
