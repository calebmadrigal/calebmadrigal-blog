author: Caleb Madrigal
comments: true
date: 2013-01-21 22:04:23
layout: post
slug: graph-ipython-notebook
title: How to graph with IPython Notebook
category: python
tags: matplotlib, python, ipython-notebook

IPython Notebook / Matplotlib / Pylab / Numpy is great for graphing (among other things).  Below is a simple demo of how to graph with it.

To run IPython Notebook, use this command: `ipython notebook --pylab inline`

Here's a screenshot:

![IPython Notebook Example](/static/images/ipython_notebook_example.png)

Here's an embedded IPython Notebook showing a slightly easier way:

{% notebook ipython_notebook/SimpleGraphingDemo.ipynb %}

Note: using the `--pylab` argument makes python automatically import a number of modeules, so that I can do things like just writing `pi` instead of `math.pi`.  Also, `sin()` is the `scipy.sin()` function, which can take a numpy array as an argument, so that I don't have to do a `map()` or list comprehension to apply the function to each item in `x`.
