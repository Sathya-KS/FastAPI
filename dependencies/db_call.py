import pyodbc
from fastapi import FastAPI
from pydantic import BaseModel


class SQLDatabaseConnection:
    def __init__(self):
        self.SERVER = 'ACER\SQLEXPRESS'
        self.DATABASE = 'practicedb'
        #self.USERNAME = '<username>'
        #self.PASSWORD = '<password>'
        
        #self.connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};'
        #UID={self.USERNAME};PWD={self.PASSWORD}
        
        self.connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};Trusted_Connection=yes'
        self.conn = None
        self.cursor = None
    
    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            print("Connection successful!")
            self.cursor = self.conn.cursor()
            return True
        except Exception as ex:
            print(ex)
            return False
    
    def fetch_employee(self, employee_id):
        try:
            self.cursor.execute(f"SELECT * from employees where EMPLOYEE_ID = {employee_id};")
            row = self.cursor.fetchone()
            print(row)
            return row
        except Exception as ex:
            print(ex)
            return None
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()




from pymongo import MongoClient

class MongoDBConnector:
    def __init__(self):
        self.myclient = MongoClient("mongodb://localhost:27017/")
        #self.db = self.myclient['testdb']
        #self.mycollection = self.db["employee"] 
       

    def connect(self, database_name):
        try:
            self.db = self.myclient[database_name]
            print(f"Connected to database: {database_name}")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def insert_one(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(document)
            print(f"Inserted ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Insert error: {e}")
            return None

    def find_all(self, collection_name,employee_id):
        try:
            collection = self.db[collection_name]
            projection =  {"FIRST_NAME": 1,"PHONE_NUMBER":1, "_id": 0}  
            return list(collection.find({"EMPLOYEE_ID":employee_id},projection))
        except Exception as e:
            print(f"Find error: {e}")
            return None
        

    def delete(self, collection_name,employee_id):
        try:
            collection = self.db[collection_name]
            result = collection.delete_one({"EMPLOYEE_ID":employee_id})
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return None
        
    def update(self, collection_name,employee_id,update_dict):
        try:
            collection = self.db[collection_name]
            result = collection.update_one({"EMPLOYEE_ID":employee_id},{"$set": update_dict})
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return None
 


    def close(self):
        if self.myclient:
            self.myclient.close()
            print("Connection closed.")
            self.myclient = None



