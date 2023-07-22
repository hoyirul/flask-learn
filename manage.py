from flask import Flask
from config import app, create_connection
from routes import item_bp

# Register blueprint
app.register_blueprint(item_bp, url_prefix='/api')

def test_database_connection():
    try:
        connection = create_connection()
        if connection.is_connected():
            print('Database connection successful.')
            connection.close()
        else:
            print('Database connection failed.')
    except Exception as e:
        print('Error:', str(e))


if __name__ == '__main__':
    test_database_connection()
    app.run(debug=True)
