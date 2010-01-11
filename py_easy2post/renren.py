import Cookie,urllib
from google.appengine.api import urlfetch


renren_usr = "wenbin87@gmail.com"
renren_passwd = "CBAnbaWW"

cookie_buf = Cookie.SimpleCookie();

def make_cookie_header(cookie):
    ret = ''
    for v in cookie.values():
        ret += '%s=%s;' % (v.key, v.value)
    return ret

def login2renren():
    verify_url = 'http://passport.renren.com/PLogin.do'
    verify_data= urllib.urlencode(
        {
        'domain':'renren.com',
        'email':  renren_usr,
        'password': renren_passwd,
        'origURL':'http://home.renren.com/Home.do',
        })
    result = urlfetch.fetch(
        url=verify_url,
        headers={'Cookie':make_cookie_header(cookie_buf),
                'Content-Type': 'application/x-www-form-urlencoded',
                'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',},
        method=urlfetch.POST,
        payload=verify_data,
        follow_redirects = False,
        )
    return result

def do_redirect(url, cookie):
    result = urlfetch.fetch(
        url=url,
        headers={'Cookie':make_cookie_header(cookie),
                'Content-Type': 'application/x-www-form-urlencoded',
                'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',},
        method=urlfetch.GET,
        follow_redirects = False,
        )
    return result

def send_status(status, cookie):
    status_url = 'http://status.renren.com/doing/update.do'
    status_data = urllib.urlencode({
        'c': status,
        'raw': status,
        'isAtHome': 0,
        })
    result = urlfetch.fetch(
        url=status_url,
        headers={
            'Cookie':make_cookie_header(cookie),
            'Content-Type': 'application/x-www-form-urlencoded',
            'user-agent':'Mozilla/5.0 (Linux; U; Linux i686; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.4.2.80 Safari/525.13',
            'Referer': 'http://status.renren.com/ajaxproxy.htm'
        },
        method=urlfetch.POST,
        payload=status_data,
        )
    return result

def send(msg):
    """ send msg to renren"""
    result = login2renren()
    cookie_buf = Cookie.SimpleCookie(result.headers.get('set-cookie', ''));
    callback_url = result.headers.get('location','xx');
 
    result = do_redirect(callback_url, cookie_buf)
    cookie_buf = Cookie.SimpleCookie(result.headers.get('set-cookie', ''))
    send_status(msg, cookie_buf)
