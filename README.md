# FastAPI Movies - [Link to Heroku](https://sdb-fastapi-movies.herokuapp.com/docs)

## Movie Rental

This project consists of a REST API to manage a movie rental system, allowing us to manage films stock and availability,
generate orders for the rented movies and register our customers. Authentication is implemented with JSON Web Tokens,
while permissions are granted based on the user's role. All data is persisted on a PostgreSQL relational database, using
SQLAlchemy as ORM and database migrations were handled with Alembic. CLI commands for generating records with fake data
were added using Typer CLI and Faker.
The application is tested using Pytest, generating a coverage report with a 90.94% coverage. All endpoints and possible
responses are also tested using Postman with its respective collection and test run result.

Extra point:

* Cache (+1 point)
* Add migrations (+1 point)
* Seed ten records per table (+1 point)
* Manage film posters on Amazon S3 (+0.5 point)

### Commands

CLI Commands added with [Typer CLI](https://typer.tiangolo.com/)

    python commands.py populate: populate database with records generated by Faker
    python commands.py clean: wipe database clean of records in most tables

### Migrations

Migrations were managed with [Alembic](https://alembic.sqlalchemy.org/en/latest/)