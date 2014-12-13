import web

db = web.database(dbn='mysql', db='ToDoList', user='root', pw='root')
def get_user(text1,text2):
    if db.where('user', username=text1, password=text2):
      return True
    else:
      return False

def put_user(text1,text2):
    
    if db.insert('user', username=text1, password=text2):
      return True
    else:
      return False

def if_user_exists(text1):

    results = db.query("select count(*) from user where username=$uname", vars={'uname':text1})
    if results>0:
       return True
    else:
       return False

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())
