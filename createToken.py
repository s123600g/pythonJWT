# -*- coding: utf-8 -*-

from pyjwt import pyjwt
import json

test_content = "My JWT First"

if __name__ == "__main__":

    # 初始化JWT模組
    jwt = pyjwt()

    gen_payload = jwt.generate_payload(test_content)
    print(f"payload:  {gen_payload}")

    # 產生Token
    run_status, msg, token = jwt.create_token(gen_payload)

    if run_status:

        print(f"token: {token}")

        # 解析Token
        run_status, msg, content = jwt.dencode_token(token)

        if run_status:

            print(f"token decode: {content}")

        else:
            print(f"{msg}")

    else:

        print(f"{msg}")
