author: Caleb Madrigal
comments: true
date: 2012-03-05 18:27:30
layout: post
slug: jsonp-for-cross-origin-ajax
title: JSONP for cross-origin AJAX
wordpress_id: 156
category: javascript
tags: ajax, javascript, jquery

I was recently wanting to enable a webpage to utilize some server-side functionality which was on a different server than the one serving the original page.  Traditionally, this has been problematic due to browsers' [Same origin policy](http://en.wikipedia.org/wiki/Same_origin_policy).  JSONP is a solution to this problem.  Here is how to do it with jQuery...


This webpage can be saved locally to any machine, opened in a browser, and can then load data from my web server:

    
    
    <html><head>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    $(document).ready(function(){
        $("button").click(function(){
            $.ajax({
                url:"http://test.calebmadrigal.com/javascript/jsonp_test.json",
                dataType:'jsonp',
                jsonpCallback: "jsonp_load",
                success:function(result){
                    $("#outputdiv").html(result);
                }
            });
        });
    });
    </script>
    </head><body>
        <button>Load data</button>
        <div id="outputdiv"></div>
    </body></html>
    



Here is what the server-side looks like:

    
    
    jsonp_load("<h4>This text was loaded from http://test.calebmadrigal.com/javascript/jsonp_test.json</h4>");
    



And here is a live example:





Load data






