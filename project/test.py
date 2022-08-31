from sqlalchemy import create_engine, inspect
from project.models.shelter import Shelter
from project.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
conn = engine.connect()
inspector = inspect(conn)
print(inspector.get_table_names())
columns = inspector.get_columns("TB_SHELTER_INFO")
for col in columns:
    print(col)

print(Shelter.query.all())