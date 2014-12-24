""" Basic todo list using webpy 0.3 """
import web
import model
import bcrypt

web.config.debug = False
global context
### Url mappings

urls = (
    '/', 'Login',
    '/signup', 'Signup',
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
        userexists=model.if_user_exists(uname)
        if userexists:
           chk=model.get_user(uname)
           for pwd in chk:
               stored_hash = pwd.password
               print ""+stored_hash
           
           if bcrypt.hashpw(password.encode('utf-8'),stored_hash.encode('utf-8')) == stored_hash.encode('utf-8'):
              session.loggedin=True
              session.username=uname
              raise web.seeother('/index')
           else:
              invalidpassword="<div class=\"container\"><h2 class=\"heading\">To Do List</h2><br><img src=\"http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons-256/blue-metallic-orbs-icons-business/078888-blue-metallic-orb-icon-business-thumbs-down.png\" style=\" height:100px; width:100px;\"></img><br><h3 class=\"errormessage\">Password doesn't match with the entered username!</h3><br><a href=\"/\" class=\"heading\">Try to Login again</a></div>"
           return render.base(invalidpassword)
        else:
            return render.login_fail()
           
class Signup:
    
    def GET(self):
        return render.signup()

    def POST(self):        
        i=web.input()
        uname=i.uname
        password=i.password
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password.encode('utf-8'),salt.encode('utf-8'))
        """Insert user details"""
        userexists=model.if_user_exists(uname)
        if userexists:
           return render.signup_fail()
        else:
           chk=model.put_user(uname,password_hashed)
           if not chk:
              return render.signup_success()

class Index:
    def GET(self):
        """ Show page """
        if session.get('loggedin')==True:
           usrname=session.username
           todos = model.get_todos(usrname)
           return render.index(todos, usrname)
        else:
           return web.seeother('/')
    
    def POST(self):
        """ Add new entry """
        i=web.input()
        newtodo=i.addmore
        usrname=session.username
        todos = model.get_todos(usrname)
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
       session.loggedin=False
       session.kill()
       web.seeother('/')

   def POST(self):
       session.loggedin=False
       session.kill()
       return render.login()
   
app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'username':'','loggedin':False})
    web.config._session = session
else:
    session = web.config._session
if __name__ == '__main__':
    app.run()
