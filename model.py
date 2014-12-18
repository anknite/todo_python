import web

##Setting for database(edit these with your database details)
##dbn:   database type
##db:    database name 
##user:  username of your mysql
##pw:    password to your mysql

##Connect to  the database
db = web.database(dbn='mysql', db='todolist', user='root', pw='root')

"""Fetch user details"""
def get_user(text1):
    return db.select('users', where="username=$unm", vars={'unm':text1})
    
"""Insert user details"""
def put_user(text1,text2):
    if db.insert('users', username=text1, password=text2):
      return True
    else:
      return False

"""Check if the username already exists"""

def if_user_exists(text1):
    results = db.query("select count(*) as no_of_sameuser from users where username=$uname", vars={'uname':text1})
    for res in results:
        counter=res.no_of_sameuser

    if counter>0:
       return True
    else:
       return False

"""Fetch todo details"""

def get_todos():
    return db.select('todo', order='id')

"""Add new todo"""

def new_todo(text1,text2):
    
    res=db.where('users', username=text2)
    for result in res:
        user=int(result.u_id)
    db.insert('todo', title=text1, u_id=user)

"""Delete a todo"""

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())

