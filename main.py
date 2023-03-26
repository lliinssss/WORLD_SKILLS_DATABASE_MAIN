import psycopg2
connect = psycopg2.connect(dbname="Base", user="postgres", password="secret", host="localhost")
connect.autocommit = True
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Orders(
    id serial PRIMARY KEY,
    name_of_clients varchar(100) NOT NULL REFERENCES name_of_client,
    name_of_manager varchar(100) NOT NULL REFERENCES name,
    name_of_executor varchar(100) NOT NULL REFERENCES name,
    services varchar(100) NOT NULL REFERENCES code_of_service,
    date_of_creating timestamptz NOT NULL,
    date_of_closing timestamptz NOT NULL,
    status bool,
    notes varchar(500),
    total_amount int NOT NULL,
    archive bool,
    category bool
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Clients(
    id serial PRIMARY KEY,
    name_of_client varchar(100) NOT NULL,
    phone varchar(20) NOT NULL,
    b_date data,
    sale float4 
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Services(
    code_of_service PRIMARY KEY,
    name_of_service varchar(100) NOT NULL,
    price_of_service float4 NOT NULL
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Users(
    code_of_employee PRIMARY KEY,
    position varchar(30) NOT NULL,
    name varchar(100) NOT NULL,
    email varchar(100),
    login varchar(100) NOT NULL,
    password varchar(100) NOT NULL,
    phone_of_employee int NOT NULL,
    passport varchar(25) NOT NULL,
    b_date_of_employee date,
    last_entry varchar(30) NOT NULL,
    type_of_entry bool NOT NULL,
    image int
);
""")

