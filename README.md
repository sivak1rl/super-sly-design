# Super Sly Designs - README
---
[![pytest](https://github.com/sivak1rl/super-sly-design/actions/workflows/python-app.yml/badge.svg)](https://github.com/sivak1rl/super-sly-design/actions/workflows/python-app.yml)

Welcome to the **Super Sly Designs** project! This README will guide you through how to set up and run the project locally. Follow the steps below to get your environment ready.

## Prerequisites

To run this project, you need to have the following installed:

- **Python 3.x**: The backend is written in Python, so you'll need the latest version.
- **pip**: Python's package manager.
- **Virtualenv (optional)**: Recommended to create an isolated environment for running the project.
- **Flask**: This project uses Flask as its web framework.

## Installation Instructions

### Step 1: Clone the Repository

First, clone this repository to your local machine. Use the command below:

```bash
$ git clone https://github.com/sivak1rl/super-sly-designs.git
$ cd super-sly-designs
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It is recommended to use a virtual environment to keep your dependencies organized.

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Python Dependencies

Use `pip` to install the required Python packages:

```bash
$ pip install -r requirements.txt
```

### Step 4: Run the Application

After completing the steps above, you can run the Flask server locally:

```bash
$ flask --app super_sly_designs/app.py run
```

Alternatively, install the Python Extension Pack in Visual Studio Code and press F5.

By default, the application will be available at `http://127.0.0.1:5000/`.

## Directory Structure

- **static/**: Contains static assets like CSS, JavaScript, and images.
- **templates/**: Contains HTML templates used by the Flask app.
- **.venv/**: (Optional) Your virtual environment folder.
- **app.py**: The main application file.
- **requirements.txt**: Lists the dependencies required to run the project.

## Development Tips

- **Static Files**: To make changes to the CSS or JavaScript, edit the files in `static/css/` or `static/js/`.
- **Templates**: Modify the HTML files in the `templates/` folder.

## License

This project is licensed under the MIT License. Feel free to modify and use it for your needs.

## Contact

For questions or contributions, please contact **Super Sly Designs** at [contact@superslydesigns.com](mailto:contact@superslydesigns.com).

Happy coding!

