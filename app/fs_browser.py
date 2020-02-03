from flask import Flask, jsonify
from flask_restful import Resource, Api
from pathlib import Path
import sys

app = Flask(__name__)
api = Api(app)

class FileSystemInformation(Resource):
    def __init__(self, home_dir_location="/browsing_data"):
        home_dir = Path(home_dir_location).resolve()
        
        if not (home_dir.exists() and home_dir.is_dir()):
            raise ValueError(f"The location provided, {home_dir}, is not a valid directory")
        
        self.home_dir = home_dir

    def get(self, relative_path="."):
        full_path = self.home_dir.joinpath(relative_path).resolve()
        
        if not full_path.exists():
            raise ValueError(f"The location provided, {full_path} is invalid")

        if not (self.home_dir.samefile(full_path) or self.home_dir in full_path.parents):
            raise ValueError(f"The location provided, {full_path}, is not within the permitted area of {self.home_dir}")
        
        if full_path.is_file():
            # Return contents of the file
            return jsonify(full_path.read_text())
        
        if full_path.is_dir():
            # Return the information on the files inside
            all_files_info = []
            for subdir_path in full_path.iterdir():
                try:
                    stats = subdir_path.stat()
                    new_file_info = {
                        "File Name": subdir_path.name,
                        "Owner": stats.st_uid,
                        "Size": stats.st_size,
                        "Permissions": stats.st_mode
                    }
                    all_files_info.append(new_file_info)
                except Exception as e:
                    pass
            return jsonify(all_files_info)


if __name__ == '__main__':
    routes = ['/','/<path:relative_path>']
    api.add_resource(FileSystemInformation, *routes)
    app.run(port='3005', host='0.0.0.0')