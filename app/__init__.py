"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7ogm4dadc9vlvinpg-a.oregon-postgres.render.com",
        database="todo_77pq",
        user="todo_77pq_user",
        password="ndTMH55vvp7s6vm12BCWUJA74LpGd3CO")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
