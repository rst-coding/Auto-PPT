import requests

class OtherAIChain:
    api_key: str = None
    session_id: str = None
    api_url: str = None

    def __init__(self, api_key, session_id, api_url):
        self.api_key = api_key
        self.session_id = session_id
        self.api_url = api_url

    def predict(self, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "session_id": self.session_id,
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": question
                }
            ]
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            # 解析响应内容为 JSON 格式
            json_response = response.json()

            # 提取 text 字段
            text = json_response.get("choices", [{}])[0].get("message", {}).get("content", "")
            return text
        else:
            return "Error: Unable to get response from AI"