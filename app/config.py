import os
class Config:
    SQL_ALCHEMY_DATABASE_URI=os.getenv('postgresql://postgres:98521Tds@4444@localhost:5432/myappdb')