author: Caleb Madrigal
comments: true
date: 2012-05-17 20:04:04
layout: post
slug: first-look-at-pylab-matplotlib
title: First look at Pylab/Matplotlib
category: python
tags: matplotlib, python, math

Since I've been getting into Machine Learning/Artificial Intelligence recently, I've been looking at various computing environments recently.  Some of the contenders are:

	
  * [MATLAB](http://en.wikipedia.org/wiki/MATLAB) - The traditional software stack for doing machine learning and statistical analysis
  * [GNU Octave](http://en.wikipedia.org/wiki/GNU_Octave) - An open-source MATLAB clone.
  * [R](http://en.wikipedia.org/wiki/R_(programming_language)) - An open source clone of a statistical computing environment called S.
  * [Julia](http://julialang.org/) - A language for doing statistical analysis.  The goals are to compete with Matlab and R.
  * [Matplotlib/Pylab/SciPy/NumPy](http://matplotlib.sourceforge.net/) - see below


Of these, I've tried Octave and Matplotlib.  Matplotlib/Pylab is the software stack consisting of:
	
  * [iPython](http://ipython.org/) - an interactive REPL for Python with things like tab completion
  * [Matplotlib](http://matplotlib.sourceforge.net/) - a graphical plotting library
  * [NumPy](http://numpy.scipy.org/) - a matrix library
  * [SciPy](http://www.scipy.org/) - a collection of scientific and mathematical algorithms


I've only played with Matplotlib/Pylab a little bit, but I like what I've seen so far.  Here's 2 quick examples:


## 1. Displaying a Histogram of a gaussian distribution


First, make sure to run `from matplotlib import *` and `from numpy import *`


![Gaussian Histogram](/static/images/gaussian_histogram.png)

(I love how there are bell-shaped curves in the array representation of the histogram) :)

## 2. Plotting a function (y=x^2+10):

![Matplotlib Quadratic](/static/images/matplotlib_quadratic1.png)

Also, there is a really good video from PyCon 2012 on Matplotlib: [Plotting with Matplotlib](http://pyvideo.org/video/617/plotting-with-matplotlib).

