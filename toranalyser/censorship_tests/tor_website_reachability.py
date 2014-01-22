# -*- encoding: utf-8 -*-
# Tests TOR website reachability with TOR proxy
# :authors: Rohit Nair
# :linebreaks UNIX


from ooni.utils import log
from ooni.templates import httpt

class httpTorTest(httpt.HTTPTest):
    name = "Tor Website HTTP Test"
    author = "Rohit Nair"
    version = 0.1
    TestId = 1

    inputs = ['http://torproject.org/','http://torproject.org/', 'https://torproject.org','http://tor.mirror.tn/','http://wikileaks.org']

    def test_http(self):
        if self.input:
            url = self.input
            return self.doRequest(url,use_tor=True)
        else:
            raise Exception("No input specified")

    def processResponseBody(self, body):
        # XXX here shall go your logic
        #     for processing the body
        self.report['Test ID'] = self.TestId
	self.TestId += 1
        if 'blocked' in body:
            self.report['IS CENSORED'] = True
        else:
            self.report['IS CENSORED'] = False

    def processResponseHeaders(self, headers):
        # XXX place in here all the logic for handling the processing of HTTP
        #     Headers.
        pass

