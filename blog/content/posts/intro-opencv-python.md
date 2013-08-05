author: Caleb Madrigal
comments: true
date: 2012-07-06 02:45:23
layout: post
slug: intro-opencv-python
title: Intro to OpenCV with Python
wordpress_id: 299
category: computer vision
tags: artificial intelligence, computer vision, opencv, python

I have started my journey into the world of OpenCV using Python on my Mac.  These are my first steps with it.



# Installing OpenCV for Python on the Mac



    
    
    # Install numpy as a prerequisite
    sudo port install numpy
    
    # Install OpenCV with the Python API
    sudo port install opencv +python27
    


(Of course, I'm using [Macports](http://www.macports.org/) here)



# Capturing an images from a webcam



    
    
    #!/usr/bin/env python2.7
    import cv
    
    cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
    
    camera_index = 0
    capture = cv.CaptureFromCAM(camera_index)
    
    frame = cv.QueryFrame(capture)
    cv.SaveImage("pic.jpg", frame)
    


(I tested this with the iSight camera on my Macbook Pro)



# Displaying live video



    
    
    #!/usr/bin/env python2.7
    import cv
    
    CAMERA_INDEX = 0
    
    cv.NamedWindow("Video", cv.CV_WINDOW_AUTOSIZE)
    capture = cv.CaptureFromCAM(CAMERA_INDEX)
    
    while True:
        frame = cv.QueryFrame(capture)
        cv.ShowImage("w1", frame)
    
