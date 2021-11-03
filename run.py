"""
common:封好的函数
test_data:测试数据
run：真正运行的代码
"""

from web.common import web01
from web.test_data import test_data
from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# 读取测试数据
url = test_data.url
username = test_data.login_user['username']
password = test_data.login_user['password']
s_key = test_data.s_key

# 调用库存查询函数     method(方法)
result = web01.search_key(url=url,username=username,password=password,driver=driver,s_key=s_key)
if s_key in result:
    print('搜素结果正确，用例执行通过!')
else:
    print('查询结果错误，用例不通过!')
# 关闭浏览器
driver.close()  # 关闭当前浏览器窗口