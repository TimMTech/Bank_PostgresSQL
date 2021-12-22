USE databaseName;               --- Database_name
CREATE TABLE accounts(
                                ID SERIAL PRIMARY KEY,
                                firstname VARCHAR(50) NOT NULL,
                                lastname VARCHAR(50) NOT NULL,
                                phone VARCHAR(15) NOT NULL,
                                email VARCHAR(50) NOT NULL,
                                question VARCHAR(50) NOT NULL,
                                answer VARCHAR(50) NOT NULL,
                                pword VARCHAR(50) NOT NULL,
                                balance DECIMAL(15, 2) NOT NULL
);

INSERT INTO accounts (firstname, lastname, phone, email, question, answer, pword,  \
                            balance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
insert_values = (firstname, lastname, contact, email, question, answer, password, balance)


SELECT * FROM accounts WHERE email=%s and pword=%s

UPDATE accounts SET balance=%s WHERE email=%s

SELECT * FROM accounts ORDER BY id DESC