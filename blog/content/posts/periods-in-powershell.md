author: Caleb Madrigal
comments: true
date: 2012-01-02 20:21:30
layout: post
slug: periods-in-powershell
title: Periods in Powershell
category: powershell
tags: powershell

For running most commands, powershell and CMD work the same. One big difference I've found is that, when you use periods (`.`) in a command, they must be surrounded by quotation marks. For instance, this won't work:

    mvn clean install -U -Docns.web.dynamic.content.version=2.6.0

But this will work:

    mvn clean install -U "-Docns.web.dynamic.content.version=2.6.0"

