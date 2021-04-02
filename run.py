import app.app as app
# import app_relay.app as app

if __name__ == "__main__":
    app = app.create_app()
    app.run()