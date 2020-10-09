# -*- coding: utf-8 -*-

from pyjwt import pyjwt

decode_token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb250ZW50IjoiTXkgSldUIEZpcnN0IiwiZXhwIjoxNjAyMjI4MTI1LCJpc3MiOiJqeXUiLCJpYXQiOjE2MDIyMjgwMDV9._qCqMClMPOpp4QSukEbqWwbkyUPdvlYMGL-FRm9HDvU'

if __name__ == "__main__":

    # 初始化JWT模組
    jwt = pyjwt()

    # 解析Token
    run_status, msg, content = jwt.dencode_token(decode_token)

    if run_status:

        print(f"token decode: {content}")

    else:
        print(f"{msg}")
