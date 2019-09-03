
from pymongo import MongoClient 
from odo import odo
import pandas as pd

# https://realpython.com/introduction-to-mongodb-and-python/
# Establish a connection

client = MongoClient('mongodb://localhost:27017') ## Specify the port number

# Create or access a database. By default if the database is not found, it will created

db = client.bankruptcyDB

# insert df into data2009 of 
