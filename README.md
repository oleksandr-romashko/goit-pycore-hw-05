# Python Programming: Foundations and Best Practices 2.0

### [# goit-pycore-hw-05](https://github.com/topics/goit-pycore-hw-05)

<p align="center">
  <img align="center" src="./assets/thumbnail.svg" width="200" title="Project thumbnail" alt="project thumbnail">
</p>


## Python embedded modules and functional programming

This assignment consists of 4 parts in total, each specified separately and has a link to the solution file.

<details>

<summary><h4 style="display: inline-block">Project Setup & Run Instructions</h4></summary>


##### Prerequisites

Before starting, ensure that you have the following installed:

* Python 3.7+ (Make sure python and pip are available in your terminal)
* Git (optional, for version control)


##### Setting Up the Development Environment

1. **Clone (or copy) the Repository**

    If you haven't cloned the project yet, you can do so using:

    ```bash
    git clone https://github.com/oleksandr-romashko/goit-pycore-hw-05.git
    cd goit-pycore-hw-04
    ```

    or download zip archive with code directly [from the repository](https://github.com/oleksandr-romashko/goit-pycore-hw-04/archive/refs/heads/main.zip).


2. **Create a Virtual Environment**

    * **Linux/macOS (using `bash` or `zsh`):**

      Run the setup.sh script:

      ```bash
      source setup.sh
      ```

      This will:
      * Create a virtual environment (`.venv`).
      * Activate the virtual environment.
      * Install dependencies listed in `requirements.txt`.
      * Set the `PYTHONPATH` for module imports.

    * **Windows (using Command Prompt):**

      If you're using Command Prompt to set up your development environment, you can run the `setup.bat` script:

      ```cmd
      setup.bat
      ```
      This will:
      * Create a virtual environment (.venv).
      * Activate the virtual environment.
      * Install dependencies listed in requirements.txt.
      * Set the `PYTHONPATH` for module imports.


#### Running the Project

Once your virtual environment is set up, you can run task code.


* **Running the Tasks in VS Code**

  Once the virtual environment is activated and `PYTHONPATH` is set, you can run each of the task files directly from VS Code. Make sure that your `settings.json` (in `.vscode` folder) is correctly set up, as discussed previously.

  VS Code will automatically use the virtual environment and set the correct `PYTHONPATH` if you've configured your settings properly.

* **Running the Tasks from the Command Line**

  After setting up your virtual environment and setting the `PYTHONPATH`, you can run the tasks directly from the terminal.

  Each of these commands will run the corresponding task script (please note, that for Linux/macOS you might use `python3` instead of `python` command):

  Run task 1:

  ```bash
  python src/task_1/main.py
  ```

* **Alternatively, you can use a script to run the tasks** (apply respective task number and arguments to run respective task script):

  * **On Linux/macOS (shell script)**:

    Run task 1 with the script:
    ```bash
    ./src/task_1/run_task_1.sh
    ```

    Make sure the shell scripts have execution permission by running:

    ```bash
    chmod +x src/task_1/run_task_1.sh
    ```

  * **On Windows (batch script)**:

    ```cmd
    src\task_1\run_task_1.bat
    ```

</details>


<details>

<summary><h4 style="display: inline-block; word-break: break-all;">Assignment 1 - Cached fibonacci using closure</h4></summary>


#### Task description:

**Closures** in programming are functions that retain references to variables from their lexical scope — that is, from the context in which they were declared.

Implement a function `caching_fibonacci` that creates and uses a cache to store and reuse previously computed Fibonacci numbers.

**The Fibonacci sequence** is a series of numbers like: `0, 1, 1, 2, 3, 5, 8, ...` where each subsequent number in the sequence is the sum of the two preceding ones.

In general, to compute the `n`-th Fibonacci number, the formula is: $F_n = F_{n−1} + F_{n−2}$.

This task can be solved recursively, by calling a function that calculates Fibonacci numbers until it reaches the base cases `n = 0` or `n = 1`.


#### Solution:

Solution for this task is located in the following files:
* [./src/task_1/main.py](./src/task_1/main.py) - main entry point file.

Result screenshot - file with no issues:

<p align="center">
  <img align="left" src="./assets/results/task_1_result_no_issues.png" title="task 1 screenshot no issues" alt="result screenshot">
</p>
.


#### Task requirements:

1. The `caching_fibonacci()` function must return an inner function `fibonacci(n)`.
2. The `fibonacci(n)` function computes the `n`-th Fibonacci number. If the value is already cached, it should return the cached result.
3. If the value is not in the cache, it should compute it, store it in the cache, and return the result.
4. Use recursion to compute Fibonacci numbers.


#### Recommendations to the implementation:

Below is the pseudocode to guide the implementation:

```
FUNCTION caching_fibonacci
    Create an empty dictionary called cache

    FUNCTION fibonacci(n)
        IF n <= 0, RETURN 0
        IF n == 1, RETURN 1
        IF n IN cache, RETURN cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        RETURN cache[n]

    RETURN function fibonacci
END FUNCTION
```

The `caching_fibonacci` function creates an inner function `fibonacci` and a `cache` dictionary to store computed Fibonacci numbers. Each time `fibonacci(n)` is called, it first checks whether the `n`-th result is already stored in `cache`. If it is, it returns the cached result immediately, greatly reducing the number of recursive calls. If not, it computes the result recursively, stores it in the `cache`, and returns it. The `caching_fibonacci` function returns the `inner` fibonacci function, which can now be used to compute Fibonacci numbers efficiently using caching.


#### Evaluation criteria:

1. Correct implementation of the `fibonacci(n)` function with cache usage.
2. Efficient use of recursion and caching to optimize computation.
3. Code clarity, including readability and use of comments.


#### Usage example:

```python
# Get the fibonacci function
fib = caching_fibonacci()

# Use the fibonacci function to compute Fibonacci numbers
print(fib(10))  # Outputs 55
print(fib(15))  # Outputs 610
```

In this example, calling `fib(10)` or `fib(15)` will compute the corresponding Fibonacci numbers using the `fibonacci` function inside `caching_fibonacci`, storing previously computed results in a cache. This makes repeated calls for the same values of `n` much faster, since the results are simply retrieved from the cache. The closure allows `fibonacci(n)` to "remember" the cache between different calls, which is key to caching the computation results.

</details>
