from flask import Flask, request, send_file
import pandas as pd
from ydata_profiling import ProfileReport
import os

app = Flask(__name__)

@app.route('/eda', methods=['POST'])
def generate_report():
    file = request.files['file']
    df = pd.read_csv(file)
    profile = ProfileReport(df, title="EDA Report", explorative=True)
    output_path = "eda_report.html"
    profile.to_file(output_path)
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
