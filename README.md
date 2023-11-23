[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/n4z4v0d)](https://t.me/n4z4v0d)
[![PyPI supported Python versions](https://img.shields.io/pypi/pyversions/better-automation.svg)](https://www.python.org/downloads/release/python-3116/)
[![works badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)  

Решение невидимой капчи v3 гугл на запросах _(без использования антикапчи, браузера)_  
_Google's invisible captcha v3 solution on requests (without using anti-captcha, browser)_  


```python
import asyncio

from invisible_captcha_bypasser import ReCaptcha

captcha_response: str = asyncio.run(ReCaptcha.solve_recaptcha(anchor_url=''))
```
# DONATE (_any evm_) - 0xDEADf12DE9A24b47Da0a43E1bA70B8972F5296F2