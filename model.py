import web

db = web.database(dbn='mysql', db='ToDoList', user='root', pw='root')
def get_user(text1):
    return db.select('users', where="username=$unm", vars={'unm':text1})
    

def put_user(text1,text2):
    if db.insert('users', username=text1, password=text2):
      return True
    else:
      return False

def if_user_exists(text1):
    results = db.query("select count(*) as no_of_sameuser from users where username=$uname", vars={'uname':text1})
    for res in results:
        counter=res.no_of_sameuser

    if counter>0:
       return True
    else:
       return False

def get_todos():
    return db.select('todo', order='id')

def new_todo(text1,text2):
    
    res=db.where('users', username=text2)
    for result in res:
        user=int(result.u_id)
    db.insert('todo', title=text1, u_id=user)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())

