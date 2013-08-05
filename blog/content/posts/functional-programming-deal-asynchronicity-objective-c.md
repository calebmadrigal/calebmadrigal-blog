author: Caleb Madrigal
comments: true
date: 2012-05-30 21:05:43
layout: post
slug: functional-programming-deal-asynchronicity-objective-c
title: Functional programming to deal with asynchronicity in Objective-C
wordpress_id: 270
category: objective-c
tags: functional programming, objective-c

In the last few weeks, I've used the `[ALAssetsLibrary loadImages:callback:]` method to load a list of images.  For what I was doing, I wanted to wait till all the images were loaded before proceeding.  I found that I could solve this problem very elegantly using a recursive solution:


    
    
    - (void)loadImages:(NSArray *)imageUrls loadedImages:(NSArray *)loadedImages callback:(void(^)(NSArray *))callback
    {
        if (imageUrls == nil || [imageUrls count] == 0) {
            callback(loadedImages);
        }
        else {
            NSURL *head = [imageUrls head];
            __unsafe_unretained id unretained_self = self;        
            ALAssetsLibrary* library = [[ALAssetsLibrary alloc] init];
            [library assetForURL:head resultBlock:^(ALAsset *asset) {
                ALAssetRepresentation *assetRepresentation = asset.defaultRepresentation;
                
                UIImage *image = [UIImage imageWithCGImage:assetRepresentation.fullResolutionImage scale:assetRepresentation.scale orientation:(UIImageOrientation)assetRepresentation.orientation];
                            
                [unretained_self loadImages:[imageUrls tail] loadedImages:[loadedImages arrayByAddingObject:image] callback:callback];
            } failureBlock:^(NSError *error) {
                [unretained_self loadImages:[imageUrls tail] loadedImages:loadedImages callback:callback];
            }];
        }
    }
    



In general, this scenario where you want to call a blocking method over a list of items seems to be better handled by recursion.  This is just another place where functional programming proves superior in handling asynchronous tasks.

By the way, the [here](http://www.calebmadrigal.com/nsarrayfp/) is a reference to my NSArray+FP category which defines the `head` and `tail` code I use above.
