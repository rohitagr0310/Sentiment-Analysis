# Project Setup Instructions

These instructions will guide you through setting up the project environment on a Windows system. Make sure you have Python 3.9 installed before proceeding.

## Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/rohitagr0310/VibeVerdict.git
cd VibeVerdict
```

## Step 2: Set Up Python Environment

### 2.1 Install Python 3.9

If Python 3.9 is not installed, download and install it from [python.org](https://www.python.org/downloads/release).

### 2.2 Create a Virtual Environment

Open a command prompt in the project directory and run the following commands:

```batch
setup.bat
```

This script will create a virtual environment named `venv`, activate it, and install project dependencies.

### 2.3 Activate the Virtual Environment

Whenever you work on the project, activate the virtual environment using:

```batch
venv\Scripts\activate
```

## Step 3: Verify Setup

Check if everything is set up correctly:

```batch
python --version
```

You should see `Python 3.9.x`.

```batch
pip list
```

Ensure that the required dependencies are listed.

## Additional Notes

- Make sure to use the provided virtual environment for this project to avoid conflicts with other projects.
- Always activate the virtual environment before running any project-related commands.
- Refer to the project documentation for additional details and usage instructions.

Enjoy coding!