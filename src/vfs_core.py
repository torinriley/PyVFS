import os
import subprocess
import sys


class VirtualFileSystem:
    def __init__(self, base_path="PyVFS"):
        self.root = {"type": "directory", "name": "root", "children": {}}
        self.current = self.root
        self.base_path = os.path.abspath(base_path)
        self.current_path = "root"

        os.makedirs(self.base_path, exist_ok=True)

    def mkdir(self, name):
        if name in self.current["children"]:
            raise Exception(f"Directory '{name}' already exists.")
        self.current["children"][name] = {
            "type": "directory",
            "name": name,
            "children": {},
            "parent": self.current,
        }
        real_path = os.path.join(self.base_path, self._get_real_path(name))
        os.makedirs(real_path, exist_ok=True)

    def touch(self, name):
        if name in self.current["children"]:
            raise Exception(f"File '{name}' already exists.")
        self.current["children"][name] = {
            "type": "file",
            "name": name,
            "content": "",
            "parent": self.current,
        }
        real_path = os.path.join(self.base_path, self._get_real_path(name))
        with open(real_path, "w") as f:
            pass

    def ls(self):
        return list(self.current["children"].keys())

    def cd(self, path):
        """
        Change the current directory to the specified path.
        Supports absolute paths (starting from root) and relative paths.
        """
        if path == "/": 
            self.current = self.root
            self.current_path = "root"
            return

        path_parts = path.strip("/").split("/")
        temp = self.current if not path.startswith("/") else self.root

        for part in path_parts:
            if part == "..": 
                if "parent" in temp:
                    temp = temp["parent"]
                    self.current_path = "/".join(self.current_path.split("/")[:-1]) or "root"
                else:
                    raise Exception("Already at the root directory.")
            elif part in temp["children"]:
                temp = temp["children"][part]
                if temp["type"] != "directory":
                    raise Exception(f"'{part}' is not a directory.")
                self.current_path = f"{self.current_path}/{part}".strip("/")
            else:
                raise Exception(f"Path '{path}' not found.")

        self.current = temp
    
    
    def open_file(self, filename):
        """
        Opens the specified file in VS Code or the default application.
        """
        if filename not in self.current["children"]:
            raise Exception(f"File '{filename}' does not exist in the current directory.")
        if self.current["children"][filename]["type"] != "file":
            raise Exception(f"'{filename}' is not a file.")

        real_path = os.path.join(self.base_path, self._get_real_path(filename))

        try:
            subprocess.run(["code", real_path], check=True)
            print(f"✔ File '{filename}' opened successfully in VS Code.")
        except FileNotFoundError:
            raise Exception("VS Code is not installed or not found in PATH. Please install it or add it to your PATH.")
        except Exception as e:
            raise Exception(f"Failed to open file '{filename}': {e}")
        

    def move(self, filename, target_dir):
        """
        Moves a file from the current directory to a target directory.
        Both filename and target_dir are relative to the current path.
        """
        if filename not in self.current["children"]:
            raise Exception(f"File '{filename}' does not exist in the current directory.")
        if self.current["children"][filename]["type"] != "file":
            raise Exception(f"'{filename}' is not a file.")

        target_parts = target_dir.strip("/").split("/")
        target = self.current
        for part in target_parts:
            if part not in target["children"] or target["children"][part]["type"] != "directory":
                raise Exception(f"Target directory '{target_dir}' does not exist.")
            target = target["children"][part]

        file_data = self.current["children"].pop(filename)
        target["children"][filename] = file_data

        current_path = os.path.join(self.base_path, self._get_real_path(filename))
        target_path = os.path.join(self.base_path, self._get_real_path(target_dir), filename)
        os.rename(current_path, target_path)

        print(f"Moved '{filename}' to '{target_dir}'.")

    def _get_real_path(self, path):
        """Helper to compute the full real path based on the virtual structure."""
        path_parts = []
        current = self.current
        while current.get("parent"):
            path_parts.append(current["name"])
            current = current["parent"]
        path_parts.reverse()
        return os.path.join(*path_parts, path)

    

    def create_boilerplate(self, template_name):
        """
        Creates a boilerplate structure for a specific project type.
        Supported templates: django, react, python.
        """
        if template_name == "django":
            self.mkdir("project_name")
            self.cd("project_name")
            self.mkdir("app")
            self.touch("manage.py")
            self.touch("requirements.txt")
            self.mkdir("templates")
            self.mkdir("static")
            self.cd("..")
            print("✔ Django boilerplate created successfully.")

        elif template_name == "react":
            self.mkdir("src")
            self.mkdir("public")
            self.touch("package.json")
            self.touch("src/index.js")
            self.touch("public/index.html")
            print("✔ React boilerplate created successfully.")

        elif template_name == "python":
            self.mkdir("src")
            self.touch("main.py")
            self.touch("requirements.txt")
            self.mkdir("tests")
            print("✔ Python boilerplate created successfully.")

        else:
            raise Exception(f"Unknown boilerplate template: '{template_name}'. Supported templates are: django, react, python.")
        

    #git commands    

    def git_init(self):
        """
        Initialize a Git repository in the base path.
        """
        try:
            subprocess.run(["git", "init", self.base_path], check=True)
            print("✔ Initialized a new Git repository.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git initialization failed: {e}")
    

    def git_status(self):
        """
        Show the Git status of the repository.
        """
        try:
            result = subprocess.run(
                ["git", "-C", self.base_path, "status"],
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git status check failed: {e}")
    


    def git_add(self, filename):
        """
        Stage a file for Git commit.
        """
    # Check if the file exists in the VFS
        if filename not in self.current["children"] or self.current["children"][filename]["type"] != "file":
            raise Exception(f"File '{filename}' does not exist or is not a file in the current directory.")

    # Get the full real path of the file
        real_path = os.path.join(self.base_path, self._get_real_path(filename))

    # Add the file to the Git index
        try:
            subprocess.run(["git", "-C", self.base_path, "add", real_path], check=True)
            print(f"✔ File '{filename}' added to Git staging.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to add '{filename}' to Git staging: {e}")
    

    def git_commit(self, message):
        """
        Commit changes to the Git repository with a message.
        """
        if not message:
            raise Exception("Commit message cannot be empty.")

        try:
            subprocess.run(["git", "-C", self.base_path, "commit", "-m", message], check=True)
            print(f"✔ Changes committed with message: '{message}'.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git commit failed: {e}")
        


    #commands for vcs


    def git_add_remote(self, remote_name, url):
        """
        Add a remote repository (e.g., GitHub) to the local repository.
        """
        try:
            subprocess.run(
                    ["git", "-C", self.base_path, "remote", "add", remote_name, url],
                    check=True
                )
            print(f"✔ Remote '{remote_name}' added with URL '{url}'.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to add remote '{remote_name}': {e}")
        
    def git_push(self, branch="main"):
        """
        Push committed changes to the remote repository.
        """
        try:
            subprocess.run(["git", "-C", self.base_path, "push", "-u", "origin", branch], check=True)
            print(f"✔ Changes pushed to remote branch '{branch}'.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git push failed: {e}")
        
    def git_pull(self, branch="main"):
        """
        Pull changes from the remote repository.
    """
        try:
            subprocess.run(["git", "-C", self.base_path, "pull", "origin", branch], check=True)
            print(f"✔ Changes pulled from remote branch '{branch}'.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git pull failed: {e}")
    