import os
from flask import Flask

# Creates the app. Test config loads alternate app configuration.
# Secret key is used in various cryptographic tasks.
# Below the database path is supplied.

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'recatcher.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Checks if all app directiories are present.

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Test app route for shits and giggles. :)

    @app.route('/hello')
    def hello():
        return "Hello, World!"

    # Blueprints are registered below.

    from . import db
    db.init_app(app)

    from . import trap
    app.register_blueprint(trap.bp)

    from . import dashboard
    app.register_blueprint(dashboard.bp)
    
    return app