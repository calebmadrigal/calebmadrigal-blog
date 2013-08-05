author: Caleb Madrigal
comments: true
date: 2012-01-09 02:30:39
layout: post
slug: first-steps-in-haskell
title: First steps in haskell
category: haskell
tags: haskell, functional-programming

Just started looking into the Haskell programming language by going through the first few chapters of the awesome book: [Learn You a Haskell](http://learnyouahaskell.com/) which is free to read online.  Here are some things I really like about what I have seen of Haskell so far:
	
  * Type inference allows you to have static typing but not all the verbosity of most other statically-typed languages.
  * Lazy evaluation is huge in Haskell, and it lets you do things like this: `let factorial n = product (take n [1..])`  So here, we have an infinite list (`[1..]` creates a infinite list from 1 to infinity!) which from which the first `n` items are taken and passed to the `product` function.  Awesomeness...
  * Nice REPL

