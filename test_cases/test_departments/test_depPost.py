#导包
import requests
import unittest
#设计用例

class TestDepPost(unittest.TestCase):
    # 设置请求的url
    # 设置信息头
    def  setUp(self) -> None:
        self.url=r'http://127.0.0.1:8000/api/departments/'
        self.head={"Content-Type":"application/json"}
    def test_depPost_depidNull(self):
        req_data=r'{"data": [{"dep_id":"","dep_name":"Test学院",' \
        r'"master_name":"毛毛","slogan":"Here is Slogan"}]}'
        res=requests.post(self.url,data=req_data.encode('utf-8'),headers=self.head)
        self.assertEqual(400,res.status_code)
        try:
            self.assertIn("为空lalalalaa",res.text,'id字段值为空')
        except AssertionError as e:
            print(e)
        #print(res.text)
if __name__ == '__main__':
    unittest.main()
