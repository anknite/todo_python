todo_python
===========

Todo list using python backend and web.py

<h2>This is a basic demo of a todo list developed using below technologies:</h2>
<ul>
<li>Python as a backend code</li>
<li>Web.py framework</li>
<li>Mysql as a database</li>
<li>Javascript as a front end code</li>
</ul>

<h3>How to get started with the todo list on your local machine?</h3>
Pre-requisites for your local machine:
<ol>
<li>Python 2.4 and above</li>
<li><a href="http://webpy.org/">Web.py framework</a></li>
<li>Mysql 5.1 and Mysqldb python package using command:sudo apt-get install python-mysqldb</li>
<li>Python bcrypt library for secured password hashing:</li>
<ul>
<ul>
<li>For Ubuntu,use command: sudo apt-get install python-bcrypt</li>
<li>For Windows, download zip file from <a href="https://pypi.python.org/pypi/py-bcrypt-w32/0.2.2">here</li>
</ul>
</ul>
</ol>

Steps:
<ol>
<li>Clone the repo todo_python</li>
<li>Import the todolist.sql in your mysql by these two steps below:<ul>
<li>Create a new database named "todolist"</li>
<li>Then use command: mysql -u [username] -p todolist < todolist.sql</li></ul>
<li>Open model.py, change settings according to your database details in db=web.database(dbn='',db='',user='',pw='')
</li>
<li>Go to your project folder and run todo.py file using command: python todo.py</li>
<li>Copy the url displayed after running previous command</li>
<li>Enter it in your browser and you will get a login and signup window.</li>
<li>And you are READY to START!!!</li>
</ol>

