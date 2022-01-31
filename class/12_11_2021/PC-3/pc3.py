"""
Author: Andrei Razvan Oproiu
Date: Mon Jan 31 2022
"""
import sqlite3
import csv

def populate_db_from_csv(file, cursor):
    with open(file, newline='', encoding='utf-8-sig', mode='r') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=' ', quotechar='|'))
        # print(reader)
        for d in reader:
            value = d[0].split(';')
            cursor.execute(f"INSERT INTO familia VALUES ('{value[0]}','{value[1]}','{value[2]}')")
            #print(value[2])
            
def select_by_age(cursor, age):
       data = cursor.execute("SELECT * FROM familia WHERE idade > ?",(str(age),))
       return list(data)
   
def select_by_age_family_name(cursor, age, name):
       data = cursor.execute("SELECT * FROM familia WHERE idade > ? AND apelido = ? ",(str(age),name))
       return list(data)
   
def read_file_error(file):
    try:
        con = sqlite3.connect(file, uri=True)
        print("Ligação efetuada!", con)
    except sqlite3.DatabaseError:
        print("O ficheiro não existe!")
    except Exception as e:
        print("Outra coisa não funcionou!", e)
       
if __name__ == "__main__":
    con = sqlite3.connect("class/12_11_2021/PC-3/teste.db")
    cursor = con.cursor()
    # cursor.execute("CREATE TABLE familia (proprio, apelido, idade)")
    # populate_db_from_csv("class/12_11_2021/PC-3/data.csv", cursor)
    by_age = select_by_age(cursor, 19)
    print(by_age)
    by_age_name =select_by_age_family_name(cursor, 0, "Oproiu")
    print(by_age_name)
    # cursor.execute("INSERT INTO familia VALUES ('2006-01-05','BUY','RHAT')")
    con.commit()
    con.close()
    
    #read_file_error("SDASDASDAs")
    
    print("")
    
    