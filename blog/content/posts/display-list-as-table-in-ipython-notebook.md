author: Caleb Madrigal
comments: true
date: 2013-08-29 22:42:00
layout: post
slug: display-list-as-table-in-ipython-notebook
title: Display List as Table in IPython Notebook
category: python
tags: python, ipython-notebook


IPython Notebook provides hook methods like `_repr_html_` which can be defined by Python objects to allow richer representations.  Here's an example:

{% notebook ipython_notebook/DisplayListAsTable.ipynb %}

The 6 rich representions currently supported by IPython Notebook are: 

* HTML
* JSON
* PNG
* JPEG
* SVG
* LaTeX

For more information, check out [this IPython Notebook](http://nbviewer.ipython.org/url/github.com/ipython/ipython/raw/master/examples/notebooks/Custom%20Display%20Logic.ipynb) (by the IPython team).

