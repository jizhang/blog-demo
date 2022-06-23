SQLALCHEMY_DATABASE_URI = 'sqlite:///nasa.db'
SQLALCHEMY_BINDS = {
    'user_db': 'sqlite:///nasa-user.db',
    'product_db': 'sqlite:///nasa-product.db'
}
SQLALCHEMY_ECHO = True
