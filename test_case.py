import json
import string

import allure
import pytest
import yaml

from API_test.services import Services
from API_test.track import Track


class TestCase():

    def setup(self):
        self.track = Track()
        self.services=Services()


    @allure.feature("轨迹")
    @allure.title("创建轨迹")
    @pytest.mark.测试
    def test_creattrack(self):

        r = self.track.creat_track()


    @allure.feature("服务")
    @allure.title("新增服务-参数校验")
    @pytest.mark.parametrize("playload", yaml.safe_load(open("name_data.yaml", encoding="utf-8")))
    def test_creat_services(self, playload):

        errcode = playload["errcode"]
        errmsg = playload["errmsg"]
        r1 = Services().search_services()
        len1 = len(r1["data"]["results"])
        print(len1)
        if len1 > 14:
            Services().delete_service()
            r = Services().creat_services(playload)
        else:
            r = Services().creat_services(playload)

        assert r["errcode"] == errcode
        assert r["errmsg"] == errmsg





if __name__=='__main__':
    pytest.main()
