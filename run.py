from app.instance import create_app, init_db
from config import Config


if __name__ == '__main__':
    import sys
    config = Config()
    if '--init-db' in sys.argv:
        init_db(config)
    else:
        app = create_app(config)
        app.run(host='127.0.0.1', port=5000)
