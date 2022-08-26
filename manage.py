from flask.cli import FlaskGroup
from project import app, db, Shelter

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("add_db")
def add_db():
    db.session.add(Shelter())
    db.session.commit()
    

if __name__ == "__main__":
    cli()