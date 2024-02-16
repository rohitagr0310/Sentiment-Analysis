Generate Directory Tree Documentation
=====================================

This script, `generate_directory_tree.py`, provides a function `generate_directory_tree` to create and print a directory tree structure.

Introduction
------------

The `generate_directory_tree` script is designed to visually represent the structure of a directory and its subdirectories. It excludes specific directories to focus on relevant information.

Usage
^^^^^

To use the script, follow these steps:

1. Import the `generate_directory_tree` function:

   .. code-block:: python

      from generate_directory_tree import generate_directory_tree

2. Specify directories to exclude (optional):

   .. code-block:: python

      exclude_directories = {".venv", ".ipynb_checkpoints", ".git"}

3. Call the `generate_directory_tree` function with optional exclusion:

   .. code-block:: python

      generate_directory_tree(exclude_dirs=exclude_directories)

   This will print the directory tree structure to the console.

Example
^^^^^^^

Suppose you have the following script in a file named `generate_directory_tree.py`:

.. code-block:: python

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

Run the script, and it will print a tree structure of your current working directory, excluding the specified directories.

Adjust the script and documentation based on your specific requirements and directory structure.
