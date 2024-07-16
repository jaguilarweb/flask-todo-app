# TODO APP

## Description
This is a simple todo app that allows you to add, delete and mark tasks as done.


## Database tips

To reset the database anytime

```bash
dropdb todoapp && createdb todoapp
```


## Migrations

Install Flask-Migrate dependencies:
  
  ```bash
  pip3 install Flask-Migrate
  ```

Import into app.py file.
Then, create an instance:
  
  ```python
  from flask_migrate import Migrate
  migrate = Migrate(app, db)
  ```

To create a migration:
  
  ```bash
  flask db init
  ```
It creates a migrations folder in the project root directory. This folder contains a version table and a migrations

Before to create migration:
    
  ```bash
  dropdb todoapp && createdb todoapp
  ```

To create a migration:
  
  ```bash
  flask db migrate -m "migration message"
  flask db migrate
  ```
