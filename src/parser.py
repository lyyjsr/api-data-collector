# 解析模块
def parse_github_user_data(data: dict) -> dict:
    return {
        "login":data.get("login"),
        "name": data.get("name"),
        "profile_url": data.get("html_url"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "bio": data.get("bio"),
        "created_at": data.get("created_at")
    }