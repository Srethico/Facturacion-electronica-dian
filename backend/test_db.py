from app.db.session import engine

with engine.connect() as conn:
    print("😎♠️ Conexión exitosa a PostgreSQL")
