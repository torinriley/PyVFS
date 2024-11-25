# PyVFS CLI

The **Virtual File System (VFS) CLI** is a Python-based command-line tool that simulates a virtual file system. It allows users to create directories, files, and project boilerplates, interact with Git, and open files in their preferred editor.

## Features
- **Directory and File Management**:
  - Create, move, and list files and directories.
- **Boilerplate Generation**:
  - Generate predefined project structures for Django, React, and Python.
- **Git Integration**:
  - Initialize repositories, stage files, and commit changes directly from the CLI.
- **File Opening**:
  - Open files in Visual Studio Code or the default system editor.
- **Cross-Platform Support**:
  - Works on Windows, macOS, and Linux.

## Available Commands
- `mkdir <name>`: Create a new directory.
- `touch <name>`: Create a new file.
- `ls`: List contents of the current directory.
- `cd <path>`: Change the current directory.
- `move <file> <target_directory>`: Move a file to the specified directory.
- `open <file>`: Open a file in Visual Studio Code.
- `boilerplate <template>`: Generate project boilerplates.
  - Supported templates: `django`, `react`, `python`.
- `git <subcommand>`:
  - `init`: Initialize a Git repository.
  - `status`: Display the Git status.
  - `add <file>`: Stage a file for commit.
  - `commit <message>`: Commit changes with a message.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/torinriley/PyVFS.git
   cd vfs-cli



## Docs

[API_REF](https://github.com/torinriley/PyVFS/blob/main/DOCS/API.md)
