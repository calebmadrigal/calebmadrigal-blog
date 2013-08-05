author: Caleb Madrigal
comments: true
date: 2012-03-01 16:43:12
layout: post
slug: standard-deviation-in-python
title: Standard Deviation in Python
category: python
tags: probability, python, statistics

I just wanted to go through the process of calculating standard deviation today, and this is how I did it in Python.  Python makes such a nice calculator :)

    
    >>> s = [2,4,4,4,5,5,7,9]
    >>> def average(s): return sum(s) * 1.0 / len(s)
    ... 
    >>> avg = average(s)
    >>> avg
    5.0
    >>> variance = map(lambda x: (x - avg)**2, s)
    >>> variance
    [9.0, 1.0, 1.0, 1.0, 0.0, 0.0, 4.0, 16.0]
    >>> average(variance)
    4.0
    >>> import math
    >>> standard_deviation = math.sqrt(average(variance))
    >>> standard_deviation
    2.0
    >>>

