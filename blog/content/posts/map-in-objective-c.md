author: Caleb Madrigal
comments: true
date: 2012-01-20 23:22:36
layout: post
slug: map-in-objective-c
title: Map in Objective-C
category: objective-c
tags: functional-programming, objective-c

Today, I was faced with an issue several times where I had an array of items of one type, and had to convert this into an array of items of a different type. This made me really want a `map()` function. So I added one to `NSArray` like so:

NSArray+FP.h

    #import <Foundation/Foundation.h>
    typedef id(^MapBlock)(id);
    @interface NSArray (FP)
    - (NSArray *)map:(MapBlock)block;
    @end


NSArray+FP.m

    #import "NSArray+FP.h"
    @implementation NSArray (FP)
    - (NSArray *)map:(MapBlock)block {
        NSMutableArray *resultArray = [[NSMutableArray alloc] init];
        for (id object in self) {
            [resultArray addObject:block(object)];
        }
        return resultArray;
    }
    @end

So now, I can do this!

    NSArray *strArray = [NSArray arrayWithObjects:@"1",@"1",@"2",@"3",@"5",@"8",nil];
    NSArray *numArray = [strArray map:^id(id object) {
        NSString *str = object;
        return [NSNumber numberWithInt:[str intValue]];
    }];

