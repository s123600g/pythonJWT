# -*- coding: utf-8 -*-

from pyjwt import pyjwt

decode_token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJjb250ZW50IjoiTXkgSldUIEZpcnN0IiwiZXhwIjoxNjAyMjQxMTg1LCJpc3MiOiJqeXUiLCJpYXQiOjE2MDIyNDEwNjV9.aji6G6CjynywYZoxhn3tfmyWFc_uVltewqFkUwCrgX-gIc9Hrl-x0c3AZN9w4YLxehh6LT42jMaaPNFo3ztvxL4HPvCNoLTNgYuHfhouY-ys1fckbrYhNgjFcRBEHfRGg7cll_lkbhM11_yKytgdKyNj54jukIr8sU8yfQW5AP63QSP4EVViwYUobzH3xB48JiQst_pUZjjmvFhfibGsXMDIshIGBbeSRE3ShS51zkslx7ak1pqTl98PZSPfn498gftlrHdimqcSn2wPRlJJTAEBNEj56usIvf47vAmMHsfNKU_JryeIfSwJaRlWOqK28IrMJDhH7foArhsu7OGHrQ'

if __name__ == "__main__":

    # 初始化JWT模組
    jwt = pyjwt()

    # 解析Token
    run_status, msg, content, is_exp = jwt.dencode_token(decode_token)

    if run_status:

        # 檢查Token是否有過期
        if not is_exp:
            print(f"token decode: {content}")
        else:
            print(f"{msg}")

    else:
        print(f"{msg}")
