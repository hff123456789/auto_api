import pytest
import yaml

from API_test.base_api import BaseApi

import random
import string


class Services(BaseApi):

    # def read_yaml():
    # with open("../data/data.yaml", encoding="utf-8") as f:
    # print(f.read())
    # a = yaml.safe_load(f)
    # return a

    def track_data(self):
        with open('track_data.yaml', 'r') as f:
            data = yaml.safe_load(f)

            return data
    def public_data(self):
        with open('common_data.yaml', 'r') as f:
            data_key = yaml.safe_load(f)
            return data_key


    def var(self):
        vars = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        print(vars)

    #@pytest.mark.parametrize("playload", yaml.safe_load(open("./name_data.yaml")))
    def creat_services(self,playload:dict):
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/service/add?key={key}"

        # 改变name的值
        name=playload.get("name")
        if "#name#"==name:
            name=f"tongtong{random.randint(111119,999999)}"
        playload['name']=name
        print(playload)


        # seed = "qwer123456789测试服务"
        # str = []
        # g改哪个值？
        # for i in range(8):
        #     str.append(random.choice(seed))
        # name = ''.join(str)

        # playload=playload
        # 你把playload都当成一个整体了把....是

        #哪儿调用creat_services
        #playload = {"name": name, "desc": None}

        # r = requests.post(url=url, json=data, headers=headers)
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)

        return r

    def search_services(self):
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/service/list?key={key}"
        playload = {"key": "666f511920b14707ae549a85379684e9"}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        # results = r["data"]["results"]
        # print(results)

        return r

    def update_service(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/service/update?key={key}"
        playload = {
            "sid": sid,
            "name": "新的服务名字1",
            "desc": None}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)

        return r

    def delete_service(self):

        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/service/delete?key={key}"
        playload = {
            "sid": sid}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def cearte_termianl(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/terminal/add?key={key}"

        playload = {
            "sid": sid,
            "name": ''.join(random.sample(string.ascii_letters + string.digits, 20)),
            "desc": ''.join(random.sample(string.ascii_letters + string.digits, 20))

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def search_termnial(self):
        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/terminal/list?key={key}"
        playload = {
            "sid": sid,
            "tid": None,
            "name": None,
            "page": 1

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def update_terminal(self):
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/terminal/update?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,
            "desc": "修改终端12346"
        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def delete_terminal(self):
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/terminal/delete?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def creat_track(self):

        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/trace/add?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,
            "trname": "轨迹123"

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def track_upload(self):
        trid = self.creat_track()["data"]["trid"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        for i in range(len(self.track_data())):
            playload = {
                "sid": sid,
                "tid": tid,
                "trid": trid,
                "points": [
                    {
                        "location": self.track_data()[i]["location"],

                        "locatetime": self.track_data()[i]["locatetime"],
                        "speed": self.track_data()[i]["speed"],
                        "direction": self.track_data()[i]["direction"],
                        "height": self.track_data()[i]["height"],
                        "accuracy": self.track_data()[i]["accuracy"]
                    }
                ]
            }
            url =f"http://test-trapi.langgemap/v1/track/point/upload?key={key}"

            ir = BaseApi()

            r = ir.run_method(url=url, json=playload, method='post')

            # print(type(r))
            print(sid, tid, trid)

            print(i)
            print(r)
        return r

    def search_track(self):
        key = self.public_data()["params"]["key"]
        url = f"http://test-trapi.langgemap/v1/track/terminal/trsearch?key={key}"
        playload = {

            "sid": 10311,
            "tid": 10300411,
            "ispoints": 1,
            "page": 1,
            "pagesize": 50,
            "starttime": 1638201600000


        }
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='get')

        # print(type(r))

        return r


if __name__ == '__main__':
    a = Services()
    #a.creat_services()
    #a.search_services()
    #a.update_service()
    #a.delete_service()
    #a.cearte_termianl()
    #a.search_termnial()
    # a.var()
    #a.update_terminal()
    #a.delete_terminal()
    #a.creat_track()
    a.track_upload()
    #a.track_data()
    #a.search_track()
