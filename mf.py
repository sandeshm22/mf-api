import requests

BOT_TOKEN = "8420478822:AAE6Y8oUkYpwLdXhJCeox7gRKsGvbHJt21A"

# List of user chat IDs (each user must have started the bot first)
USER_CHAT_IDS = ["889779276"]

SCHEME_CODE = "118834"  # Replace with your mutual fund scheme code

def get_nav():
    url = f"https://api.mfapi.in/mf/{SCHEME_CODE}"
    response = requests.get(url)
    data = response.json()
    latest_nav = data["data"][0]
    scheme_name = data["meta"]["scheme_name"]
    nav_date = latest_nav["date"]
    nav_value = latest_nav["nav"]
    return f"{scheme_name}\nDate: {nav_date}\nNAV: {nav_value}"

def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)

def job():
    for chat_id in USER_CHAT_IDS:
        send_message(chat_id, get_nav())

if __name__ == "__main__":
    resp = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates')
    print(resp.text)
    job()
