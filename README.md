calebmadrigal-blog
==================

calebmadrigal.com - my Pelican-powered blog.

Running on Ubuntu 14.04 on DigitalOcean.

# Steps to deploy

## Install dependencies

    apt-get update
    apt-get upgrade
    apt-get install python-pip
    apt-get install python-dev

    pip install Pygments
    pip install ipython
    pip install numpy

    apt-get install python-scipy
    apt-get install python-matplotlib
    apt-get install python-pandas
    pip install scikit-learn

    apt-get install pandoc
    pip install Markdown
    pip install pelican

## Clone this repository (and git submodules)

    git clone https://github.com/calebmadrigal/calebmadrigal-blog
    git pull && git submodule init && git submodule update && git submodule status

## Add regular user

    adduser caleb
    adduser caleb sudo

## Install nginx

    apt-get install nginx
    mkdir /var/www
    chown caleb /var/www
    chmod 755 /var/www
    cat nginx-conf.txt > /etc/nginx/sites-enabled/default
    service nginx restart

## Deploy site (logged in as caleb)

    make ssh_upload


# Other notes

## How to update submodules

    git submodule update --remote pelican-plugins


