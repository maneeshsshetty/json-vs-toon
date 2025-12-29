from flask import Flask
import json
import toon_python as toon
import tiktoken

app = Flask(__name__)

def count_tokens(text):
    try:
        encoding = tiktoken.get_encoding("cl100k_base") # Encoding for GPT-4
        return len(encoding.encode(text))
    except Exception:
        return -1

@app.route('/')
def home():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        json_output = json.dumps(data, indent=2)
        toon_output = toon.encode(data)
        
        json_tokens = count_tokens(json_output)
        toon_tokens = count_tokens(toon_output)
        
        reduction = 0
        if json_tokens > 0:
            reduction = ((json_tokens - toon_tokens) / json_tokens) * 100

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>JSON vs TOON</title>
            <style>
                body {{ font-family: monospace; display: flex; flex-direction: column; height: 100vh; margin: 0; }}
                .header {{ padding: 20px; text-align: center; background: #eee; border-bottom: 2px solid #ccc; }}
                .container {{ display: flex; flex: 1; overflow: hidden; }}
                .pane {{ flex: 1; padding: 20px; overflow: auto; border-right: 2px solid #ccc; }}
                .pane:last-child {{ border-right: none; }}
                h1 {{ margin-top: 0; font-family: sans-serif; }}
                pre {{ white-space: pre-wrap; word-wrap: break-word; background: #f4f4f4; padding: 15px; border-radius: 5px; }}
                .stats {{ font-size: 1.2rem; font-weight: bold; margin-bottom: 10px; color: #333; }}
                .saving {{ color: green; }}
            </style>
        </head>
        <body>
            <div class="header">
                <span class="stats">JSON: {json_tokens} tokens</span> | 
                <span class="stats">TOON: {toon_tokens} tokens</span> | 
                <span class="stats saving">Reduction: {reduction:.1f}%</span>
            </div>
            <div class="container">
                <div class="pane">
                    <h1>JSON</h1>
                    <pre>{json_output}</pre>
                </div>
                <div class="pane">
                    <h1>TOON</h1>
                    <pre>{toon_output}</pre>
                </div>
            </div>
        </body>
        </html>
        """
        return html
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
