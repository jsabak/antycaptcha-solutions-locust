from locust import TaskSequence, seq_task


class Exercise3Steps(TaskSequence):
    def __init__(self, parent):
        super().__init__(parent)
        self.seed = '553a09d3-baf5-45f6-ad89-83324bac051a'

    @seq_task(1)
    def GET_http_localhost__exercises_exercise3_1359873973_9020769934715694284(self):
        response = self.client.get(
            url=f'/exercises/exercise3?seed={self.seed}',
            name='E2.01 Main',
            # headers={'Host': 'localhost:5000', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
            #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            #          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #          'asdasdas': '', 'Referer': 'http://localhost:5000/?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
            #          'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
            #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=.eJwNy0EKgCAQAMCvxJ4zNN2oftAz1lxhQRTK6hD9Pe8zL5zMAVZAtKSXYJWniMphnBSFeVGztaPztGs0BD2cJV1VSm6jGrduufJxCz_dI7mjKwjnnQdvGq0HSWoOvh_d6B6a.XIKedg.MbtqUXcZwPaKdSjth77VEG0F3Io'},
            timeout=30, allow_redirects=False)

    @seq_task(3)
    def POST_http_localhost__exercises_exercise3_dropdown_2807237457_5944980282322223139(self):
        response = self.client.post(url='/exercises/exercise3/dropdown',
                                    name='E3.02 Dropdown',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise3?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOiJzMTM6djciLCJ0cmFpbCI6IiJ9.XIKegA.WJeR-dCPhX0lnWI872O39svbw9Y',
                                    #          'Connection': 'keep-alive', 'Content-Length': '12'}, timeout=30,
                                    allow_redirects=False, data=b'{"s13":"v7"}')

    @seq_task(4)
    def POST_http_localhost__exercises_exercise3_solution_2816150369_607949673669403381(self):
        response = self.client.post(url='/exercises/exercise3/solution',
                                    name='E3.03 Solution',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise3?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=.eJyrVipOTU1RslIyNTVONLBMMdZNSkwz1TUxTTPTTUyxsNS1MDY2MklKTDYwNUxU0lEqzs8pLcnMzwPqKDY0tiozB4qVFCVm5iAEagHlHxe5.XIKehg.icK8j6FJN_U9Yxl44ARjy2BTaHE',
                                    #          'Connection': 'keep-alive', 'Content-Length': '1'}, timeout=30,
                                    allow_redirects=False, data=b'0')
        assert "OK. Good answer" in response.text

    @seq_task(100)
    def stop(self):
        self.interrupt()
