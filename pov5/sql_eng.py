import psycopg2
from config import host, db_name, user, password


# Функция для создания подключения к базе данных
def create_connection():
    try:
        conn = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        return conn
    except psycopg2.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None


# Функция для выполнения SQL-запроса
def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Запрос успешно выполнен")
    except psycopg2.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")


# Пример использования

# Создаем подключение
connection = create_connection()

if connection:
    # SQL-запрос для создания таблицы
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        position VARCHAR(100)
    )
    '''
    # Выполняем SQL-запрос
    execute_query(connection, create_table_query)

    # SQL-запрос для вставки данных
    insert_data_query = '''
    INSERT INTO employees (name, age, position)
    VALUES ('John Doe', 30, 'Manager'),
           ('Jane Smith', 25, 'Developer'),
           ('Mark Johnson', 35, 'Designer')
    '''
    # Выполняем SQL-запрос
    execute_query(connection, insert_data_query)

    # SQL-запрос для выборки данных
    select_data_query = '''
    SELECT * FROM employees
    '''
    # Выполняем SQL-запрос
    cursor = connection.cursor()
    cursor.execute(select_data_query)
    rows = cursor.fetchall()

    # Выводим результаты выборки
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Position: {row[3]}")

    # Закрываем подключение
    connection.close()
