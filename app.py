from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_ip = request.remote_addr
    return render_template("index.html", current_time=current_time, user_ip=user_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
