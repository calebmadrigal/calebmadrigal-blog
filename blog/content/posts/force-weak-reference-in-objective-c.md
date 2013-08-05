author: Caleb Madrigal
comments: true
date: 2012-01-10 20:14:27
layout: post
slug: force-weak-reference-in-objective-c
title: Force weak reference in Objective-C
category: objective-c
tags: objective-c

Today, I was trying to add an object to an `NSDictionary` and force it to be a weak reference.  This can be done with the `[NSValue valueWithNonretainedObject]` call:

    
    NSValue *weakRef = [NSValue valueWithNonretainedObject:loadDelegate];
    NSDictionary *userInfo = [[NSDictionary alloc] initWithObjectsAndKeys:weakRef, @"loadDelegate", nil];


