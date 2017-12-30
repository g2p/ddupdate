'''
ddupdate plugin updating data on changeip.com.

See: ddupdate(8)
'''

from ddupdate.plugins_base import UpdatePlugin, UpdateError
from ddupdate.plugins_base import http_basic_auth_setup, get_response


class ChangeIpPlugin(UpdatePlugin):
    '''
    Update a dns entry on changeip.com. Does not require (but allows) an
    ip address, the ip-disabled plugin can be used.

    netrc: Use a line like
        machine nic.ChangeIP.com login <username>  password <password>

    Options:
        none
    '''
    _name = 'changeip.com'
    _oneliner = 'Updates on http://changeip.com/'
    _url = "https://nic.ChangeIP.com/nic/update?&hostname={0}"

    def run(self, config, log, ip=None):

        url = self._url.format(config.hostname)
        if ip:
            url += "&ip=" + ip
        http_basic_auth_setup(url, 'nic.ChangeIP.com')
        html = get_response(log, url)
        if not'uccessful' in html:
            raise UpdateError("Bad update reply: " + html)
