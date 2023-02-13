from flask import Flask, request
import os
import humanize

app = Flask(__name__)

@app.route("/metadata", methods=["POST"])
def extract_metadata():
    # Get the uploaded file from the request
    file = request.files["file"]

    # Save the uploaded file to the /tmp directory
    save_path = "/tmp/{}".format(file.filename)
    file.save(save_path)

    # Extract the file's metadata
    file_size = os.path.getsize(save_path)
    human_readable_size = humanize.naturalsize(file_size)
    file_name = file.filename

    # Remove the saved file
    os.remove(save_path)

    # Return the extracted metadata
    return {
        "file_name": file_name,
        "file_size": human_readable_size,
        "exact_file_size": file_size
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0")
