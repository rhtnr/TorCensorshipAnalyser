from ooni.templates import dnst

class torDNSTest(dnst.DNSTest):
    inputFile = ['file', 'f', None, 'foobar']

    def test_a_lookup(self):
        def gotResult(result):
	    print self
            print result
	    if d.result.count('38.229.72.14') == 0:
	    	d.result['DNS Manipulated'] = True
	    else:
	    	d.result['DNS Manipulated'] = False
            

	
	#uses the dns from google 8.8.8.8
        d = self.performALookup('torproject.org', ('8.8.8.8', 53))
        d.addCallback(gotResult)
        return d

