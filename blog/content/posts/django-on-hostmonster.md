author: Caleb Madrigal
comments: true
date: 2012-02-21 00:05:37
layout: post
slug: django-on-hostmonster
title: Django on Hostmonster
wordpress_id: 102
category: django
tags: django, python

I just finished going through the process of installing and configuring Django (with FastCGI) on Hostmonster's Shared hosting. It was more painful than I expected, so I decided write a post about how I got it working...


First, I wanted to create a subdomain which would host my django stuff. In order to do this, I created a subdomain using the cPanel (the item is called "Subdomains"). This created the directory and a basic .htaccess file (along with a few error pages).

I then went through the basic processes described on these pages:



	
  * [http://www.infoinfoc.us/django/hostmonster](http://www.infoinfoc.us/django/hostmonster)

	
  * [http://www.techgeekguy.com/2011/01/how-to-install-python-svn-django-osqa-web-hosting-server-hostmonster-dreamhost-bluehost-godaddy-hostgator/](http://www.techgeekguy.com/2011/01/how-to-install-python-svn-django-osqa-web-hosting-server-hostmonster-dreamhost-bluehost-godaddy-hostgator/)


When I finished these guides, I kept getting a 500 error. I eventually found that I can access the error log through cPanel (maybe there is a more direct way?). Then I went through and fixed error by error.  Hostmonster's helpdesk has a great [Troubleshooting Django](https://my.hostmonster.com/cgi/help/585) page which was helpful once the error log started showing python-related errors.

So after all this pain, I finally got it working.  I now present to you my basic setup:

**Directory structure:**

    
    
    /home4/questiq1/
    |
    |-- django/
    |   |-- django_src/
    |   |-- django_projects/
    |   |   |-- mysite/
    |   |   |   |-- manage.py
    |   |   |   |-- mysite/
    |   |   |   |   |-- __init__.py
    |   |   |   |   |-- settings.py
    |   |   |   |   |-- urls.py
    |   |   |   |   |-- wsgi.py
    |
    |-- python/
    |   |-- bin/
    |   |-- include/
    |   |-- lib/
    |   |-- share/
    |
    |-- public_html/
    |   |-- highaltitudescience/
    |   |   |-- .htaccess
    |   |   |-- django.fcgi
    
    
    


A few things to note about the directory structure:



	
  * `~/django/django_src` is a direct svn checkout of the django project (`svn co http://code.djangoproject.com/svn/django/trunk/ django_src`)

	
  * `~/django/django_projects` contains the actual django code (rather than it living under `public_html`).


	
  * `django.fcgi` must be executable (`chmod a+x django.fcgi`)



**django.fcgi file:**


    
    
    #!/home4/questiq1/python/bin/python
    import sys, os
    
    # Add a custom Python path.
    sys.path.insert(0, "/home4/questiq1/django/django_src")
    sys.path.insert(0, "/home4/questiq1/django/django_projects")
    sys.path.insert(0, "/home4/questiq1/django/django_projects/mysite")
    
    # Set the DJANGO_SETTINGS_MODULE environment variable.
    os.environ['DJANGO_SETTINGS_MODULE'] = "mysite.settings"
    
    from django.core.servers.fastcgi import runfastcgi
    runfastcgi(method="threaded", daemonize="false")
    


Notice that I use a custom python path for `django.fcgi` (to force FastCGI to use my custom-installed version of python rather than the older, pre-installed one).

**.htaccess file:**

    
    
    Options +SymLinksIfOwnerMatch
    AddHandler fcgid-script .fcgi
    RewriteEngine On
    RewriteCond %{HTTP_HOST} ^(www.)?highaltitudescience.calebmadrigal.com$
    RewriteCond %{REQUEST_FILENAME} !-f [NC]
    RewriteRule ^(.*)$ django.fcgi/$1 [QSA,L]
    



**.bashrc file:**

    
    
    if [ -f /etc/bashrc ]; then
            . /etc/bashrc
    fi
    
    export PATH=~/python/bin:$PATH
    export PATH=~/django/django_src/django/bin:$PATH
    export PYTHONPATH=~/django/django_src:$PYTHONPATH
    export PYTHONPATH=~/django/django_projects:$PYTHONPATH
    
