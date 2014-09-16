author: Caleb Madrigal
comments: true
date: 2014-07-13 00:20:00
layout: post
slug: sessions-in-nodejs-expressjs
title: Sessions in Node.js and Express.js
category: javascripot
tags: javascript, nodejs, expressjs

In the process of trying to explain to a friend how sessions work, I decided to write a barebones example to demonstrate how to do sessions in Node.js with Express.js.

**Here's a live demo: <http://expressjs-session-example.herokuapp.com/>**

And Here's what it looks like:

Before you enter your name:
![Before you enter a name](/static/images/session_example_1.png)

After you enter your name:
![After you enter a name](/static/images/session_example_2.png)

And here is the code:

    var express = require('express');
    var cookieParser = require('cookie-parser');
    var bodyParser = require('body-parser');
    var session = require('cookie-session');
    
    ///////////////////////////////////////////////////////////////////////////////////////// MIDDLEWARE
    
    var app = express();
    
    // Needed to handle JSON posts
    app.use(bodyParser.json());
    
    // Cookie parsing needed for sessions
    app.use(cookieParser('notsosecretkey'));
    
    // Session framework
    app.use(session({secret: 'notsosecretkey123'}));
    
    // Consider all URLs under /public/ as static files, and return them raw.
    app.use(express.static(__dirname + '/public'));
    
    /////////////////////////////////////////////////////////////////////////////////////////// HANDLERS 
    
    function getName(req, res) {
      if (req.session.name) {
        return res.json({ name: req.session.name });
      }
      else {
        return res.json({ name: '' });
      }
    }
    
    function setName(req, res) {
      if(!req.body.hasOwnProperty('name')) {
        res.statusCode = 400;
        return res.json({ error: 'Invalid message' });
      }
      else {
        req.session.name = req.body.name;
        return res.json({ name: req.body.name });
      }
    }
    
    function logout(req, res) {
      req.session = null;
      return res.json({});
    }
    
    ///////////////////////////////////////////////////////////////////////////////////////////// ROUTES 
    
    app.get('/name', getName);
    app.post('/name', setName);
    app.get('/logout', logout);
    
    ////////////////////////////////////////////////////////////////////////////////////// SERVER LISTEN
    var port = process.env.PORT || 3000;
    app.listen(port, function () { console.log("Listening on port " + port); });


Github repo: <https://github.com/calebmadrigal/expressjs-session-example>

