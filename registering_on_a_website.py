start = int(input("Hello! Welcome to website.com, please press 1 to register"))

if start == 1:

    username = input("Please create a username:")

    password = input("Please create a password:")

    email = input("Please use an email:")

login = int(input("Please press 1 to login"))

if login == 1:

    conf_username = input("please input your username here:")

    while conf_username != username:
        conf_username = input("please input your username here:")


    conf_password = input("please input your password here:")

    while conf_password != password:
        conf_password = input("please input your password here:")



if conf_password == password and conf_username == username:
    print("Hello welcome to website.com!! There are very few things you can do on this website so have fun.")


