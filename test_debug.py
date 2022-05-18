import random

import pytest
import yaml

from API_test.base_api import BaseApi
from API_test.services import Services


class TestDebug:
    @pytest.mark.parametrize("playload", yaml.safe_load(open("name_data.yaml", encoding="utf-8")))
    def test_creat_services(self,playload):

        errcode=playload["errcode"]
        errmsg=playload["errmsg"]
        r1=Services().search_services()
        len1=len(r1["data"]["results"])
        print(len1)
        if len1 > 14:
            Services().delete_service()
        else:
            r=Services().creat_services(playload)

        assert r["errcode"]==errcode
        assert r["errmsg"]==errmsg



    def test_search_service(self):

        r=Services().search_services()
        print(len(r["data"]["results"]))





