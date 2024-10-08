from app import create_app

app = create_app()  # Create Flask application and MongoDB instance

if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode
