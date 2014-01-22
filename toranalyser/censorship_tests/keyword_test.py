from twisted.python import usage
from ooni.templates import httpt

class UsageOptions(usage.Options):
    optParameters = [['backend', 'b', 'http://www.google.com/?q=',
                        'URL of the test backend to use']]

class HTTPKeywordFiltering(httpt.HTTPTest):
 

    inputFile = ['file', 'f', None, 'List of keywords to use for censorship testing']

    usageOptions = UsageOptions
    requiredOptions = ['backend']

    def test_get(self):
        return self.doRequest(self.localOptions['backend'], method="GET", body=self.input)

