# PyJsCrawler

## 我常用的文件结构，用于快速构建 py js 组成的 web 逆向项目，不同于传统框架繁琐的处理，只考虑如何清晰的完成加密与请求

### main.py
请求逻辑实现，

### Encrypt Encrypt.py
py 整合所有加密，为 main.py 提供服务

### Encrypt Encrypt.js
js 加密逻辑实现，存放网页扣下来的代码，为 Encrypt.py 提供服务

### Encrypt Base.py
py 内置的一些经典加密，将其封装为函数，为 Encrypt.py 提供服务

### 笔记.md test.py
笔记与 py 测试代码