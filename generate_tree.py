import os


def generate_directory_tree(exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = set()

    def is_excluded(dir_name):
        return dir_name in exclude_dirs

    def walk_and_print(path, depth=0):
        if not is_excluded(os.path.basename(path)):
            print("|   " * depth + "|-- " + os.path.basename(path))
            if os.path.isdir(path):
                for item in sorted(os.listdir(path)):
                    walk_and_print(os.path.join(path, item), depth + 1)

    walk_and_print(os.getcwd())  # Get the current working directory


# Specify directories to exclude
exclude_directories = {".venv", ".ipynb_checkpoints", ".git"}

# Generate and print the directory tree
generate_directory_tree(exclude_dirs=exclude_directories)
