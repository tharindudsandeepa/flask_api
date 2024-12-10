import psycopg2

try:
    conn = psycopg2.connect(
        dbname="myappdb",
        user="postgres",
        password="98521Tds@4444",
        host="localhost"
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
