'''
Connect to Jira
'''
from urllib.request import Request, urlopen
import json


class Jira:
    def __init__(self, url, authentication_string):
        self.query_url = url
        self.authentication_string = authentication_string
        self.data = []

    def connect(self):

        try:
            q = Request(self.query_url)
            q.add_header('Authorization', self.authentication_string)
            page = urlopen(q).read()
            page = page.decode('utf-8')
            self.data = json.loads(page)
        except:
            self.data['total'] = 0

    def TotalTickets(self):
        return int(self.data['total'])

    def CriticalCount(self):

    # TODO finsh this

    def HighCount(self):
# TODO finsh this
