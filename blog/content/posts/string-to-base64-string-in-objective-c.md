author: Caleb Madrigal
comments: true
date: 2012-02-08 17:11:48
layout: post
slug: string-to-base64-string-in-objective-c
title: String to Base64 String in Objective-C
category: objective-c
tags: ios, objective-c

Today, I needed to convert an ASCII-encoded NSString to a base64 NSString.  I found a number of methods that convert from an NSString to a Base64 NSData, or from NSData to a Base64 string, but couldn't find one that did exactly what I needed.  So here is a method that simply converts an NSString to a Base64 NSString:

    
    + (NSString *)base64String:(NSString *)str
    {
        NSData *theData = [str dataUsingEncoding: NSASCIIStringEncoding];
        const uint8_t* input = (const uint8_t*)[theData bytes];
        NSInteger length = [theData length];
        
        static char table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
        
        NSMutableData* data = [NSMutableData dataWithLength:((length + 2) / 3) * 4];
        uint8_t* output = (uint8_t*)data.mutableBytes;
        
        NSInteger i;
        for (i=0; i < length; i += 3) {
            NSInteger value = 0;
            NSInteger j;
            for (j = i; j < (i + 3); j++) {
                value <<= 8;
                
                if (j < length) {
                    value |= (0xFF & input[j]);
                }
            }
            
            NSInteger theIndex = (i / 3) * 4;
            output[theIndex + 0] =                    table[(value >> 18) & 0x3F];
            output[theIndex + 1] =                    table[(value >> 12) & 0x3F];
            output[theIndex + 2] = (i + 1) < length ? table[(value >> 6)  & 0x3F] : '=';
            output[theIndex + 3] = (i + 2) < length ? table[(value >> 0)  & 0x3F] : '=';
        }
        
        return [[NSString alloc] initWithData:data encoding:NSASCIIStringEncoding];
    }


Note that the base code (which I slightly modified) was taken from this [Stackoverflow answer](http://stackoverflow.com/questions/6006823/how-to-get-base64-nsstring-from-nsdata).

