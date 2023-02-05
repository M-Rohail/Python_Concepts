# slicing create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]
name = "Rohail Majid"
first = name[:6]
last = name[7:15]
funky = name[0:15:2]
reversed_n = name[::-1]
print(first)
print(last)
print(funky)
print(reversed_n)

# Slicing
web = "http://google.com"
web2 = "http://Wikipedia.com"
slice = slice(7, -4,)
print(web[slice])
print(web2[slice])
