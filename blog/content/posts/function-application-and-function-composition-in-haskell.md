author: Caleb Madrigal
comments: true
date: 2012-01-22 22:57:42
layout: post
slug: function-application-and-function-composition-in-haskell
title: Function application and function composition in Haskell
wordpress_id: 76
category: haskell
tags: functional programming, haskell

In the process of learning haskell, I've been trying to become comfortable with the function applicator ('$') and function composition ('.').  Here is some code to show how they relate (and how they relate to using parenthesis to enforce order of operations):


    
    
    let dict = [(1,'a'),(2,'b'),(3,'c')]
    -- The following 3 lines of code are equivalent...
    snd . head . filter (\item@(k,v) -> k == 2) $ dict -- returns 'b'
    snd $ head $ filter (\item@(k,v) -> k == 2) dict -- returns 'b'
    snd (head (filter (\item@(k,v) -> k == 2) dict)) -- return 'b'
    
