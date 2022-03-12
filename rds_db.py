import psycopg2
import pandas as pd 
from config import rds_password

print("connecting")
engine = psycopg2.connect(
    database="unemployment",
    user="postgres",
    password=rds_password,
    host="unemployment.c6erikhiwbbw.us-east-1.rds.amazonaws.com",
    port='5432'
)
print("connected")

sql = "select * from gender limit 10;"
df = pd.read_sql(sql, engine)
print(df)
