import sqlite3

conn=sqlite3.connect('internetveikals.db')
cursor=conn.cursor()

cursor.execute('''INSERT INTO Produkts (produkts_id, nosaukums, cena, noliktava)VALUES (?,?,?,?)''', (15,'Rieksti DeezNuts', 14.56, 'ir') )
conn.commit()

cursor.execute('SELECT * FROM Pasutijums')
orders=cursor.fetchall()
print('Pasūtījumi:')
for order in orders:
    print(order)



cursor.execute('''SELECT vards,datums,cena,nosaukums,daudzums, cena*daudzums FROM Klients
JOIN Pasutijums ON Klients.klients_id=Pasutijums.klienta_id
JOIN Detalas ON Detalas.Pasutijums_id= Pasutijums.Pasutijums_id
JOIN Produkts ON Produkts.produkts_id=Detalas.produkts_id''')

order_details=cursor.fetchall()
print("\nPasūtījuma detaļas:")
for detail in order_details:
    print(detail)

conn.close()

