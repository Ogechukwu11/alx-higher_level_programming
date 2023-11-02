PYTHON - IMPORT & MODULES

Python's "import" and modules feature is a powerful tool that promotes code organization, reusability, and efficient development. Here's an overview with unique examples to help you understand and leverage this functionality:

Modules:
1. Modules are like virtual toolboxes that keep your code organized.
2. They group related code, functions, and variables into separate files.

Import Statement:
1. Use the "import" statement to access the contents of modules.
2. It allows you to reuse code from other files in your Python program.

Example - Math Module:

import math

result = math.sqrt(16)  # Use the "sqrt" function from the math module.

How to Use:

After importing a module, reference its functions or variables using the module name. For instance, if you have a module named "my_module," access its functions like this: my_module.my_function().

Benefits:

1. Modules encourage code reuse and minimize redundancy.
2. They enhance code readability and maintenance.

Prevent Execution When Imported:

To ensure that specific code only runs when the script is the main program (not when imported), use the following condition:

if __name__ == "__main__":
	# Code here will execute only when the script is run as the main program.
Example - Prevent Execution When Imported:

def my_function():
	print("This code runs when the script is executed directly.")

if __name__ == "__main__":
	my_function()  # This code runs only when the script is the main program.

Use Cases:

1. Import built-in modules (e.g., math, datetime) for various tasks.
2. Create your own modules to organize related code in larger projects.

Python's import & modules feature simplifies code management, fosters reusability, and enhances code structure, making it a valuable skill for Python developers.
