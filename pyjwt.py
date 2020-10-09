# -*- coding: utf-8 -*-

from os import device_encoding
from config import config_args

import jwt
import datetime as dtime
import traceback


class pyjwt():

    def create_token(self, payload):
        '''
        產生加密後token \n
        1. payload --> 放置在token內容
        '''

        token = None
        run_status = False
        msg = ""

        try:

            # 產生token
            token = jwt.encode(
                payload,
                config_args['secret'],
                algorithm=config_args['algorithm'],
                headers=config_args['headers']
            )

            run_status = True
            msg = "Done."

        except Exception as err:

            msg = "產生Token發生錯誤."
            print(f"[pyjwt-create_token] {msg} \n{traceback.format_exc()}")

        return run_status, msg, token

    def dencode_token(self, token, options={}):
        '''
        解密token取得內容 \n

        Args: \n
        1. token --> 要解密的token
        2. options --> 參數項目設定集合
        '''

        content = None
        run_status = False
        msg = ""

        try:

            # 取得token內容
            content = jwt.decode(
                token,
                config_args['secret'],
                algorithms=config_args['algorithm'],
                options=options
            )

            run_status = True
            msg = "Done."

        except jwt.ExpiredSignatureError as err:  # 檢查token是否有過期

            msg = f"Token過期. '{token}'"

        except jwt.exceptions.DecodeError as err:

            msg = "解析發生錯誤."
            print(f"[pyjwt-dencode_token] {msg} \n{traceback.format_exc()}")

        except Exception as err:

            msg = "解析發生錯誤."
            print(f"[pyjwt-dencode_token] {msg} \n{traceback.format_exc()}")

        return run_status, msg, content

    def generate_payload(self, value=None, exp=None, nbf=None, iss=None, aud=None, iat=None):
        '''
        產生要放置在Token內容，包含JWT參數值設置 \n

        Args: \n
        1. value --> 自訂放置的內容
        2. exp --> token到期時間
        3. nbf --> token 可允許處理的時間點
        4. iss --> token發行者
        5. aud --> token允許接收對象
        6. iat --> token發行的時間
        '''

        temp_content = dict()
        get_current_dt = dtime.datetime.utcnow()

        # 檢查是否有給主要的內容，如果沒給不需要在產生內容因為沒意義
        if value != None:

            # 產生主要內容key與欄位設置
            temp_content['content'] = value

        # 檢查處理 'exp' 參數
        if exp != None:

            # 產生主要內容key與欄位設置
            temp_content['exp'] = exp

        else:  # 未指定Token過期時間，使用系統預設值進行設置

            # 產生主要內容key與欄位設置
            temp_content['exp'] = self._get_next_dtime(
                dt=get_current_dt,
                unit=config_args['exp_time_unit'],
                time=config_args['exp_time']
            )

        # 檢查處理 'iss' 參數
        if iss != None:

            # 產生主要內容key與欄位設置
            temp_content['iss'] = iss

        else:  # 未指定發行者，使用系統預設值進行設置

            # 產生主要內容key與欄位設置
            temp_content['iss'] = config_args['iss']

        # 檢查處理 'iat' 參數
        if iat != None:

            # 產生主要內容key與欄位設置
            temp_content['iat'] = iat

        else:  # 未指定Token發行時間，使用系統預設值進行自動產生當下建置日期

            # 產生主要內容key與欄位設置
            temp_content['iat'] = get_current_dt

        # 檢查處理 'nbf' 參數
        if nbf != None:

            # 產生主要內容key與欄位設置
            temp_content['nbf'] = nbf

        # 檢查處理 'aud' 參數
        if aud != None:

            # 產生主要內容key與欄位設置
            temp_content['aud'] = aud

        return temp_content

    def _get_next_dtime(self, dt, unit, time=1):
        '''
        取得當前日期下一個時間點\n
        Args:
        1. dt --> 當前日期
        2. unit --> 下一個時間間隔單位
        3. time --> 時間間隔單位量，預設為1
        '''

        next_dt = None

        # 檢查要產生下一天日期單位
        if unit == 'm':  # 分鐘

            # 產生下一個時間點，以分鐘來計算
            next_dt = dt + dtime.timedelta(minutes=time)

        elif unit == 's':  # 秒

            # 產生下一個時間點，以秒來計算
            next_dt = dt + dtime.timedelta(seconds=time)

        else:  # 如果不是分鐘或秒一律都以天來計算

            # 產生下一個時間點，以天來計算
            next_dt = dt + dtime.timedelta(days=time)

        return next_dt