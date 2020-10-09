# -*- coding: utf-8 -*-

# 參數清單
config_args = {

    # Secret KEY
    'secret': 'myTesT123kEy@@10O09!!',

    # 配置標頭訊息表示加密演算法配置
    'headers': {
        "alg": "HS256",
        "typ": "JWT"
    },

    # 設置JWT使用的加密演算法
    'algorithm': 'HS256',

    # 設置預設Token多久過期時間單位，用在呼叫時未設置指定過期時間
    # d --> 天數
    # m --> 分鐘
    # s --> 秒數
    'exp_time_unit': 'm',

    # 設置預設Token多久過期，用在呼叫時未指定過期時間
    'exp_time': 2,

    # 設置預設發行者，用在呼叫時未設置指定發行者
    'iss': 'jyu',

}
