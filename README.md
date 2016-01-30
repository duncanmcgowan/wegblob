# wegblob

## A self-contained Django blog framework

This is a simple framework that enables anyone to deploy a blog without relying on
an external service, such as Wordpress.

It could also be tweaked to give a simple CMS.

---

## Architecture

**Wegblob** is intended to be simple, and this is reflected in the architecture.

This version uses an SQLite database which manages two tables, detailed below.

The Django SQLite DB driver provides all the connectivity.

Content is added to a nominated directory, by default this is in the STATIC_PATH of the application (it can be anywhere on your filesystem). Content imports a pre-defined layout template, which you can customize.

The front end is Bootstrap. Override stylesheets can be modified so you are in complete control of visuals. This means you write your content pages using standard Bootstrap classes and modify them where required.

The framework, being a standard Django app, provides the usual directory layout; so, views are in the /views folder, templates in /templates, static in /static.

## Setup

A WSGI file is provided in the project folder. Update this to reflect your application name and ensure the application root can be accessed by your web server.

If you're using Apache then you need to add a config file to /etc/httpd/conf.d, ensuring that mod_wsgi is installed. The config file might look like this;

```
Alias /static /home/YOUR_DIR/YOUR_APP/YOUR_APP/static
WSGIScriptAlias / /home/YOUR_DIR/YOUR_APP/YOUR_APP/wsgi.py
WSGIPythonPath /home/YOUR_DIR/YOUR_APP

<Directory /home/YOUR_DIR/YOUR_APP/YOUR_APP/static>
   Require all granted
</Directory>

<Directory /home/YOUR_DIR/YOUR_APP/YOUR_APP>
<Files wsgi.py>
   Require all granted
</Files>
</Directory>

WSGIDaemonProcess YOUR_APP python-path=/home/YOUR_DIR/YOUR_APP:/PATH_TO_YOUR_VIRTUAL_ENV/lib/python2.7/site-packages
WSGIProcessGroup YOUR_APP
```

Set up your app in the usual Django way and off you go!

<a href="https://uk.linkedin.com/in/mcgowanduncan" target="_blank">&copy; Duncan McGowan 2015</a>
