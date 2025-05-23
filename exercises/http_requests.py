"""
练习: HTTP请求

描述：
本练习帮助您学习如何使用requests库发送HTTP请求并处理响应。
注意：运行此练习前，请确保已安装requests库（pip install requests）。

请补全下面的函数，实现发送HTTP请求并处理响应的功能。
"""

import requests

def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典: 
      {
        'status_code': HTTP状态码,
        'content': 响应内容文本,
        'headers': 响应头部信息
      }
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return {
            'status_code': resp.status_code,
            'content': resp.text,
            'headers': dict(resp.headers)
        }
    except Exception:
        return None

def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP状态码,
        'response_json': 响应的JSON数据(如果有),
        'success': 请求是否成功(状态码为2xx)
      }
    """
    try:
        resp = requests.post(url, data=data)
        resp.raise_for_status()
        return {
            'status_code': resp.status_code,
            'response_json': resp.json() if 'application/json' in resp.headers.get('Content-Type', '') else resp.text,
            'success': True
        }
    except Exception:
        return {
            'status_code': resp.status_code if 'resp' in locals() else None,
            'response_json': None,
            'success': False
        }