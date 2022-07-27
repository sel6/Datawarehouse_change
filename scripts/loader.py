import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import pandas as pd

class Warehouse():
    
    def __init__(self):
        pass
        
    def DBConnect(self, dbName=None):
        """
        A function to connect to PostgresSQL database
        """
        p_engine = create_engine("postgresql://root:password@localhost:5432/postgres")
        
        return p_engine
    

    def createTables(self, dbName: str, path: str) -> None:
        """
        A function to create SQL table
        """
        fd = open('schema.sql', 'r')
        readsqlFile = fd.read()
        fd.close()
        p_sqlCommands = readsqlFile.split(';')
        for command in p_sqlCommands:
            try:
        result = p_engine.execute(command)
          except Exception as e:
            print('command skipped: ', command)
            print(e)
          
