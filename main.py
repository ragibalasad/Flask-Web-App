from website import create_app

app = create_app()

if __name__ == "__main__":
    # host will set autometically
    app.run(debug=True, host="0.0.0.0")
