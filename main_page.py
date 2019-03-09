from logging import getLogger

from locust import TaskSequence, seq_task

log = getLogger(__name__)


class MainPageSteps(TaskSequence):
    def __init__(self, parent):
        super().__init__(parent)
        self.seed = '553a09d3-baf5-45f6-ad89-83324bac051a'

    @seq_task(1)
    def index(self, name='Main Page'):
        response = self.client.get(url=(f'/?seed={self.seed}'),
                                   name='Main Page',
                                   # headers={'Host': 'localhost:5000', 'Connection': 'keep-alive',
                                   #          'Upgrade-Insecure-Requests': '1',
                                   #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                   #          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                   #          'asdasdas': '', 'Accept-Encoding': 'gzip, deflate, br',
                                   #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                   #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOiJ0MTQ6Q2FtZXJhIHllYXIgbW92aWUuYjEiLCJ0cmFpbCI6IiJ9.XIKcOA.e832410E5XshzeBHb3DSI-tJr9c'},
                                   timeout=30, allow_redirects=True)

    @seq_task(100)
    def stop(self):
        self.interrupt()
