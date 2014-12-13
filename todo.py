""" Basic todo list using webpy 0.3 """
import web
import model
import hashlib
web.config.debug = False
global context
### Url mappings

urls = (
    '/', 'Login',
    '/signup', 'Signup',
    '/index', 'Index',
    '/del/(\d+)', 'Delete'
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
        password=hashlib.md5(i.password).hexdigest()
        """Insert user details"""
        userexists=model.if_user_exists(uname)
        if userexists:
          print "User already exists"
        else:
           chk=model.put_user(uname,password)
           if chk:
              print "Signup Successfull!"
              raise web.seeother('/')	
           else:
              print "Signup not successfull"
              return render.signup()

class Index:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, 
            description="I need to:"),
        web.form.Button('Add todo'),
    )
    def GET(self):
        """ Show page """
        todos = model.get_todos()
        form = self.form()
        usrname=session.username
        print "session working fine"+usrname
        return render.index(todos, form, usrname)

    def POST(self):
        """ Add new entry """
        form = self.form()
        usrname=session.username
        print "session working fine"+usrname
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form, usrname)
        model.new_todo(form.d.title)
        raise web.seeother('/')


class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')

app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'username':'','loggedin':False})
    web.config._session = session
else:
    session = web.config._session
if __name__ == '__main__':
    app.run()
