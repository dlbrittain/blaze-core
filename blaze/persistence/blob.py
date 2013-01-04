import blaze
from blaze.carray import carray, cparams

blb = carray([], dtype='O', rootdir='p', mode='w')

for i in xrange(10):
    blb.append("s%d"%i)

for i in xrange(10):
    print blb[i]
