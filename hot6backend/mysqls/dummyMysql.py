import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='qzwx1596',  charset='utf8')

cur = conn.cursor()

cur.execute('CREATE DATABASE IF NOT EXISTS tct DEFAULT CHARACTER SET UTF8;')

cur.execute('use tct;')

# cur.execute('INSERT INTO tct.tct_mst (skt_id, cht_id) VALUES(\'1113444\', \'thirduuid\')')

cur.execute('select * from tct_mst where cht_id = \'thirduuid\';')
test=cur.fetchall()
print(test)
for row in test:
    print(row[2])
cur.execute(f'INSERT INTO tct.tct_hst (cht_id, question, answer) VALUES(\'{test[0][2]}\', \'인터랙트팀 직원 알려줘\', \'인터랙트팀 직원은 최수희 인터랙트팀 입니다.\')')

conn.commit()

conn.close()