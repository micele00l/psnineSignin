import sys
import urllib, urllib2, requests
import logging

logging.basicConfig(level=logging.DEBUG)
reload(sys)
sys.setdefaultencoding("utf8")

loginurl = r"http://psnine.com/sign/in"
signurl = r"http://psnine.com/set/qidao/post"
logouturl = r"http://psnine.com/sign/out"

class psnineSign(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()

    def getHeaders(self):
        headers = {}
        headers['Host'] = "psnine.com"
        headers['Accept - Language'] = "zh-CN,zh;q=0.8,en;q=0.6"
        headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        headers["Referer"] = "http://psnine.com/"
        headers["Connection"] = "keep-alive"
        return headers

    def login(self):
        logging.debug("login...")
        loginparams = {'psnid': self.username,
                       'pass': self.password,
                       'signin': ''}
        req = self.session.post(loginurl, data=loginparams, headers=self.getHeaders())
        #logging.debug(req.content)

    def sign(self):
        signreq = self.session.get(signurl, headers=self.getHeaders())
        #logging.debug(signreq.content)

    def logout(self):
        logoutreq = self.session.get(logouturl, headers=self.getHeaders())
        self.session.close()

if __name__ == "__main__":
    psnloginObj = psnineSign("psnid", "123456")
    psnloginObj.login()
    psnloginObj.sign()
    psnloginObj.logout()
