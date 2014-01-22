import mechanize, re
from BeautifulSoup import BeautifulSoup
import webbrowser
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
        





        done = False
        br = mechanize.Browser()
        response=br.open('https://bridges.torproject.org/bridges')


        forms = mechanize.ParseResponse(response, backwards_compat=False)
        form = forms[0]
        response.seek(0)

        soup = BeautifulSoup(response)
        image_tags = soup.findAll('img')
        basePresence = 'data:image/jpeg;base64,'
        for image in image_tags:
                if basePresence in image['src']:
			done = True
	    	        encData = image['src'].split(',')[1]
	    	        captcha = open("captcha.jpg", "wb")
	    	        captcha.write(encData.decode('base64'))
	    	        captcha.close()
    	        	break
        if done:
	        webbrowser.open("captcha.jpg")
	        form["recaptcha_response_field"] = raw_input('Enter Captcha:')
	        response2 = mechanize.urlopen(form.click())
	        iptext = response2.read()
	        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', iptext )
	for ipaddr in ip:
		print ipaddr
                self.address = ipaddr
                self.port = 443
                payload = "GET!\n\r"
                d = self.sendPayload(payload)
                d.addErrback(connection_failed)
                d.addCallback(got_response)
                return d
