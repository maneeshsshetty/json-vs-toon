from flask import Flask
import json
import toon_python as toon

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        json_output = json.dumps(data, indent=2)
        toon_output = toon.encode(data)
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>JSON vs TOON</title>
            <style>
                body {{ font-family: monospace; display: flex; flex-direction: row; height: 100vh; margin: 0; }}
                .pane {{ flex: 1; padding: 20px; overflow: auto; border-right: 2px solid #ccc; }}
                .pane:last-child {{ border-right: none; }}
                h1 {{ text-align: center; font-family: sans-serif; }}
                pre {{ white-space: pre-wrap; word-wrap: break-word; background: #f4f4f4; padding: 15px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class="pane">
                <h1>JSON</h1>
                <pre>{json_output}</pre>
            </div>
            <div class="pane">
                <h1>TOON</h1>
                <pre>{toon_output}</pre>
            </div>
        </body>
        </html>
        """
        return html
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
