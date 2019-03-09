from logging import getLogger

from locust import TaskSequence, seq_task

log = getLogger(__name__)


class Exercise2Steps(TaskSequence):
    def __init__(self, parent):
        super().__init__(parent)
        self.seed = '553a09d3-baf5-45f6-ad89-83324bac051a'

    @seq_task(1)
    def GET_http_localhost__exercises_exercise2_1359808436_2871986203929162953(self):
        response = self.client.get(
            url=f'/exercises/exercise2?seed={self.seed}',
            name='E2.01 Main',
            # headers={'Host': 'localhost:5000', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
            #          'Upgrade-Insecure-Requests': '1',
            #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            #          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #          'asdasdas': '', 'Referer': 'http://localhost:5000/?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
            #          'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
            #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=.eJwNy0EKgCAQAMCvxJ4zNN2oftAz1lxhQRTK6hD9Pe8zL5zMAVZAtKSXYJWniMphnBSFeVGztaPztGs0BD2cJV1VSm6jGrduufJxCz_dI7mjKwjnnQdvGq0HSWoOvh_d6B6a.XIKd5Q.-9BJXq_XrTcCYaYTUbU1lCjMZ48'},
            timeout=30, allow_redirects=False)

    @seq_task(2)
    def POST_http_localhost__exercises_exercise2_button1_2617182896_7215017534630073528(self):
        response = self.client.post(url='/exercises/exercise2/button1',
                                    name='E2.02 Button1',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise2?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=.eJwNy0EKgCAQAMCvxJ4zNN2oftAz1lxhQRTK6hD9Pe8zL5zMAVZAtKSXYJWniMphnBSFeVGztaPztGs0BD2cJV1VSm6jGrduufJxCz_dI7mjKwjnnQdvGq0HSWoOvh_d6B6a.XIKd-g.WWFmfu7taf-qgMkOmmeS4elRykk',
                                    #          'Connection': 'keep-alive', 'Content-Length': '33'}, timeout=30,
                                    allow_redirects=False, data='{"t14":"Interview win audience."}')
        log.debug(response.text)

    @seq_task(4)
    def POST_http_localhost__exercises_exercise2_solution_2815495008_2851250397991540474(self):
        response = self.client.post(url='/exercises/exercise2/solution',
                                    name='E2.03 Solution',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise2?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=.eJyFy0EKgCAQAMCvxJ4zNN2oftAzVl1hQQzK6hD9vX7QfeaGnTnCDIiW9BSt8pRQOUyDojhOarS2d56CRkPQwr7mo8pavlGNm5dSeTuFr-aS0tARhUvgzpuP1o0k_7rnBfPFKPc.XIKeFg.fg9h-s7Gi8YzzpWiLiPX5AXB-6I',
                                    #          'Connection': 'keep-alive', 'Content-Length': '1'}, timeout=30,
                                    allow_redirects=False, data=b'0')
        log.debug(response.text)
        assert 'OK. Good answer' in response.text

    @seq_task(100)
    def stop(self):
        self.interrupt()
