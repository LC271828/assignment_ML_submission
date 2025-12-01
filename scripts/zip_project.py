import os
import zipfile
from datetime import datetime

def zip_project():
    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Output directory
    output_dir = os.path.join(".", "zips")
    os.makedirs(output_dir, exist_ok=True)

    # Output filename
    zip_filename = os.path.join(output_dir, f"project_backup_{timestamp}.zip")

    # Root directory (current workspace folder)
    root_dir = os.getcwd()

    # ZIP the project
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder, subfolders, files in os.walk(root_dir):
            # Skip the zips folder itself (so backups don't contain previous backups)
            if "zips" in folder:
                continue
            # Skip venv
            if ".venv" in folder:
                continue
            # Skip .git
            if ".git" in folder:
                continue

            for file in files:
                file_path = os.path.join(folder, file)
                arcname = os.path.relpath(file_path, root_dir)
                zipf.write(file_path, arcname)

    print(f"✔ Project zipped successfully: {zip_filename}")

if __name__ == "__main__":
    zip_project()
