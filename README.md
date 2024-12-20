# PyJsCrawler

## 我常用的文件结构，用于快速构建 py js 组成的 web 逆向项目，不同于传统框架繁琐的处理，只考虑如何清晰的完成加密与请求

## 使用
安装js依赖
```shell
npm install
```
## JsCall单独使用
```py
from JsCall import JsCall

js = JsCall.load(filePath) # filePath是要调用js的相对路径（当对于整个项目），返回一个实例，加载好了函数名到其代码的映射
retulet = js.call(functionName, arg1, arg2, arg3, ...) # functionName要调用的函数名，后面跟上它的参数
```
### main.py
请求逻辑实现，

### Encrypt Encrypt.py
py 整合所有加密，为 main.py 提供服务

### Encrypt encrypt.js
js 加密逻辑实现，存放网页扣下来的代码，为 Encrypt.py 提供服务

### Encrypt base.py
py 内置的一些经典加密，将其封装为函数，为 Encrypt.py 提供服务

### Encrypt utiles.py
自定义一些 py 工具函数

### Test
写测试代码

### JsCall
py 调用 js 模块

### 笔记.md
记录逆向过程中的信息
