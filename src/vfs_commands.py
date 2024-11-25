from vfs_core import VirtualFileSystem


class CommandHandler:
    def __init__(self):
        self.vfs = VirtualFileSystem()

    def run_command(self, command):
        args = command.split()
        cmd = args[0].lower()

        try:
            if cmd == "mkdir":
                self.vfs.mkdir(args[1])
                print(f"Directory '{args[1]}' created successfully.")

            elif cmd == "touch":
                self.vfs.touch(args[1])
                print(f"File '{args[1]}' created successfully.")

            elif cmd == "ls":
                items = self.vfs.ls()
                if items:
                    print("Contents:")
                    for item in items:
                        print(f"  {item}")
                else:
                    print("Directory is empty.")

            elif cmd == "cd":
                if len(args) < 2:
                    print("Error: Missing path.")
                else:
                    self.vfs.cd(args[1])
                    print(f"Changed directory to '{self.vfs.current_path}'.")

            elif cmd == "open":
                if len(args) < 2:
                    print("Error: Missing file name.")
                else:
                    self.vfs.open_file(args[1])

            elif cmd == "move":
                if len(args) < 3:
                    print("Error: Missing arguments. Usage: move <file> <target_directory>")
                else:
                    self.vfs.move(args[1], args[2])
            
            
            elif cmd == "del":
                if len(args) < 2:
                    print("Error: Missing argument. Usage: del <name>")
                else:
                    self.vfs.delete(args[1])

            elif cmd == "git":
                        if len(args) < 2:
                            print("Error: Missing Git subcommand.")
                        elif args[1] == "init":
                            self.vfs.git_init()
                            print("✔ Initialized a new Git repository.")
                        elif args[1] == "status":
                            self.vfs.git_status()
                        elif args[1] == "add":
                            if len(args) < 3:
                                print("Error: Missing file name for Git add.")
                            else:
                                self.vfs.git_add(args[2])
                        elif args[1] == "commit":
                            if len(args) < 3:
                                print("Error: Missing commit message.")
                            else:
                                message = " ".join(args[2:])
                                self.vfs.git_commit(message)
                        elif args[1] == "remote" and args[2] == "add":
                            if len(args) < 4:
                                print("Error: Missing remote name or URL. Usage: git remote add <name> <url>")
                            else:
                                self.vfs.git_add_remote(args[3], args[4])
                        elif args[1] == "push":
                            branch = args[2] if len(args) > 2 else "main"
                            self.vfs.git_push(branch)
                        elif args[1] == "pull":
                            branch = args[2] if len(args) > 2 else "main"
                            self.vfs.git_pull(branch)
                        else:
                            print(f"❌ Unknown Git subcommand: {args[1]}")

        except Exception as e:
            print(f"Error: {e}")
            