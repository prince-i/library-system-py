import sqlite3

def sqlqueryselecttbl():
    # mainconn() is a connection for sqlite3 database bitcoindb.db
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    # This is to execute to find record from the database using sqlite3
    c.execute("select * from books_table")
    row = c.fetchall()
    conn.rollback()
    # To close database after execute from searchfunction()
    conn.close()
    return row
#print(sqlqueryselecttbl()[0])

def sqlqueryinsertrecord():
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    # this is an insert record execute for insert record function
    c.execute("insert into books_table(Isbn, Title, Author, Borrowed, Borrower) values (?,?,?,?,?)", \
              (23, 'jiego', 'albiemer porte', '5:50', 'moymoy palaboy'))
    print("\nINSERTED DATA SUCCESSFULLY")
    input()
    conn.commit()
    conn.close()

#sqlqueryinsertrecord()
    
def sqlquerytitlesearch(mysearch):
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("select * from books_table where Title=(?)", (mysearch, ))
    result = c.fetchone()
    conn.close()
    return result

#print(sqlquerytitlesearch())

def sqlqueryisbnsearch(mysearch):
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("select * from books_table where Isbn=(?)", (mysearch, ))
    result = c.fetchone()
    conn.close()
    return result
#print(sqlqueryisbnsearch())

def sqlquerysaverecord(*saverec):
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("insert into books_table(Isbn, Title, Borrowed, Author, Borrower) values(?,?,?,?,?)", \
              (saverec[0], saverec[1], saverec[2], saverec[3], saverec[4]))
    conn.commit()
    conn.close()
    
def sqlquerysaveupdateentry(*toupdate):
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("update books_table set Isbn = ?, Title = ?, Author = ?, Borrowed = ?, Borrower = ? where ID = ?", \
              (toupdate[1], toupdate[2], toupdate[3], toupdate[4], toupdate[5], toupdate[0]))
    conn.commit()
    conn.close()
    
def sqlquerycountlastid():
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("select * from books_table order by ID desc limit 1")
    row = c.fetchone()
    conn.commit()
    conn.close()
    return row

def sqlquerycountfirstid():
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("select * from books_table order by ID asc limit 1")
    row = c.fetchone()
    conn.commit()
    conn.close()
    return row

#print(type(sqlquerycountlastid()[0]))


def sqlqueryidsearchset(mysearchid):
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("select * from books_table where Id=(?)", (mysearchid, ))
    result = c.fetchone()
    conn.close()
    return result
#print(sqlqueryidsearchset(49))

def sqlquerydeleterec(todelete):
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("delete from books_table where ID = ?", (todelete,))
    conn.commit()
    conn.close()
    print("\nDELETED SUCCESSFUL, PRESS ENTER TO REFRESH THE RECORD")

#sqlquerydeleterec(53)
        
def autoresetid():
    conn = sqlite3.connect('lms.db')
    c = conn.cursor()
    c.execute("UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'books_table';")
    conn.commit()
    conn.close()
    print("\nreset id")
    
autoresetid()