# Draw Heap

This project draws a min-heap as a binary tree on a 2D grid and displays the result on a web page using a Flask GUI. The project is designed to be user-friendly, with automation workflows for continuous integration.

## Features

- Computes node positions and draws connecting edges for a binary heap.
- Displays the drawn tree in a simple web page.
- Includes automation workflows to test the application.

## Files

- **draw_heap.py:** Contains the function that computes the text-based drawing of the heap.
- **app.py:** A Flask web app that uses `draw_heap.py` to display the tree.
- **requirements.txt:** Lists the project dependencies.
- **setup.py:** Allows the project to be installed as a command-line tool.
- **.github/workflows/python-app.yml:** GitHub Actions workflow for automation testing.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/draw_heap.git
   cd draw_heap

## Usage

1. **Make sure you install Flask**
   Run
    ```bash
        pip install -r requirements.txt
    ``` 

2. **Create a virtual environment:**
   ```bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
   ```

3. **Run the Flask Web App:**
    Start the web server by running:
    ```bash
        python3 app.py
    ```

    Or run directly by Command Line:
    ```bash
        python3 draw_heap.py
    ```

4. **View Output:**
    Open your web browser and navigate to http://127.0.0.1:5000.

5. **Exit:**
    Exit the program by: Press CTRL + C to quit

