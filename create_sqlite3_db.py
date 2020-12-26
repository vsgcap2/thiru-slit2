import csv, sqlite3
import pandas as pd
#from pathlib import Path
#Path('stksDat.db').touch()

conn = sqlite3.connect("stksDat.db")

df = pd.read_csv('c:/masterHp/vPython/thiru-slit2/stksDat.csv')
df.to_sql('df2', conn, if_exists='append', index=False)

conn.commit
conn.close

cur=conn.cursor()
result=cur.execute('''select * from df2''').fetchall()
len(result)
