import pandas as pd
from sqlalchemy import create_engine
import pandas as pd

class Warehouse():
    
    def __init__(self):
        pass
        
    def DBConnect(self):
        """
        A function to connect to PostgresSQL database
        """
        p_engine = create_engine("postgresql://root:password@localhost:5432/postgres")
        
        return p_engine
    

    def createTables(self, path: str) -> None:
        """
        A function to create PostgresSQL table
        """
        p_engine = DBConnect()
        fd = open(path, 'r')
        readsqlFile = fd.read()
        fd.close()
        sqlCommands = readsqlFile.split(';')
        for command in sqlCommands:
            try:
                result = p_engine.execute(command)
            except Exception as e:
                print('command skipped: ', command)
                print(e)

    def insert_warehouse(self):
        """
        A function to insert values from dataframe to Postgres Database
        """
        p_engine = DBConnect()
        df = pd.read_csv("extracted.csv")
        df.drop(["Unnamed: 0"], axis=1, inplace=True)
        for _, row in df.iterrows():
            p_sqlQuery = """INSERT INTO elt 
            (track_id, cars, traveled_d, avg_speed, lat, lon,
                        speed, lon_acc, lat_acc, time)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9])
            try:
                p_engine.execute(p_sqlQuery, data)
                print('Data inserted successfully')
            except Exception as e:
                print('Error: ', e)
                

if __name__=="__main__":
    wr = Warehouse()