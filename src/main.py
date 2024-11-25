from vfs_commands import CommandHandler

def main():
    print("Welcome to the Virtual File System!")
    handler = CommandHandler()
    while True:
        command = input("vfs> ").strip()
        if command in ["exit", "quit"]:
            print("Exiting VFS...")
            break
        try:
            handler.run_command(command)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

