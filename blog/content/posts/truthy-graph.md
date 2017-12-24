author: Caleb Madrigal
comments: true
date: 2017-12-24 16:50:00
layout: post
slug: truthy-graph
title: Truthy Graph
category: math
tags: math

One time, I was looking at a graph, and the thought occurred to me, "this graph shows where the two sides of this equation are exactly equal, but what would a graph showed also where they were *almost* the same?", so I write a little graphing web app: **<https://truthygraph.github.io/>**.

I called it "Truthy Graph", since it shows where the 2 sides of the equation are true, or near true. I think some interesting shapes show up. Here's a few screenshots:

![sin(3x)](/images/truthygraph_sin.png)

Another cool thing, is that either side of the equation can use the 'y' or 'x' variables in any way (calling functions like `sin`, can be squared, etc - the equations need not follow the 'y=' formula). Example:

![Elliptic curve](/images/truthygraph_elliptic_curve.png)

I'm aware there are a few bugs (especially when adjusting the "fuzzy level" or the zoom), but I don't care enough to fix them (I'll accept pull requests though).

