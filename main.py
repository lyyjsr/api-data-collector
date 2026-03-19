import requests
import json
import csv
import os

URL = "https://api.github.com/events"

def fetch_data():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("请求超时")
        return None
    except requests.exceptions.RequestException as e:
        print("请求失败：", e)
        return None

def save_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_csv(data, filepath):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "type", "actor", "repo", "created_at"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            writer.writerow({
                "id": item.get("id"),
                "type": item.get("type"),
                "actor": item.get("actor", {}).get("login"),
                "repo": item.get("repo", {}).get("name"),
                "created_at": item.get("created_at")
            })

def main():
    os.makedirs("output", exist_ok=True)

    data = fetch_data()
    if not data:
        return

    print("成功获取数据，前2条示例：")
    for item in data[:2]:
        print(item["id"], item["type"])

    save_json(data, "output/result.json")
    save_csv(data, "output/result.csv")

    print("已保存到 output/result.json 和 output/result.csv")

if __name__ == "__main__":
    main()