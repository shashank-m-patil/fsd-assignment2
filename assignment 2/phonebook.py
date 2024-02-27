import sqlite3

con = sqlite3.connect('PhoneBook.db')
c = con.cursor()
#c.execute("CREATE TABLE PhoneDirectory(ID text,name text,phone_number text,Email text)")

data = [
    ('100','Shar','9738835738','shar21ec@cmrit.ac.in'),
    ('101','shashu','84649263645','shap21ec@cmrit.ac.in'),
    ('102','shek','7537463957','shek21ec@cmrit.ac.in'),
    ('103','shik','75375663957','shik21ec@cmrit.ac.in'),
    ('104','shak','7537693957','shak21ec@cmrit.ac.in')

]

#c.executemany("INSERT INTO PhoneDirectory (ID,name,phone_number, Email) VALUES(?,?,?,?)",data)

c.execute("SELECT * FROM PhoneDirectory")
for i in range(0,5):
    print(c.fetchone())
con.commit()
con.close()