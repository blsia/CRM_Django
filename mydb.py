import psycopg

conn = None
cursor = None

try:
    # Koneksi awal HARUS ke database 'postgres' (database bawaan)
    conn = psycopg.connect(
        dbname="postgres",             # <-- PASTIKAN INI "postgres", BUKAN "dcrm_db"
        user="postgres",
        password="User", # Ganti dengan password user postgres kamu
        host="127.0.0.1",
        port="5432"
    )
    
    conn.autocommit = True
    cursor = conn.cursor()

    # Perintah SQL untuk membuat database dcrm_db
    cursor.execute("CREATE DATABASE dcrm_db;")
    print("Database 'dcrm_db' berhasil dibuat!")

except Exception as e:
    print(f"Gagal membuat database: {e}")

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()