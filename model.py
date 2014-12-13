import web

db = web.database(dbn='mysql', db='ToDoList', user='root', pw='root')
def get_user(text1,text2):
    if db.where('user', username=text1, password=text2):
      return True
    else:
      return False

def put_user(text1,text2,text3,text4):
    if db.insert('user', fname=text1, lname=text2, username=text3, password=text4):
      return True
    else:
      return False

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())
