import sqlite3 as lite
import os



class DatabaseManage():

	def __init__(self):

		global con

		path, filename = os.path.split(os.path.abspath(__file__))
		newPath = path+"\\database"
		if not os.path.exists(newPath):
			os.makedirs(newPath)

		try:
			con = lite.connect(newPath+'\\studenttttt.db')
			with con:
				cur = con.cursor()
				cur.execute("CREATE TABLE IF NOT EXISTS Studenttttts(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Class TEXT)")

		except Exception as e:
			print(str(e))

	def insertData(self,name,className):
	
		try:
			with con:
				cur = con.cursor()
				cur.execute("INSERT INTO Studenttttts(Name, Class) VALUES('"+name+"','"+className+"')")

		except Exception as e:
			print(str(e))


	def viewData(self):

		name = []

		try:
			with con:
				cur = con.cursor()
				cur.execute("SELECT * FROM Studenttttts")
				rows = cur.fetchall()
				for row in rows:
					data = str(row[0]) + " - Name : " + str(row[1]) + ", Mobile : " + str(row[2])
					name.append(data)
			return name
		except Exception as e:
			print("Exception in fetching the values : "+str(e))
			
			
	def delData(self,id):
		print(id)
		try:
			with con:
				cur = con.cursor()
				sql = "DELETE FROM Studenttttts WHERE Id = ?"
				cur.execute(sql,[id])
		except Exception as e:
			print(str(e))
			
	def fetchData(self, id):
		data = []
		try:
			with con:
				cur = con.cursor()
				sql = "SELECT * FROM Studenttttts WHERE Id = ?"
				cur.execute(sql,[id])
				rows = cur.fetchall()
				for row in rows:
					current = []
					current.append(row[1])
					current.append(row[2])
					#current.append(row[3])
					data.append(current)
			return data
					
		except Exception as e:
			print("Exception in fetching the values : "+str(e))
			
	def updateData(self, id, name, className):

		try:
			with con:
				cur = con.cursor()
				sql = "UPDATE Studenttttts SET Name = ?, Class = ? WHERE Id = ?"
				cur.execute(sql, [name, className, id])

		except Exception as e:
			print(str(e))
			
			
# 			
# db = DatabaseManage()
# db.viewData()		