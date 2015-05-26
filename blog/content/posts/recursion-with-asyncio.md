author: Caleb Madrigal
comments: true
date: 2015-05-25 23:15:00
layout: post
slug: recursion-with-asyncio
title: Recursion with asyncio
category: python
tags: python, algorithms, programming

Recursion is awesome, but has the downside of growing the stack, which can limit its usefulness. Some languages like [Scheme](http://en.wikipedia.org/wiki/Scheme_%28programming_language%29), however, have lovely thing called [Tail-call optimization](http://en.wikipedia.org/wiki/Tail_call), lets programmers write Tail-recursive functions which don't grow the call stack. Python does not have Tail-call optimization (TCO), but with [asyncio](https://docs.python.org/3/library/asyncio.html), we can something like Tail-call optimization. Basically, this method uses the asyncio event loop like a [trampoline function](http://en.wikipedia.org/wiki/Tail_call#Through_trampolining).

Example:

{% include_code python/tail_recursion_with_asyncio.py %}

([Source on Github](https://github.com/calebmadrigal/asyncio-examples/blob/master/tail_recursion_with_asyncio.py))

A few things to note:

* This will NOT grow the call stack
* This is about 2x slower than a loop-based iterative approach (at least for this factorial algorithm)
* Notice the use of `asyncio.async()`
* Notice that we are using a done callback - this is similar to [Continuation-passing style](http://en.wikipedia.org/wiki/Continuation-passing_style).

