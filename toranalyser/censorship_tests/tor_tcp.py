
from twisted.internet.error import ConnectionRefusedError
from ooni.utils import log
from ooni.templates import tcpt

class ExampleTCPT(tcpt.TCPTest):
    def test_tor_tcp(self):
        def got_response(response):
            print "Response" % response

        def connection_failed(failure):
            failure.trap(ConnectionRefusedError)
            print "Connection Refused"

        self.address = "torproject.org"
        self.port = 80
        payload = "GET!\n\r"
        d = self.sendPayload(payload)
        d.addErrback(connection_failed)
        d.addCallback(got_response)
        return d
