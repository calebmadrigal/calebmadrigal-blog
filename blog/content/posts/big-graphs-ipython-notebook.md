author: Caleb Madrigal
comments: true
date: 2013-07-29 21:20:15
layout: post
slug: big-graphs-ipython-notebook
title: Big graphs in iPython Notebook
wordpress_id: 484

I've been doing a good bit of [graphing](https://github.com/calebmadrigal/FourierTalkOSCON) in iPython Notebook recently, and I often wanted to make the graphs larger.  I also often wanted to label the graph axes.  So I wrote this simple function and have been using it a lot.


    
    
    # Graphing helper function
    def setup_graph(title='', x_label='', y_label='', fig_size=None):
        fig = plt.figure()
        if fig_size != None:
            fig.set_size_inches(fig_size[0], fig_size[1])
        ax = fig.add_subplot(111)
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
    



Here's what it looks like to use it:

[![setup_graph_demo](http://www.calebmadrigal.com/wp-content/uploads/2013/07/setup_graph_demo.png)](http://www.calebmadrigal.com/wp-content/uploads/2013/07/setup_graph_demo.png)

As you can see, you simply call `setup_graph` before your call to `pylab.plot()` in iPython Notebook.
