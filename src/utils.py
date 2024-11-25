import json

def save_state(vfs, filename="data/vfs_state.json"):
    with open(filename, "w") as f:
        json.dump(vfs.root, f)

def load_state(filename="data/vfs_state.json"):
    with open(filename, "r") as f:
        return json.load(f)
    
    