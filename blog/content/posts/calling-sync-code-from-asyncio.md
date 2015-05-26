author: Caleb Madrigal
comments: true
date: 2015-05-25 23:59:00
layout: post
slug: calling-sync-code-from-asyncio
title: Calling synchronous code from asyncio
category: python
tags: python, programming

I recently needed to call some synchronous code from [asyncio](https://docs.python.org/3/library/asyncio.html). Thankfully, asyncio provides the [`run_in_executor`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.BaseEventLoop.run_in_executor) function, which runs the specified function in a different thread. Here is an example of using it:

{% include_code python/call_sync_code.py %}

And here is the output:

<pre>
Counter: 0
Counter: 1
Counter: 2
Counter: 3
Counter: 4
Counter: 5
Data size: 337581
Counter: 6
Counter: 7
Counter: 8
Counter: 9
Counter: 10
</pre>

As you can see, even while the `get_page_len()` blocking function is running, the `count_to_10()` coroutine is still running as desired. Yay.

