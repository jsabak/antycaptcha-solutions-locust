from locust import seq_task, TaskSequence


class Exercise1Steps(TaskSequence):
    def __init__(self, parent):
        super().__init__(parent)
        self.seed = '553a09d3-baf5-45f6-ad89-83324bac051a'

    @seq_task(1)
    def exercises_exercise1(self):
        response = self.client.get(
            url=f'/exercises/exercise1?seed={self.seed}',
            name='E1.01 Main',
            # headers={'Host': 'localhost:5000', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
            #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            #          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #          'asdasdas': '', 'Referer': 'http://localhost:5000/?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
            #          'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
            #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOiJ0MTQ6Q2FtZXJhIHllYXIgbW92aWUuYjEiLCJ0cmFpbCI6IiJ9.XIKcVg.4un88p7NIFSc7cq8I5eYdJRTD7M'},
            timeout=30, allow_redirects=False)

    @seq_task(3)
    def exercises_exercise1_button1a(self):
        response = self.client.post(url='/exercises/exercise1/button1',
                                    name='E1.02 Button1',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise1?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOiJiMWIxYjEiLCJ0cmFpbCI6IiJ9.XIKcgw.gjQGmB7vDSa8l2nMo8jFgAkyOek',
                                    #          'Connection': 'keep-alive', 'Content-Length': '1'}, timeout=30,
                                    allow_redirects=False, data=b'0')

    @seq_task(4)
    def exercises_exercise1_button1b(self):
        response = self.client.post(url='/exercises/exercise1/button1',
                                    name='E1.03 Button1',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise1?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOiJiMWIxYjEiLCJ0cmFpbCI6ImIxIn0.XIKciA.s_QTDBB_vBeDBCCFSBwxLbtkC5U',
                                    #          'Connection': 'keep-alive', 'Content-Length': '1'}, timeout=30,
                                    allow_redirects=False, data=b'0')

    @seq_task(5)
    def exercises_exercise1_button1c(self):
        response = self.client.post(url='/exercises/exercise1/button1',
                                    name='E1.04 Button1',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise1?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=.eJyrVipOTU1RslIyNTVONLBMMdZNSkwz1TUxTTPTTUyxsNS1MDY2MklKTDYwNUxU0lEqzs8pLcnMzwPqSDIEQaBYSVFiZg5UQKkWALW7Fxw.XIKciw.J4U2SMP8hOorIW24a70iP3lZzEo',
                                    #          'Connection': 'keep-alive', 'Content-Length': '1'}, timeout=30,
                                    allow_redirects=False, data=b'0')

    @seq_task(6)
    def exercises_exercise1_solution(self):
        response = self.client.post(url='/exercises/exercise1/solution',
                                    name='E1.05 Solution',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise1?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=.eJyrVipOTU1RslIyNTVONLBMMdZNSkwz1TUxTTPTTUyxsNS1MDY2MklKTDYwNUxU0lEqzs8pLcnMzwPqSDIEQaBYSVFiZg5CoBYA5NAXrw.XIKcjA.xqrERxswWtopRCHPruDUrXQIpp8',
                                    #          'Connection': 'keep-alive', 'Content-Length': '1'}, timeout=30,
                                    allow_redirects=False, data=b'0')
        assert 'OK. Good answer' in response.text

    @seq_task(100)
    def stop(self):
        self.interrupt()
