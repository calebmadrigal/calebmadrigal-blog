author: Caleb Madrigal
comments: true
date: 2012-01-19 18:02:16
layout: post
slug: how-to-place-custom-image-in-uitextfield-in-ios
title: How to place custom image in UITextField in iOS
wordpress_id: 63
category: ios
tags: cocoa, gui, ios, objective-c

Here is how to put an image in the right portion of a UITextField:


    
    
    UITextField *textField = [[UITextField alloc] initWithFrame:CGRectMake(55, 10, 660, 30)];
    textField.rightViewMode = UITextFieldViewModeWhileEditing;
    
    UIImageView *imageView = [[UIImageView alloc] initWithFrame:CGRectMake(0, 0, 15, 15)];
    imageView.image = [UIImage imageNamed:@"invalidFieldCircle"];
    textField.rightView = imageView;
    



This also assumes that an image called "invalidFieldCircle.png" is in your project's "Resources" directory, which should be located just below the main project directory (you may have to create it).
