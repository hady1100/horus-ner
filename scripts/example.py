# encoding: utf-8
from horus.components.core import Core

# = ["\xe5\x81\x9a\xe6\x88\x8f\xe4\xb9\x8b\xe8\xaf\xb4"]
#a = [l[0].decode('utf8')]
#print a[0]

text = u"ricardo lives in florida".encode('utf8')

horus = Core(False, 5)
print horus.annotate(text)
#print horus.get_cv_annotation()
