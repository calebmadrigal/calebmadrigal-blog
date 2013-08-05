author: Caleb Madrigal
comments: true
date: 2012-04-11 19:36:30
layout: post
slug: embedding-xslt-xml-document
title: Embedding an XSLT in an XML document
wordpress_id: 183
category: html, programming

Today, I had this XML document which I was wanting to make viewable in a browser.  My plan was to run the XML document through an XSLT engine to transform it into an HTML document (which could then be opened in a browser).

Instead, I found that I could just embed the XSLT directly in the XML document.  Then, when this file is opened in a browser, the XSLT executes and spits out HTML, which is then rendered into the browser window.  This is great because I now have the original XML file (which we wanted to keep further analysis purposes) which can also be rendered nicely in a browser.

Here's an example:


    
    
    
    
    
    ]>
    <catalog>
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" id="stylesheet">
    <xsl:template match="/">
      <html>
      <body>
      <h2>My CD Collection</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th>Title</th>
            <th>Artist</th>
          </tr>
          <xsl:for-each select="catalog/cd">
          <tr>
            <td><xsl:value-of select="title"></xsl:value-of></td>
            <td><xsl:value-of select="artist"></xsl:value-of></td>
          </tr>
          </xsl:for-each>
        </table>
      </body>
      </html>
    </xsl:template>
    </xsl:stylesheet>
    
        <cd>
            <title>Empire Burlesque</title>
            <artist>Bob Dylan</artist>
            <country>USA</country>
            <company>Columbia</company>
            <price>10.90</price>
            <year>1985</year>
        </cd>
        <cd>
            <title>Hide your heart</title>
            <artist>Bonnie Tyler</artist>
            <country>UK</country>
            <company>CBS Records</company>
            <price>9.90</price>
            <year>1988</year>
        </cd>
    </catalog>
    



And this renders as such:
[![](http://www.calebmadrigal.com/wp-content/uploads/2012/04/embedded_xslt_screenshot.png)](http://www.calebmadrigal.com/wp-content/uploads/2012/04/embedded_xslt_screenshot.png)

Please note that this doesn't work for Internet Explorer.  For IE, the XSL document must be referenced like this:

    
    
    
    
