import unittest
from wsgiref import headers

import requests
import re

from testtools.MySQLHelper import SqlHelper


class readnote(unittest.TestCase):

    mUrl = 'http://127.0.0.1:8000/note/readnotes';

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_readnote_null(self):
        '''所有参数为空'''
        resp = requests.get(self.mUrl).json();
        self.assertTrue(resp['code'] == 0);
        self.assertTrue(resp['data'] != []);
        r = SqlHelper().query('SELECT * FROM account_note WHERE public=1');
        self.assertTrue(len(r) == len(resp['data']));

    def test_readnote_only_token(self):
        '''只填写token，获取自己的列表'''
        resp = requests.get(self.mUrl,headers={'TOKEN':'1'}).json();
        self.assertTrue(resp['code'] == 0);
        self.assertTrue(resp['data'] != []);
        r = SqlHelper().query("SELECT * FROM account_user a JOIN account_note b ON a.uid = b.uuid WHERE TOKEN='1'");
        self.assertTrue(len(r) == len(resp['data']));

    def test_readnote_only_uid(self):
        '''只填写uid，获取用户列表'''
        pass

    def test_readnote_all(self):
        '''参数都填写'''
        pass

    def test_readnote_invalidataUID(self):
        '''uid不存在'''
        pass

    def test_readnote_invalidataToken(self):
        '''token不存在'''
        pass

    def test_readnote_no_content(self):
        '''新注册用户，无内容返回'''
        pass