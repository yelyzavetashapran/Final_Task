import papermill

def run_jupyter_notebook(notebook_path, output_path):
    # Execute the Jupyter Notebook
    papermill.execute_notebook(notebook_path, output_path)

# Specify the path to your Jupyter Notebook
notebook_path = "./dq_checks.ipynb"

# Specify the output path for the executed notebook
output_path = "./execution.ipynb"

# Run the Jupyter Notebook
run_jupyter_notebook(notebook_path, output_path)
