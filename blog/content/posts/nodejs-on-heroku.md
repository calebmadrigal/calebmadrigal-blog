author: Caleb Madrigal
comments: true
date: 2014-02-08 15:45:00
layout: post
slug: nodejs-on-heroku
title: NodeJS on Heroku
category: javascript
tags: javascript

I've recently tried both [Heroku](http://heroku.com) and [Node.js](http://nodejs.org/) for the first time.  Both are very simple, and work very nicely together.  This is a quick guide to deploying a Node.js app to Heroku.  To make it simple, I'll walk through deploying a Node.js [sample project I created](https://github.com/calebmadrigal/expressjs-messageboard).  It is a very simple message board.

Here are the steps to getting this simple app up and running on Heroku...

#### Get Heroku account

* Go to [Heroku](http://heroku.com), and click Sign Up
* Download and install the Heroku Toolbeld for your operating system (which gives you the `heroku` command in your terminal)
	 - [Installation details](https://toolbelt.heroku.com/)
* Open your terminal and run `heroku login`, and enter your heroku credentials and the prompts

#### Deploy your app to heroku

In your terminal, do the following:

* `git clone https://github.com/calebmadrigal/expressjs-messageboard`
    - Clone the sample message board app
* `cd expressjs-messageboard`
    - It is important to be in the top-level directory of the repository
* `heroku apps:create expressjs-messageboard`
    - Adds a git remote for heroku
    - At this point, you should be able to see the app listed in your Heroku dashboard
* `git push heroku master`
    - Pushes your repo out to heroku, which causes heroku to deploy your app
* `heroku ps:scale web=1`
    - Ensures that at least 1 "dyno" is allocated to the app

#### Bask in the glory

* `heroku open`
    - Attempts to open your app in a browser window

