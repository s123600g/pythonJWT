---
title: python JWT
tags: Github, readme
description: 使用Python實作一個JWT實例
---

# python JWT

### Virtualenv環境
建立環境
```shell=
virtualenv pyjwt_env --python=python3
```
進入環境
```shell=
source pyjwt_env/bin/activate
```
### 安裝pyjwt
```shell=
pip install pyjwt
```

### 執行範例 - 產生Token
```shell=
python3 createToken.py
```

### 執行範例 - 解析Token
```shell=
python3 decodeToken.py
```

# 參考
* [pyJWT](https://pyjwt.readthedocs.io/en/latest/index.html)
* [pyJWT API Reference](https://pyjwt.readthedocs.io/en/latest/api.html)

