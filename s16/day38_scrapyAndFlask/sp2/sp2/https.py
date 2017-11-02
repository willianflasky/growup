from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory
from twisted.internet.ssl import (optionsForClientTLS, CertificateOptions, PrivateCertificate)


class MySSLFactory(ScrapyClientContextFactory):
    def getCertificateOptions(self):
        from OpenSSL import crypto
        v1 = crypto.load_privatekey(crypto.FILETYPE_PEM, open('/Users/wupeiqi/client.key.unsecure', mode='r').read())
        v2 = crypto.load_certificate(crypto.FILETYPE_PEM, open('/Users/wupeiqi/client.pem', mode='r').read())
        return CertificateOptions(
            privateKey=v1,  # pKey对象
            certificate=v2,  # X509对象
            verify=False,
            method=getattr(self, 'method', getattr(self, '_ssl_method', None))
        )