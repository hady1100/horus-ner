# encoding: utf-8
from horus.components.core import Core

# = ["\xe5\x81\x9a\xe6\x88\x8f\xe4\xb9\x8b\xe8\xaf\xb4"]
#a = [l[0].decode('utf8')]
#print a[0]

#text = u"diego esteves lives in sao paulo".encode('utf8')
text3 = 'Driving , driving , driving away to Phil . Tasty dinner tonight with the Society of Mining and Metallurgy Engineers .'
text = u"paris hilton was once the toast of the town".encode('utf8')
text2 = u"bullshit about airports/coffee/conferences".encode('utf8')
horus = Core(False, 5)
horus.annotate(text3)
#print horus.get_cv_annotation()


