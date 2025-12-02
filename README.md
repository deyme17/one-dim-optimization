# one-dim-optimization

A Python application for finding the minimum of unimodal functions of one variable. This project implements numerical analysis algorithms to first bracket the uncertainty interval and then refine the minimum to a specified precision.

## 📋 Features

This application implements the following numerical methods:

1.  **Interval Bracketing (Phase 1):**
    **Svenn's Algorithm**: Determines the initial uncertainty interval [a, b] where the minimum exists (maybe :P).

2.  **Minimization (Phase 2):**
    **Golden Section Search**: Reduces the interval by the golden ratio to find the minimum.
    **Fibonacci Search**: Uses Fibonacci numbers to efficiently narrow down the search range.

3.  **Graphical User Interface:**
    * User-friendly input for custom functions (e.g., `(x+1.4)**1.51 + 3*sin(1.06*x)`).
    * Selection of optimization method and precision (epsilon).
    * Visualization of results including the interval boundaries and final minimum point.

## 📂 Project Structure

The project follows a modular architecture separating the core mathematical logic from the GUI presentation.

```text
D:\one-dim-optimization
└─── README.md                  # Project documentation
└─── main.py                    # Entry point of the application
└─── requirements.txt           # Python dependencies
├─── core/                      # Mathematical logic and algorithms
│   ├─── __init__.py
│   ├─── interval_bracketer/    # Logic for finding the initial interval
│   │   ├─── __init__.py
│   │   └─── svenns_method.py   # Implementation of Svenn's Algorithm
│   └─── optimizers/            # Logic for precise minimization
│       ├─── __init__.py
│       ├─── fibonacci_method.py
│       └─── golden_section_method.py
├─── gui/                       # User Interface logic
│   ├─── __init__.py
│   ├─── app_window.py          # Main application window
│   ├─── input_widget.py        # Widget for user inputs
│   ├─── result_widget.py       # Widget for displaying results
└─── utils/                     # Shared helpers and data structures
    ├─── __init__.py
    ├─── constants.py           # Global constants
    ├─── containers.py          # Dataclasses
    ├─── formatters.py          # Text/Number formatting utilities
    ├─── interfaces.py          # Abstract Base Classes (IOptimizer, IIntervalBracketer)
    ├─── stylesheet.py          # GUI styling/CSS
    └─── ui_helper.py           # Common UI utility functions
```

## 🚀 Getting Started

### Prerequisites
* **Python 3.8+**
* Required libraries (listed in `requirements.txt`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/deyme17/one-dim-optimization.git](https://github.com/deyme17/one-dim-optimization.git)
    cd one-dim-optimization
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the main script to launch the application:
```bash
python main.py
```

## 🧠 Theory & Methods

### 1. Svenn's Algorithm (Interval Bracketing)
**Purpose:** To localize the minimum by finding an initial *uncertainty interval* [a, b] that contains the optimal point x*.

**How it works:**
The algorithm starts at an initial point x_0 and moves in the direction of decreasing function values. The step upsize with each iteration using this formula - `h_i+1 = h_i * 2^k`, where k - current iteration.
* **Expansion:** This allows the algorithm to quickly traverse flat regions of the function.
* **Termination:** The process stops when the function value begins to rise, indicating the minimum has been passed. The last three points are then used to form the bracket [a, b].

### 2. Golden Section Search (Optimization)
**Purpose:** To refine the interval [a, b] found by Svenn's method down to a precise minimum with accuracy epsilon.

**How it works:**
This is a zero-order interval reduction method that divides the search range using the **Golden Ratio** (phi≈1.618$).
* **Key Feature:** It is highly computationally efficient. After the first iteration, it requires only **one new function evaluation** per step, as it reuses one interior point from the previous iteration.

### 3. Fibonacci Search (Optimization)
**Purpose:** To find the minimum with the mathematically optimal reduction ratio for a specific number of iterations.

**How it works:**
Similar to the Golden Section method, but instead of a fixed ratio, it uses the sequence of **Fibonacci numbers** (1, 1, 2, 3, 5, 8) to determine the interval division points.
* **Key Feature:** This method provides the **greatest possible reduction** of the uncertainty interval for a fixed number of function evaluations, making it slightly more efficient than the Golden Section method when the number of steps is pre-calculated.