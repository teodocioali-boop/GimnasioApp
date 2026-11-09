import os

SECRET_KEY = 'esta_es_una_clave_secreta_super_larga_y_segura_12345'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3307/gimnasio_db?charset=utf8mb4'

# Agrega estas dos líneas:
AUTH_TYPE = 1 
AUTH_ROLE_ADMIN = 'Admin'