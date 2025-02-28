from flask import Flask, render_template_string
from draw_heap import draw_heap, DEFAULT_HEAP

app = Flask(__name__)

@app.route('/')
def index():
    tree_str = draw_heap(DEFAULT_HEAP)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Heap Tree Visualization</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
            pre {{
                font-family: monospace;
                font-size: 16px;
                background: #f4f4f4;
                padding: 10px;
                border: 1px solid #ddd;
            }}
        </style>
    </head>
    <body>
        <h1>Heap Tree Visualization</h1>
        <pre>{tree_str}</pre>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
