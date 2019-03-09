from locust import TaskSequence, seq_task


class Exercise4Steps(TaskSequence):
    def __init__(self, parent):
        super().__init__(parent)
        self.seed = '553a09d3-baf5-45f6-ad89-83324bac051a'

    @seq_task(1)
    def GET_http_localhost__exercises_exercise4_1359939510_1332684827073400618(self):
        response = self.client.get(
            url=f'/exercises/exercise4?seed={self.seed}',
            name='E4.01 Main',
            # headers={'Host': 'localhost:5000', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
            #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            #          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #          'asdasdas': '', 'Referer': 'http://localhost:5000/?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
            #          'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
            #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOiJzMTM6djciLCJ0cmFpbCI6IiJ9.XIKemw.aamX2mmq0nskd2yMzws3XerQ6sg'},
            timeout=30, allow_redirects=False)

    @seq_task(3)
    def POST_http_localhost__exercises_exercise4_radio_2258110964_4539212486410037292(self):
        response = self.client.post(url='/exercises/exercise4/radio',
                                    name='E4.02 Radiobutton1',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise4?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOls3LDEsNCw0XSwidHJhaWwiOlstMSwtMSwtMSwtMV19.XIKerA.HnS-FfONwYY-4WxTru7_MBAHo04',
                                    #          'Connection': 'keep-alive', 'Content-Length': '14'}, timeout=30,
                                    allow_redirects=False, data=b'{"s14a":"v70"}')

    @seq_task(4)
    def POST_http_localhost__exercises_exercise4_radio_2258110964_6418937321639132456(self):
        response = self.client.post(url='/exercises/exercise4/radio',
                                    name='E4.03 Radionutton2',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise4?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOls3LDEsNCw0XSwidHJhaWwiOls3LC0xLC0xLC0xXX0.XIKesg.LO3nJlQRqZQfVxIqP1Wkmo14yXo',
                                    #          'Connection': 'keep-alive', 'Content-Length': '14'}, timeout=30,
                                    allow_redirects=False, data=b'{"s14a":"v11"}')

    @seq_task(5)
    def POST_http_localhost__exercises_exercise4_radio_2258110964_478895383920122343(self):
        response = self.client.post(url='/exercises/exercise4/radio',
                                    name='E4.04 Radiobutton3',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise4?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOls3LDEsNCw0XSwidHJhaWwiOls3LDEsLTEsLTFdfQ.XIKetg._iga11XqHBnHpCmUaz2FOwnKfDU',
                                    #          'Connection': 'keep-alive', 'Content-Length': '14'}, timeout=30,
                                    allow_redirects=False, data=b'{"s14a":"v42"}')

    @seq_task(6)
    def POST_http_localhost__exercises_exercise4_radio_2258110964_3313422586282403451(self):
        response = self.client.post(url='/exercises/exercise4/radio',
                                    name='E4.05 Radiobutton4',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise4?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOls3LDEsNCw0XSwidHJhaWwiOls3LDEsNCwtMV19.XIKeug.GrCDzPsW9kEqvzmHeqnj8rpVoWY',
                                    #          'Connection': 'keep-alive', 'Content-Length': '14'}, timeout=30,
                                    allow_redirects=False, data=b'{"s14a":"v43"}')

    @seq_task(7)
    def POST_http_localhost__exercises_exercise4_solution_2816805730_8420951951149241877(self):
        response = self.client.post(url='/exercises/exercise4/solution',
                                    name='E4.06 Radiobutton5',
                                    # headers={'Origin': 'http://localhost:5000', 'Accept-Encoding': 'gzip, deflate, br',
                                    #          'Host': 'localhost:5000', 'asdasdas': '',
                                    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                                    #          'Content-Type': 'application/json; charset=UTF-8',
                                    #          'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                    #          'Accept': 'application/json, text/*',
                                    #          'Referer': 'http://localhost:5000/exercises/exercise4?seed=553a09d3-baf5-45f6-ad89-83324bac051a',
                                    #          'Cookie': 'Pycharm-3df98f63=98db09b2-b36b-4444-8454-ebfae793727a; grafana_session=2a4ddc7ab47e815ccdff5873d7c7d452; session=eyJzZWVkIjoiNTUzYTA5ZDMtYmFmNS00NWY2LWFkODktODMzMjRiYWMwNTFhIiwic29sdXRpb24iOls3LDEsNCw0XSwidHJhaWwiOls3LDEsNCw0XX0.XIKevQ.PnBq_FsvFPZkUNuhw2SQUhsa6g4',
                                    #          'Connection': 'keep-alive', 'Content-Length': '1'}, timeout=30,
                                    allow_redirects=False, data=b'0')

    @seq_task(100)
    def stop(self):
        self.interrupt()
