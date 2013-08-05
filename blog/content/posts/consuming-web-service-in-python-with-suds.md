author: Caleb Madrigal
comments: true
date: 2012-01-02 20:25:08
layout: post
slug: consuming-web-service-in-python-with-suds
title: Consuming web service in Python with SUDS
category: python
tags: python, web


    import datetime
    from suds.client import Client
    url = "http://localhost:9080/dataplanws/DataPlanWebService/WEB-INF/wsdl/DataPlanWebService.wsdl"
    client = Client(url)
    print client.service.hello("Caleb")

