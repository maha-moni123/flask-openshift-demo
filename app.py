from flask import Flask
import os
from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

app = Flask(__name__)

@app.route("/")
def home():
    message = os.environ.get("MESSAGE", "Hello from OpenShift ")
    now_utc = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %H:%M:%S %Z")
    now_ist = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S %Z")
    return f"""
    <html>
      <head>
        <title>Flask on OpenShift</title>
        <meta charset="utf-8"/>
        <style>
          body {{ font-family: system-ui, sans-serif; padding: 2rem; }}
          .card {{ max-width: 640px; padding: 1.5rem; border: 1px solid #ddd; border-radius: 12px; }}
          .msg {{ font-size: 1.25rem; margin: 0.5rem 0 1rem; }}
          code {{ background: #f6f8fa; padding: 2px 6px; border-radius: 6px; }}
        </style>
      </head>
      <body>
        <div class="card">
          <h1> Flask running on OpenShift</h1>
          <p class="msg"><strong>MESSAGE:</strong> {message}</p>
          <p><strong>UTC time:</strong> {now_utc}</p>
          <p><strong>India time (IST):</strong> {now_ist}</p>
          <p>Edit the <code>MESSAGE</code> environment variable in your Deployment to change the text without rebuilding.</p>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
