# api请求模块
import requests

def fetch_github_user(username:str) -> dict:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url,timeout=20)
    if response.status_code != 200:
        raise Exception(f"请求失败，失败码：{response.status_code}")
    return response.json()