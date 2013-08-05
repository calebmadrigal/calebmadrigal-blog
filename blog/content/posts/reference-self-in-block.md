author: Caleb Madrigal
comments: true
date: 2012-05-08 16:14:15
layout: post
slug: reference-self-in-block
title: How to reference self in a block in Objective-C
category: objective-c
tags: functional-programming, ios, objective-c

When using ARC (automatic reference counting) in Objective-C, you need to be careful to avoid causing retain cycles.  One place where a retain cycle can occur is where self is referenced in a block.  To avoid a retain cycle, you can use the `__unsafe_unretained` modifier as such:


    __unsafe_unretained id unretained_self = self;
    reachability = [Reachability reachabilityWithHostname:@"maps.google.com"];
    reachability.reachableBlock = ^(Reachability *r) {
        dispatch_async(dispatch_get_main_queue(), ^{
            SurveyFormController *myself = unretained_self;
            self.mapView.reachable = YES;
            [myself configureView];
        });
    };

