from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

def get_geo_info(ip):
    try:
        # Usando a API ip-api.com para obter informações geográficas
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json()
    except Exception as e:
        return {"country": "Unknown", "error": str(e)}

@app.route("/")
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_ip = request.remote_addr
    geo_info = get_geo_info(user_ip)
    country = geo_info.get("country", "Unknown")
    user_agent = request.headers.get("User-Agent")

    return render_template("index.html", current_time=current_time, user_ip=user_ip, country=country, user_agent=user_agent)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
