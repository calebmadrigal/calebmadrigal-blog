from urllib2 import urlopen
data = urlopen("http://calebmadrigal.com/static/code/python/liquid_tags_test.py").read()
print data
