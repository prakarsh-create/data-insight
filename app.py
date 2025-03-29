from flask import Flask, request, render_template
import os
import process
import visualize

app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # Process Data
            insights = process.get_insights(file_path)

            # Generate Visualization
            visualize.generate_visual(file_path)

            return render_template("insights.html", insights=insights, file_name=file.filename)

    return render_template("index.html")  # Make sure index.html exists inside templates/

if __name__ == "__main__":
    app.run(debug=True)
