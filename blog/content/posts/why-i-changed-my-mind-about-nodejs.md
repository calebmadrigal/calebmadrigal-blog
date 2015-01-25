author: Caleb Madrigal
comments: true
date: 2014-09-15 22:55:00
layout: post
slug: why-i-changed-my-mind-about-nodejs
title: Why I changed my mind about Node.js
category: javascript
tags: javascript, nodejs, expressjs


## Intro

<img src="/images/nodejs-logo.png" style="width:259px; height:141px; float:left; margin-right:15px" />
I first heard of [Node.js](http://nodejs.org/) about 4 years ago. I thought it was a ridiculous idea: using JavaScript as your server-side language! JavaScript always felt to me like an inferior language. Why would you use it unless you absolutely had to!? Now of course, you have to do JavaScript if you are writing code which runs in the browser, but on the server, you can use any language you choose. So why choose JavaScript?

I did choose to use JavaScript/Node.js on my current project. I have now been using it for the last several months, and I am quite impressed! Let me tell you what made me change my mind about Node.js.

## Adoption by the Enterprise world

First, Node.js has been adopted by multiple top-tier companies, with great success. Here are a few companies who have adopted Node.js: [PayPal](https://www.paypal-engineering.com/2013/11/22/node-js-at-paypal/), [Walmart](http://venturebeat.com/2012/01/24/why-walmart-is-using-node-js/), [Ebay](http://www.ebaytechblog.com/2013/05/17/how-we-built-ebays-first-node-js-application/#.VBe2hi5dV00), [Groupon](http://www.datacenterknowledge.com/archives/2013/12/06/need-speed-groupon-migrated-node-js/), and [LinkedIn](http://venturebeat.com/2011/08/16/linkedin-node/). And these companies are not using Node for menial tasks; they’re using it in heavily-used production applications. For example, PayPal wrote about their experience using Node.js on what they call "one of the most trafficked apps on the website”. Here are some of their observations comparing their Node.js version of the app to their Java version of the app:

* Built **almost twice as fast** with fewer people
* Written in **33% fewer lines of code**
* Constructed with **40% fewer files**
* **Double the requests per second vs. the Java application**
* **35% decrease in the average response time**

(Source: <https://www.paypal-engineering.com/2013/11/22/node-js-at-paypal/>)

That’s pretty serious! That’s what got me interested.

## Package manager - NPM

<img src="/images/npm-logo.png" style="width:300px; height:150px; float:left; margin-right:15px" />
So I started looking into Node.js for myself, and found many wonderful things. First, it has a wonderful package management system called [npm](https://www.npmjs.org/). With npm, you can install practically any Node.js package/library by running “npm install package-name”. Node.js also has nice conventions for keeping track of dependencies with a package.json file. With this, you can simply clone a Node.js repo, and run “npm install” to install all of the necessary dependencies.

## Libraries

These days, having good libraries is crucial to success. And in this regard, Node.js delivers in spades. The Node.js community is incredibly vibrant, and is always turning out new packages. I have found the libraries in Node.js to be so good, that they make JavaScript into a great, productive platform. I’m a long-time Pythonista, and I have a lot of trouble getting excited about other technologies because I just can’t be as productive in them as I can in Python. But I’m excited about Node.js - I feel super productive in it, and I’ve only recently started using it. That’s about the best complement I can give to any language or platform.

## The REPL

Another thing I loved about Node.js was the [REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (read-evaluate-print loop) - or as it is sometimes called, the Node.js command-line. With this, you can just type “node” in the terminal, and be able to test out Node.js one line at a time. This is something that, coming from a strong Python background, I have come to absolutely love! I can easily write a function, and jump into the REPL, import the code, and test it out. Or I sometimes write the function in the REPL, and once it is working well, copy it to my source code file.

## Non-blocking everywhere

Node.js has another big thing going for it: it was built with an emphasis on non-blocking functions (on the [Event loop](http://en.wikipedia.org/wiki/Event_loop) model), and this emphasis has been adopted by the whole Node.js community. This is why you will see a lot of [callbacks](http://en.wikipedia.org/wiki/Callback_(computer_programming)) and [promises](https://github.com/kriskowal/q) in Node.js code. When you call a function in Node.js, if there is any chance it could take a while, that function will not return it’s value directly; instead, it will return immediately, run the long-running operation "in the background", and call the callback function when complete (passing the return value as a parameter to that callback function). This design pattern is what leads to Node.js’s impressive performance record.

## One language

Lastly, one of Node.js’s biggest advantages is also what may seem to be a disadvantage: that it is JavaScript. But this is indeed an advantage for a few reasons. The first reason is that everyone knows (or soon will need to know) JavaScript (due to everything moving to the web). So you don’t need to teach anyone a new language to use Node.js. The other reason JavaScript is advantageous is that you can use one language - JavaScript - for everything. JavaScript can obviously run in Browsers, with Node.js, JavaScript can be your server-side code, and with [Document databases](http://en.wikipedia.org/wiki/Document-oriented_database) like [MongoDB](http://www.mongodb.org/) and [CouchDB](http://couchdb.apache.org/) which store JSON objects, JavaScript can be the native format of your data. And having one language for everything can greatly simplify the task of transferring data between your database and UI, and that task often makes up a large portion of the complexity of an application.

## Conclusion

Use Node.js! It's fun, easy to learn, and (I'm betting) will continue to gain prominence in the upcoming years.

**More comments on Hacker News: <https://news.ycombinator.com/item?id=8324890>**



