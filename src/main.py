from api_client import fetch_github_user
from parser import parse_github_user_data
from utils import save_to_json
def main():
    username = input("请输入Github用户名:").strip()
    if not username:
        print("用户名不能为空")
        return
    try:
        raw_data = fetch_github_user(username)
        parsed_data = parse_github_user_data(raw_data)
        print("\n采集结果：")
        for key,value in parsed_data.items():
            print(f"{key}:{value}")
        save_to_json(parsed_data,f"{username}.json")
        print(f"\n数据已保存到 output/{username}.json")
    except Exception as e:
        print(f"程序运行出错：{e}")
if __name__ =="__main__":
    main()