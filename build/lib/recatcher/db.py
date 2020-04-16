import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

# Opens and reads the database.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# Closes the database.
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Erases and recreates the database.
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# As stated above, this creates the CLI command initialising the db.
@click.command('init-db')
@with_appcontext
def init_db_command():
    '''This creates a new database; existing tables will be dropped!'''
    warn = input('Warning! Existing database WILL BE DROPPED. Make sure to back it up before issuing this command.\nType in "y" or "Y" to proceed.\n> ')
    if warn in ['Y', 'y']:
        init_db()
        click.echo('Database erased and (re)created.')
    else:
        pass
        
# Registers the 'init-db' command in app factory.
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)