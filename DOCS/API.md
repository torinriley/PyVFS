#  PyVFS Virtual File System (VFS) Project API

This document outlines the available commands and their functionality in the Virtual File System (VFS) project.

---

## **Commands**

### **1. mkdir <name>**
- **Description**: Creates a new directory in the current path.
- **Usage**:
  ```
  mkdir folder_name
  ```
- **Behavior**:
  - Updates the virtual file system.
  - Creates the directory on the real file system at the corresponding path.
- **Example**:
  ```
  mkdir my_folder
  ✔ Directory 'my_folder' created successfully.
  ```

---

### **2. touch <name>**
- **Description**: Creates a new file in the current path.
- **Usage**:
  ```
  touch file_name
  ```
- **Behavior**:
  - Updates the virtual file system.
  - Creates an empty file on the real file system.
- **Example**:
  ```
  touch example.txt
  ✔ File 'example.txt' created successfully.
  ```

---

### **3. ls**
- **Description**: Lists the contents of the current directory.
- **Usage**:
  ```
  ls
  ```
- **Behavior**:
  - Displays the names of all files and directories in the current directory.
- **Example**:
  ```
  ls
  Contents:
    file1.txt
    folder1
  ```

---

### **4. cd <path>**
- **Description**: Changes the current directory to the specified path.
- **Usage**:
  ```
  cd target_directory
  ```
- **Behavior**:
  - Navigates to the specified directory.
  - Supports absolute (`/`) and relative paths.
- **Example**:
  ```
  cd folder1
  ✔ Changed directory to 'root/folder1'.
  ```

---

### **5. open <file_name>**
- **Description**: Opens the specified file in the current editor (e.g., VS Code).
- **Usage**:
  ```
  open file_name
  ```
- **Behavior**:
  - Opens the file in VS Code using the `code` command.
  - Displays an error if the file doesn’t exist.
- **Example**:
  ```
  open example.txt
  ✔ File 'example.txt' opened successfully in VS Code.
  ```

---

### **6. move <file_name> <target_directory>**
- **Description**: Moves a file to the specified target directory.
- **Usage**:
  ```
  move file_name target_directory
  ```
- **Behavior**:
  - Moves the file in the virtual file system.
  - Updates the file’s location on the real file system.
- **Example**:
  ```
  move example.txt folder1
  ✔ Moved 'example.txt' to 'folder1'.
  ```

---

### **7. boilerplate <template_name>**
- **Description**: Creates a predefined project structure based on the specified template.
- **Supported Templates**: `django`, `react`, `python`
- **Usage**:
  ```
  boilerplate template_name
  ```
- **Behavior**:
  - Generates directories and files for the chosen template.
  - Creates the structure in both the virtual and real file systems.
- **Example**:
  ```
  boilerplate django
  ✔ Django boilerplate created successfully.
  ```

---

### **8. git <subcommand>**
- **Description**: Interacts with Git to initialize repositories, stage changes, and commit.
- **Subcommands**:
  - `init`: Initializes a Git repository.
  - `status`: Displays the Git status.
  - `add <file_name>`: Stages the specified file.
  - `commit <message>`: Commits staged changes with a message.
- **Usage**:
  ```
  git init
  git status
  git add file_name
  git commit "commit message"
  ```
- **Behavior**:
  - Uses the `git` command-line tool to manage repositories in the real file system.
- **Example**:
  ```
  git init
  Initialized a new Git repository.

  git add example.txt
  Added 'example.txt' to Git staging.

  git commit "Initial commit"
  Committed changes with message: 'Initial commit'.
  ```

---

## **Error Handling**
- All commands provide meaningful error messages if they fail, such as:
  - Missing arguments.
  - Invalid paths or file names.
  - Attempting unsupported operations (e.g., moving a directory).
- Example:
  ```
  cd nonexistent_folder
  Error: Path 'nonexistent_folder' not found.
  ```

---

## **Future Enhancements**
1. **Custom Boilerplates**:
   - Allow users to define their own boilerplate structures.
2. **Undo/Redo**:
   - Add a command history for reversing changes.
3. **Advanced File Operations**:
   - Add support for copying files, creating symbolic links, and directory moves.
4. **Permissions and User Roles**:
   - Simulate file permissions (read/write/execute) and ownership.

---

This document serves as a comprehensive guide to the commands available in the VFS project. Use these commands to efficiently manage files and directories in both the virtual and real file systems.


