author: Caleb Madrigal
comments: true
date: 2012-03-03 04:50:36
layout: post
slug: tail-call-optimization-in-python
title: Tail call optimization in Python
wordpress_id: 149
category: python
tags: functional programming, python

Since I've been getting into functional programming more recently, the fact that Python doesn't do tail-call optimization has been bothering me.  So I did a bit of searching, and found this gem: [Tail Call Optimization Decorator](http://code.activestate.com/recipes/474088/).

Here is a snippet from it:

    
    
    import sys
    
    class TailRecurseException:
      def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def tail_call_optimized(g):
      """
      This function decorates a function with tail call
      optimization. It does this by throwing an exception
      if it is it's own grandparent, and catching such
      exceptions to fake the tail call optimization.
      
      This function fails if the decorated
      function recurses in a non-tail context.
      """
      def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
            and f.f_back.f_back.f_code == f.f_code:
          raise TailRecurseException(args, kwargs)
        else:
          while 1:
            try:
              return g(*args, **kwargs)
            except TailRecurseException, e:
              args = e.args
              kwargs = e.kwargs
      func.__doc__ = g.__doc__
      return func
    
    @tail_call_optimized
    def factorial(n, acc=1):
      "calculate a factorial"
      if n == 0:
        return acc
      return factorial(n-1, n*acc)
    



So it is a decorator that you place on a tail-call recursive function.  This basically lets the function continue executing rather than throwing the `RuntimeError: maximum recursion depth exceeded` exception.
