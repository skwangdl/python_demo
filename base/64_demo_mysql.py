import mysql.connector

def demo_mysql():
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) PRIMARY KEY , NAME VARCHAR (20))')
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    demo_mysql()