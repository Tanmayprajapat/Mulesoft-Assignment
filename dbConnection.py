#connection to sqlite3
import sqlite3
conn=sqlite3.connect('movies.db')			#creating database
print("opened database succesfully")
cursor=conn.cursor()



#create table to store movies
conn.execute('''CREATE TABLE MOVIES 
			( ID INT PRIMARY KEY NOT NULL,
			NAME TEXT NOT NULL,
			ACTOR TEXT NOT NULL,
			ACTRESS TEXT NOT NULL,
			YEAR OF RELEASE TEXT NOT NULL,
			DIRECTOR TEXT NOT NULL
			);''')

print("table created succesfully")


#inserting rows into database
cursor.execute("INSERT INTO movies VALUES ('1','Bala','Ayushman Khurana','Bhumi Pednekar','2019','Amar Kaushik')")
cursor.execute("INSERT INTO movies VALUES ('2','War','Hrithik Roshan','Vaani Kapoor','2019','Siddharth Anand')")
cursor.execute("INSERT INTO movies VALUES ('3','Chhichhore','Sushant Singh Rajput','Shraddha Kapoor','2019','Nitesh Tiwari')")
cursor.execute("INSERT INTO movies VALUES ('4','Mission Mangal','Akshay Kumar','Vidya Balan','2019','Jagan Shakti')")
cursor.execute("INSERT INTO movies VALUES ('5','Batla House','John Abraham','Mrunal Thakur','2019','Nikhil Advani')")
cursor.execute("INSERT INTO movies VALUES ('6','Article 15','Ayushman Khurana','Isha Talwar','2019','Anubhav Sinha')")


#select all rows
cursor.execute("SELECT * FROM movies")
print(cursor.fetchall())


#select movies of particular actor
actorName="Ayushman Khurana"
cursor.execute("SELECT * FROM movies WHERE actor=?", (actorName,))
print(cursor.fetchall())

conn.commit()
conn.close()
