author: Caleb Madrigal
comments: true
date: 2013-03-01 19:52:27
layout: post
slug: finding-golden-ratio
title: Finding the Golden Ratio
category: math
tags: math, python

I recently was exploring the [Golden Ratio](http://en.wikipedia.org/wiki/Golden_ratio).  I was really surprised what a simple (and recursive) relationship it comes from:

![golden_ratio](/static/images/golden_ratio.png)

Here is an iPython Notebook explaining the derivation: [Golden Ratio iPython Notebook](http://nbviewer.ipython.org/urls/raw.github.com/calebmadrigal/ipython_notebooks/master/Golden%2520Ratio.ipynb)

If you don't want to look at the iPython Notebook, here is some Python code to find the golden ratio using [Fixed-point Iteration](http://en.wikipedia.org/wiki/Fixed-point_iteration):
    
    reduce(lambda acc,_: (acc+1.0)/acc, xrange(100), 1)
    # Result: 1.6180339887498947

