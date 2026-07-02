-- ============================================
-- Кейс-задача № 3
-- База данных «Туризм»
-- ============================================

-- Создаём базу данных
CREATE DATABASE IF NOT EXISTS Turizm;
USE Turizm;

-- ============================================
-- 1. Таблица-справочник: Страны
-- ============================================
CREATE TABLE Countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(3) NOT NULL UNIQUE
);

-- ============================================
-- 2. Таблица-справочник: Города
-- ============================================
CREATE TABLE Cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    FOREIGN KEY (country_id) REFERENCES Countries(id)
);

-- ============================================
-- 3. Таблица-справочник: Отели
-- ============================================
CREATE TABLE Hotels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    address VARCHAR(255),
    stars INT DEFAULT 3 CHECK (stars BETWEEN 1 AND 5),
    city_id INT NOT NULL,
    FOREIGN KEY (city_id) REFERENCES Cities(id)
);

-- ============================================
-- 4. Таблица-справочник: Услуги
-- ============================================
CREATE TABLE Services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

-- ============================================
-- 5. Таблица переменной информации: Заказы
-- ============================================
CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_name VARCHAR(150) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    hotel_id INT NOT NULL,
    service_id INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    status ENUM('новый', 'подтвержден', 'оплачен', 'отменен') DEFAULT 'новый',
    FOREIGN KEY (hotel_id) REFERENCES Hotels(id),
    FOREIGN KEY (service_id) REFERENCES Services(id)
);

-- ============================================
-- Заполняем справочники тестовыми данными
-- ============================================

-- Страны
INSERT INTO Countries (name, code) VALUES
('Россия', 'RU'),
('Турция', 'TR'),
('Египет', 'EG'),
('Италия', 'IT'),
('Испания', 'ES');

-- Города
INSERT INTO Cities (name, country_id) VALUES
('Москва', 1),
('Санкт-Петербург', 1),
('Сочи', 1),
('Стамбул', 2),
('Анталья', 2),
('Каир', 3),
('Шарм-эль-Шейх', 3),
('Рим', 4),
('Венеция', 4),
('Барселона', 5),
('Мадрид', 5);

-- Отели
INSERT INTO Hotels (name, address, stars, city_id) VALUES
('Ritz-Carlton Moscow', 'Тверская ул., 3', 5, 1),
('Астория', 'Большая Морская ул., 39', 4, 2),
('Grand Hotel Polyana', 'Красная Поляна', 4, 3),
('Four Seasons Istanbul', 'Босфор', 5, 4),
('Kempinski Antalya', 'Белек', 5, 5),
('Mena House', 'Каир', 4, 6),
('Rixos Sharm', 'Шарм-эль-Шейх', 5, 7),
('Hilton Rome', 'Рим', 4, 8),
('Danieli Hotel', 'Венеция', 4, 9);

-- Услуги
INSERT INTO Services (name, description, price) VALUES
('Стандартный тур', 'Проживание + завтрак', 50000.00),
('Полный пансион', 'Проживание + 3-разовое питание', 80000.00),
('All Inclusive', 'Всё включено', 100000.00),
('Экскурсия по городу', 'Обзорная экскурсия', 15000.00),
('Трансфер', 'Встреча в аэропорту', 7000.00),
('Страховка', 'Медицинская страховка', 3000.00);

-- ============================================
-- Заполняем таблицу заказов (переменная информация)
-- ============================================

INSERT INTO Orders (order_date, customer_name, customer_phone, hotel_id, service_id, total_price, status) VALUES
('2026-07-01', 'Иванов Иван', '+7(926)123-45-67', 1, 1, 50000.00, 'новый'),
('2026-07-02', 'Петрова Мария', '+7(903)987-65-43', 3, 3, 100000.00, 'подтвержден'),
('2026-07-03', 'Сидоров Алексей', '+7(915)555-33-11', 5, 2, 80000.00, 'оплачен'),
('2026-07-04', 'Козлова Екатерина', '+7(925)111-22-33', 7, 4, 65000.00, 'новый'),
('2026-07-05', 'Михайлов Дмитрий', '+7(916)777-88-99', 8, 1, 50000.00, 'отменен');

-- ============================================
-- Проверочные запросы (для демонстрации)
-- ============================================

-- Показать все заказы с деталями
SELECT 
    o.id AS 'Номер заказа',
    o.order_date AS 'Дата заказа',
    o.customer_name AS 'Клиент',
    h.name AS 'Отель',
    c.name AS 'Город',
    s.name AS 'Услуга',
    o.total_price AS 'Цена',
    o.status AS 'Статус'
FROM Orders o
JOIN Hotels h ON o.hotel_id = h.id
JOIN Cities c ON h.city_id = c.id
JOIN Services s ON o.service_id = s.id
ORDER BY o.order_date;

-- Количество заказов по странам
SELECT 
    cu.name AS 'Страна',
    COUNT(o.id) AS 'Количество заказов'
FROM Orders o
JOIN Hotels h ON o.hotel_id = h.id
JOIN Cities c ON h.city_id = c.id
JOIN Countries cu ON c.country_id = cu.id
GROUP BY cu.name
ORDER BY COUNT(o.id) DESC;