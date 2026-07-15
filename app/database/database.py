import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="ai_chatbot",
    user="postgres",
    password="Monika@123"
)

cursor = conn.cursor()