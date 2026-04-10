from flask import Flask
import os
import socket

app = Flask(__name__)

# 환경 변수 및 호스트네임 설정
VERSION = os.environ.get("APP_VERSION", "v1")
HOSTNAME = socket.gethostname()

@app.route("/")
def home():
    return f"""
    <html>
      <head>
        <title>GitOps Demo</title>
      </head>
      <body>
        <h1>GitOps Demo Application</h1>
        <p><strong>Version:</strong> {VERSION}</p>
        <p><strong>Pod Hostname:</strong> {HOSTNAME}</p>
        <p>This app is running on EKS and deployed by Argo CD.</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "ok",
        "version": VERSION,
        "hostname": HOSTNAME
    }, 200

if __name__ == "__main__":
    # 외부 접속 허용을 위해 0.0.0.0으로 실행
    app.run(host="0.0.0.0", port=5000)