CREATE TABLE IF NOT EXISTS Users(
    user_id INT,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff SMALLINT,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS Order_status(
    order_status_id INT,
    status_name VARCHAR(255),
    PRIMARY KEY (order_status_id)
);

CREATE TABLE IF NOT EXISTS Categories(
    category_id INT,
    category_title VARCHAR(255),
    category_description TEXT,
    PRIMARY KEY (category_id)
);

CREATE TABLE IF NOT EXISTS Carts(
    cart_id INT,
    Users_user_id INT,
    subtotal DECIMAL,
    total DECIMAL,
    timestamp TIMESTAMP(2),
    PRIMARY KEY (cart_id),
    FOREIGN KEY (Users_user_id)
        REFERENCES Users(user_id)
);


CREATE TABLE IF NOT EXISTS Orders(
    order_id INT,
    Carts_cart_id INT,
    Order_status_order_status_id INT,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),
    PRIMARY KEY (order_id),
    FOREIGN KEY (Order_status_order_status_id)
        REFERENCES Order_status(order_status_id),
    FOREIGN KEY (Carts_cart_id)
        REFERENCES Carts(cart_id)
);



CREATE TABLE IF NOT EXISTS Products(
    product_id INT,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(45),
    category_id INT,
    PRIMARY KEY (product_id),
    FOREIGN KEY (category_id)
        REFERENCES Categories(category_id)
);

CREATE TABLE IF NOT EXISTS Cart_product(
    carts_cart_id INT,
    products_product_id INT,
    FOREIGN KEY (carts_cart_id)
        REFERENCES Carts(cart_id),
    FOREIGN KEY (products_product_id)
        REFERENCES Products(product_id)
);

