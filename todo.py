""" Basic todo list using webpy 0.3 """
import web
import model

web.config.debug = False
global context
### Url mappings

urls = (
    '/', 'Login',
    '/signup', 'Signup',
    '/signup_success','',
    '/index', 'Index',
    '/del/(\d+)', 'Delete',
    '/logout','Logout'
)


### Templates
render = web.template.render('templates', base='base')
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'))


class Login:

    def GET(self):
        return render.login()
        
    def POST(self):
        i=web.input()
        uname=i.uname
        password=i.password
        """Validate username and password"""
        chk=model.get_user(uname,password)
        if chk:
           session.loggedin=True
           session.username=uname
           print "session working fine"+ session.username
           raise web.seeother('/index')
        else:
           print "Invalid"

class Signup:
    
    def GET(self):
        return render.signup()

    def POST(self):        
        i=web.input()
        uname=i.uname
        password=i.password
        """Insert user details"""
        userexists=model.if_user_exists(uname)
        chk=model.put_user(uname,password)
        if chk:
          return render.signup_success()

class Index:
    def GET(self):
        """ Show page """
        todos = model.get_todos()
        usrname=session.username
        session.loggedin=True
        print "session working fine"+usrname
        return render.index(todos, usrname)

    def POST(self):
        """ Add new entry """
        i=web.input()
        newtodo=i.addmore
        usrname=session.username
        print "session working fine"+usrname
        todos = model.get_todos()
        render.index(todos, usrname)
        model.new_todo(newtodo,usrname)
        raise web.seeother('/index')

class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/index')

class Logout:
   def GET(self):
        session.loggedin = False
        session.kill()
        raise web.seeother('/')

app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'username':'','loggedin':False})
    web.config._session = session
else:
    session = web.config._session
if __name__ == '__main__':
    app.run()
