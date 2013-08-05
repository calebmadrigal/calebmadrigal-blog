author: Caleb Madrigal
comments: true
date: 2012-06-26 23:31:24
layout: post
slug: nsarrayfp
title: NSArray+FP
category: objective-c
tags: functional-programming, objective-c

I realized that I utilize the `[NSArray head]` and `[NSArray tail]` functions in various code snippets, but haven.t shared the actual code for that category. So here is my `NSArray+FPcode`.

NSArray+FP.h

    #import <Foundation/Foundation.h>
    typedef id(^MapBlock)(id);
    @interface NSArray (FP)
    - (NSArray *)map:(MapBlock)block;
    - (id)head;
    - (NSArray *)tail;
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
     
    - (id)head
    {
        return [self objectAtIndex:0];
    }
     
    - (NSArray *)tail
    {
        NSRange tailRange;
        tailRange.location = 1;
        tailRange.length = [self count] - 1;
        return [self subarrayWithRange:tailRange];
    }
 
    @end


