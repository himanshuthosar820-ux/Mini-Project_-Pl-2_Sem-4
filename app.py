from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


IMAGE_DIRS = [
    "Visualisation/histogram/output/",
    "Visualisation/boxplot/output/",
    "Visualisation/barchart/output/",
    "Visualisation/linechart/output/",
    "Visualisation/scatter/output/",
    "Visualisation/correlation/output/",
    "Visualisation/stack_barchart/output/",
]

def get_visualizations():
    visualizations = []
    
    
    desc_map = {
        "histogram": "Distribution analysis showing frequency of data points.",
        "boxplot": "Statistical summary showing median, quartiles, and outliers.",
        "barchart": "Comparison of categorical data using rectangular bars.",
        "linechart": "Trend analysis showing data progression over time.",
        "scatter": "Correlation analysis showing relationship between variables.",
        "correlation": "Matrix representation of relationships between multiple features.",
        "stack_barchart": "Composition analysis showing sub-categories within main categories."
    }

    for directory in IMAGE_DIRS:
        full_path = os.path.join(BASE_DIR, directory)
        if not os.path.exists(full_path):
            continue
            
        
        category = directory.split('/')[1]
        description = desc_map.get(category, "Data visualization plot.")

        for filename in os.listdir(full_path):
            if filename.endswith(".png"):
                
                title = filename.replace(".png", "").replace("-", " ").replace("_", " ").title()
                
                visualizations.append({
                    "title": title,
                    "description": description,
                    "filename": filename,
                    "directory": directory,
                    "url": f"/images/{category}/{filename}"
                })
                
    return visualizations

@app.route("/")
def index():
    viz_data = get_visualizations()
    return render_template("index.html", visualizations=viz_data)

@app.route("/images/<category>/<filename>")
def serve_image(category, filename):
    image_path = os.path.join(BASE_DIR, "Visualisation", category, "output")
    return send_from_directory(image_path, filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
