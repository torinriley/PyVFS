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

            elif cmd == "git":
                if args[1] == "init":
                    self.vfs.git_init()
                    print("Initialized a new Git repository.")
                elif args[1] == "status":
                    self.vfs.git_status()
                    print("Displayed Git status.")
                elif args[1] == "add":
                    self.vfs.git_add(args[2])
                    print(f"Added '{args[2]}' to Git staging.")
                elif args[1] == "commit":
                    message = " ".join(args[2:])
                    self.vfs.git_commit(message)
                    print(f"Committed changes with message: '{message}'.")
                else:
                    print(f"Unknown Git subcommand: {args[1]}")

            elif cmd == "boilerplate":
                self.vfs.create_boilerplate(args[1])
                print(f"Boilerplate '{args[1]}' created successfully.")

            else:
                print(f"Unknown command: '{cmd}'. Type 'help' for a list of commands.")

        except Exception as e:
            print(f"Error: {e}")
            