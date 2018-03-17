from app.instance import create_app, init_db
from config import DevelopmentConfig, ProductionConfig

if __name__ == '__main__':
    import sys
    config = ProductionConfig()
    if '--init-db' in sys.argv:
        init_db(config)
    else:
        app = create_app(config)
        app.run()
