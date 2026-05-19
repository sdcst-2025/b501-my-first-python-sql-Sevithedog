#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.  A function to create your table has been started, but you
will need to finish it with the correct variables and data types
"""
import sqlite3
file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()
def createTable():
  query = """
  create table if not exists custom(
    id integer primary key autoincrement,
    cnum int,
    name tinytext,
    phone tinytext,
    email tinytext,
    balance real,
    firstvisit, tinytext);"""
  cursor.execute(query)
  query = """
  create table if not exists pets(
  id integer primary key autoincrement,
  petid int,
  name tinytext,
  species tinytext,
  breed tinytext,
  owncnum int);"""
  cursor.execute(query)
  connection.commit()
"""
  query = "PRAGMA table_info(custom);"
  cursor.execute(query)
  results = cursor.fetchall()
  print(results)
  

  query = "PRAGMA table_info(pets);"
  cursor.execute(query)
  results = cursor.fetchall()
  print(results)
"""
def main():
  createTable()
  role = input('Enter 1 to view or search tables\nEnter 2 to edit tables')
  if role == '1':
    choice = input('Enter 1 to view customer table\nEnter 2 to view pet table\nEnter 3 to search customer by id\nEnter 4 to search customer by email\nEnter 5 to search customer by phone\nEnter 6 to search pet by petid:\n')
    if choice == '1':
      #Print customers table
      query = 'select * from custom;'
      cursor.execute(query)
      results = cursor.fetchall()
      for i in results:
        print(i)
    if choice == '2':
      #Print pets table
      query = 'select * from pets;'
      cursor.execute(query)
      results = cursor.fetchall
      for i in results:
        print(i)
    if choice == '3':
      #Search by id
      id = input('Enter id: ')
      query = f'select id == {id} from custom'
      cursor.execute(query)
      results = cursor.fetchall()
      print(results)
    if choice == '4':
      #Search by email
      email = input('Enter email: ')
      query = f'select email == {email} from custom'
      cursor.execute(query)
      results = cursor.fetchall()
      print(results)
    if choice == '5':
      #Search by phone number
      phone = input('Enter phone number: ')
      query = f'select phone == {phone} from custom'
      cursor.execute(query)
      results = cursor.fetchall()
      print(results)
    if choice == '6':
      #Search pets by pet id 
      petid = input('Enter pet id: ')
      query = f'select petid == {petid} from pets'
      cursor.execute(query)
      results = cursor.fetchall()
      print(results)
  elif role == '2':
    username =  input('You need to be an administrator to edit the tables.\nPlease enter your username: ')
    if username == 'Finlay':
      while go == False:
        password = input('Please enter your password: ')
        if password == '.':
          go = True
        else:
          print('Incorrect password')
    if username == 'MrYang':
      while go == False: 
        password = input('Please enter your password: ')
        if password == 'Finlayismyfavouritestudent':
          go == True
        else:
          print('Incorrect password')
    
if __name__ == "__main__":
  main()
