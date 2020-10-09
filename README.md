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


# 使用RSA Private & Public Key
透過openssl來進行Private & Public Key產生
### 產生Private Key
```shell=
openssl genrsa -out private.pem 2048
```
### 產生Public Key
```shell=
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```


# 參考
* [pyJWT](https://pyjwt.readthedocs.io/en/latest/index.html)
* [pyJWT API Reference](https://pyjwt.readthedocs.io/en/latest/api.html)
* [Generate OpenSSL RSA Key Pair from the Command Line](https://rietta.com/blog/openssl-generating-rsa-key-from-command/)
