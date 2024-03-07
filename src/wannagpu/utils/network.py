import requests


def reminder(title, content, mode="bark", bark_id=""):
    if mode is None:
        print(title + "\n" + content)
    elif mode == "bark":
        # 提醒服务的URL
        reminder_url = f"https://api.day.app/{bark_id}/{title}/{content}"
        try:
            response = requests.post(reminder_url)
            response.raise_for_status()  # 检查请求是否成功
            print(f"发送成功: {title}")
        except requests.exceptions.RequestException as e:
            print(f"发送失败: {e}")