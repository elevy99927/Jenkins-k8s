# Python Package Management

This directory contains materials and examples for understanding and managing Python environments and packages. It is organized into the following subdirectories:

- **venv**: Learn how to create and manage Python virtual environments using `venv`.
- **anaconda**: Explore environment and package management using Anaconda.

## About Python

Python is a versatile, high-level programming language that is widely used for web development, data analysis, machine learning, and more. Its simplicity and a vast ecosystem of libraries make it an excellent choice for beginners and professionals alike.

## About pip

`pip` is the default package manager for Python. It allows you to install, upgrade, and manage Python packages from repositories like the Python Package Index (PyPI). `pip` is essential for managing project dependencies and streamlining the development process.

## Using pip with a Local Repository

In some cases, you might want to install Python packages from a local repository instead of an online source. This is particularly useful for custom or internal packages that are not hosted on PyPI. Follow the instructions below to use `pip` with a local repository:

1. **Prepare the Local Repository**:
   - Ensure your package directory contains a valid `setup.py` file.

2. **Install from the Local Directory**:
   - Use the following command to install the package:
     ```bash
     pip install /path/to/your/package
     ```
   - Replace `/path/to/your/package` with the path to the local package directory.

3. **Install from a Local `.whl` File**:
   - If your package is pre-built as a `.whl` file, use:
     ```bash
     pip install /path/to/your/package.whl
     ```

4. **Install from a Local `.tar.gz` File**:
   - For source distributions packaged as `.tar.gz`, use:
     ```bash
     pip install /path/to/your/package.tar.gz
     ```

5. **Using a Local Index**:
   - If you have multiple packages and want to simulate a local PyPI repository, use the `--find-links` option:
     ```bash
     pip install --find-links=/path/to/local/repo package_name
     ```
   - Replace `/path/to/local/repo` with the path to the directory containing your packages.

These instructions will be useful for future exercises or scenarios where network access is limited or restricted.


## Learning Objectives

By working through the materials in this directory, students will:

- Understand the importance of Python virtual environments.
- Learn how to create and manage virtual environments with `venv`.
- Learn how to use Anaconda for environment and package management.
- Best practices for handling dependencies in Python projects.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---