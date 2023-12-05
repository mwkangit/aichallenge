import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='qzwx1596',  charset='utf8')

cur = conn.cursor()

cur.execute('CREATE DATABASE IF NOT EXISTS tct DEFAULT CHARACTER SET UTF8;')

cur.execute('use tct;')

# cur.execute('CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(20), birthYear int)')

# cur.execute('INSERT INTO userTable VALUES( \'hong\' , \'홍지윤\' , \'hong@naver.com\' , 1996)')
# cur.execute('INSERT INTO userTable VALUES( \'kim\' , \'김태연\' , \'kim@daum.net\', 2011)')
# cur.execute('INSERT INTO userTable VALUES( \'star\' , \'별사랑\' , \'star@paran.com\' , 1990)')
# cur.execute('INSERT INTO userTable VALUES( \'yang\' , \'양지은\' , \'yang@gmail.com\' , 1993)')
cur.execute('CREATE TABLE IF NOT EXISTS tct_mst (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, skt_id INT NOT NULL, cht_id varchar(255) NOT NULL UNIQUE, last_update_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, creation_time DATETIME DEFAULT CURRENT_TIMESTAMP);')

cur.execute('CREATE TABLE IF NOT EXISTS tct_hst (id INT AUTO_INCREMENT PRIMARY KEY, cht_id varchar(255) NOT NULL, question VARCHAR(1000) NOT NULL, answer VARCHAR(2000) NOT NULL, creation_time DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (cht_id) REFERENCES tct_mst(cht_id));')


# ALTER 컬럼 
# cur.execute('ALTER TABLE tct.tct_mst ADD COLUMN skt_id INT NOT NULL;')

# cur.execute('ALTER TABLE tct.tct_mst MODIFY COLUMN skt_id INT AFTER id;')

# UPDATE 데이터
# cur.execute('UPDATE tct.tct_mst SET skt_id=1113444 where id=3')

conn.commit() 

conn.close()