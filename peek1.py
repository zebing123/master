import requests
from bs4 import BeautifulSoup

# 设置目标网站的URL
url = 'https://eea.gd.gov.cn/'  # 替换为实际的专升本录取人数信息页面URL

# 发起请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, "html.parser")  # 正确指定解析器

    # 假设录取人数在某个特定的HTML标签内，例如<div class="admission-info">，根据实际页面结构修改
    admission_info = soup.find_all('div', class_='admission-info')  # 根据实际HTML结构修改

    # 提取并打印出录取人数
    if admission_info:
        for info in admission_info:
            print(info.text.strip())  # 输出每个录取人数的信息
    else:
        print("没有找到相关的录取人数信息。")
else:
    print(f"请求失败，状态码：{response.status_code}")




