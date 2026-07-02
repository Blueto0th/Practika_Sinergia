# Кейс-задача № 4
# WEB-приложение "Туризм" на Flask + MySQL

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# ---------- Подключение к БД ----------
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='turizm',
            user='root',
            password='5263883'  # 
        )
        return connection
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None

# ---------- Главная страница (список заказов) ----------
@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        return "Ошибка подключения к базе данных"
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT 
            o.id,
            o.order_date,
            o.customer_name,
            o.customer_phone,
            o.total_price,
            o.status,
            h.name AS hotel_name,
            s.name AS service_name
        FROM Orders o
        JOIN Hotels h ON o.hotel_id = h.id
        JOIN Services s ON o.service_id = s.id
        ORDER BY o.order_date DESC
    ''')
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', orders=orders)

# ---------- Добавление нового заказа ----------
@app.route('/add', methods=['POST'])
def add_order():
    customer_name = request.form['customer_name']
    customer_phone = request.form['customer_phone']
    hotel_id = request.form['hotel_id']
    service_id = request.form['service_id']
    total_price = request.form['total_price']
    status = request.form['status']
    
    conn = get_db_connection()
    if conn is None:
        return "Ошибка подключения к базе данных"
    
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Orders 
        (order_date, customer_name, customer_phone, hotel_id, service_id, total_price, status)
        VALUES (CURDATE(), %s, %s, %s, %s, %s, %s)
    ''', (customer_name, customer_phone, hotel_id, service_id, total_price, status))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

# ---------- Удаление заказа ----------
@app.route('/delete/<int:order_id>')
def delete_order(order_id):
    conn = get_db_connection()
    if conn is None:
        return "Ошибка подключения к базе данных"
    
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Orders WHERE id = %s', (order_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

# ---------- Запуск приложения ----------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)