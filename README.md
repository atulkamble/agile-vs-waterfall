# 📘 Agile vs Waterfall Model

## 1. Waterfall Model

### 🔹 Definition

A **linear and sequential approach** to software development. Each phase must be completed before moving to the next.

### 🔹 Phases

1. Requirements
2. Design
3. Implementation (Coding)
4. Testing
5. Deployment
6. Maintenance

### 🔹 Example

* **Banking systems** (where requirements are fixed and strict compliance is required).
* **Government projects** with rigid contracts.

### 🔹 Small Code Example (Waterfall-like)

Suppose requirements say: "Develop a calculator with `add` and `subtract` only".

```python
# Waterfall approach: Fixed scope, build only requested features
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(5, 3))      # 8
print(calc.subtract(5, 3)) # 2
```

👉 If later stakeholders ask for `multiply`, it requires a **new change request**.

---

## 2. Agile Model

### 🔹 Definition

An **iterative and incremental approach**, focusing on flexibility, customer collaboration, and continuous delivery.

### 🔹 Agile Principles

* Responding to change over following a plan
* Working software over documentation
* Collaboration with stakeholders
* Frequent delivery of small increments

### 🔹 Example

* **Startups** where requirements evolve quickly.
* **E-commerce websites** (Amazon/Flipkart), where features change based on customer needs.

### 🔹 Small Code Example (Agile-like)

Iteration 1: Build basic calculator

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

Iteration 2: Add subtraction

```python
    def subtract(self, a, b):
        return a - b
```

Iteration 3: Add multiplication/division based on user feedback

```python
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Error"
```

👉 Agile allows **incremental delivery**.

---

## 3. Practical Example: E-commerce Website

* **Waterfall**:

  * Requirements fixed: Login, Product Catalog, Payment Gateway.
  * Final delivery after 6 months.
* **Agile**:

  * Sprint 1: Basic Login & Product Display.
  * Sprint 2: Add Cart feature.
  * Sprint 3: Add Payment Integration.
  * Continuous feedback improves user experience.

---

## 4. Key Differences (Comparison Chart)

| Aspect                   | Waterfall Model 🚰                      | Agile Model 🔄                          |
| ------------------------ | --------------------------------------- | --------------------------------------- |
| **Approach**             | Linear, sequential                      | Iterative, incremental                  |
| **Flexibility**          | Rigid, difficult to change              | Highly flexible                         |
| **Customer Involvement** | Minimal (end only)                      | Continuous feedback                     |
| **Testing**              | At the end                              | Continuous, in every sprint             |
| **Delivery**             | Single release                          | Frequent small releases                 |
| **Best for**             | Fixed-scope projects (banking, defense) | Dynamic-scope projects (startups, apps) |
| **Cost of change**       | High                                    | Low                                     |
| **Risk**                 | High (late discovery of issues)         | Low (early feedback)                    |

---

✅ **Summary**:

* **Waterfall** = Best for projects with well-defined, stable requirements.
* **Agile** = Best for fast-changing, user-driven projects.

---

Great—here are two small, well-commented Python programs that *illustrate* Waterfall vs Agile styles.

---

# 🚰 `waterfall_calculator.py` (Waterfall style)

*A single, fixed-scope delivery: requirements are frozen, all phases done once, then shipped.*

```python
"""
WATERFALL CALCULATOR
--------------------
- Scope is fixed: only add & subtract (per the signed-off requirements).
- We "simulate" waterfall phases in comments: Req -> Design -> Build -> Test -> Deploy.
- Any new feature (e.g., multiply) would need a formal change request and a new release.
"""

# ===== 1) REQUIREMENTS (Fixed) =====
# R1: Provide addition of two numbers.
# R2: Provide subtraction of two numbers.
# R3: Provide a CLI to run one operation at a time.

# ===== 2) DESIGN =====
# - A Calculator class with 'add' and 'subtract' methods.
# - A simple CLI parser that reads: <op> <a> <b>
# - No iterative feedback loops: we assume requirements will not change.

class Calculator:
    """Implements the fixed, approved feature set."""
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b


# ===== 3) IMPLEMENTATION =====
calc = Calculator()

def run_cli():
    """
    Very basic CLI: 
      python waterfall_calculator.py add 5 3
      python waterfall_calculator.py subtract 10 4
    """
    import sys
    if len(sys.argv) != 4:
        print("Usage: python waterfall_calculator.py <add|subtract> <a> <b>")
        sys.exit(1)

    op, a_str, b_str = sys.argv[1], sys.argv[2], sys.argv[3]
    a, b = float(a_str), float(b_str)

    if op == "add":
        print(calc.add(a, b))
    elif op == "subtract":
        print(calc.subtract(a, b))
    else:
        # No flexibility: unsupported operations are rejected
        print("Error: Operation not allowed by scope. Use 'add' or 'subtract' only.")
        sys.exit(2)

# ===== 4) (INTERNAL) TESTING =====
# In a strict Waterfall, testing happens near the end.
def _self_test():
    assert calc.add(5, 3) == 8
    assert calc.subtract(5, 3) == 2

# ===== 5) DEPLOYMENT =====
# In reality this might be packaged & shipped once.
if __name__ == "__main__":
    _self_test()   # run tests once before "release"
    run_cli()
```

---

# 🔄 `agile_calculator.py` (Agile style)

*Iterative, incremental delivery with a mini-backlog, feature toggles, and tests run every time.*

```python
"""
AGILE CALCULATOR
----------------
- Start minimal (Iteration 1), then grow features with feedback.
- Maintain a simple backlog and a feature toggle system.
- Run tests continuously to keep quality high.
"""

from typing import Callable, Dict, List

# ===== Product Backlog (evolves over time) =====
# Each backlog item is small, testable, and can be prioritized.
PRODUCT_BACKLOG: List[str] = [
    "I1: Add basic addition",                     # Iteration 1
    "I2: Add subtraction",                        # Iteration 2
    "I3: Add multiplication & division",          # Iteration 3
    "I4: Add safe division by zero handling",     # Iteration 3 (refinement)
    "I5: Add history of operations (nice-to-have)"# Future
]

# ===== Feature Toggles (deploy dark, enable when ready) =====
FEATURES: Dict[str, bool] = {
    "add": True,          # delivered in Iteration 1
    "subtract": True,     # delivered in Iteration 2
    "multiply": True,     # delivered in Iteration 3
    "divide": True,       # delivered in Iteration 3/4
    "history": False      # planned for future iteration
}

class AgileCalculator:
    """Calculator grows iteratively with toggled features and tests each iteration."""
    def __init__(self):
        self.history = []  # Enabled when FEATURES['history'] becomes True

        # Operation registry lets us add/replace behaviors without big rewrites
        self.ops: Dict[str, Callable[[float, float], float]] = {}
        if FEATURES["add"]:
            self.ops["add"] = lambda a, b: a + b
        if FEATURES["subtract"]:
            self.ops["subtract"] = lambda a, b: a - b
        if FEATURES["multiply"]:
            self.ops["multiply"] = lambda a, b: a * b
        if FEATURES["divide"]:
            self.ops["divide"] = lambda a, b: a / b if b != 0 else float("inf")  # safe-ish

    def run(self, op: str, a: float, b: float) -> float:
        """Runs an operation if enabled; otherwise raises a friendly error."""
        if op not in self.ops:
            raise ValueError(f"Feature '{op}' not available yet (toggle off or not built).")
        result = self.ops[op](a, b)

        # Record history only when the feature is truly enabled
        if FEATURES.get("history"):
            self.history.append((op, a, b, result))

        return result

    def get_history(self):
        if not FEATURES.get("history"):
            raise RuntimeError("History feature not enabled yet.")
        return list(self.history)


# ===== Continuous Testing (run every iteration) =====
def _tests():
    calc = AgileCalculator()

    # Iteration 1/2: add + subtract
    assert abs(calc.run("add", 2, 3) - 5) < 1e-9
    assert abs(calc.run("subtract", 7, 4) - 3) < 1e-9

    # Iteration 3/4: multiply + divide with safe behavior
    assert abs(calc.run("multiply", 3, 4) - 12) < 1e-9
    assert calc.run("divide", 10, 0) == float("inf")  # safe division-by-zero handling

    # History is currently toggled OFF; requesting history should fail fast
    try:
        calc.get_history()
        raise AssertionError("History should not be accessible when feature is off.")
    except RuntimeError:
        pass

def run_cli():
    """
    Usage:
      python agile_calculator.py backlog
      python agile_calculator.py features
      python agile_calculator.py <op> <a> <b>
    Examples:
      python agile_calculator.py add 5 3
      python agile_calculator.py divide 10 0
    """
    import sys
    args = sys.argv[1:]

    if not args:
        print(run_cli.__doc__)
        return

    if args[0] == "backlog":
        print("Product Backlog:")
        for item in PRODUCT_BACKLOG:
            print(" -", item)
        return

    if args[0] == "features":
        print("Feature Toggles:")
        for k, v in FEATURES.items():
            print(f" - {k}: {'ON' if v else 'OFF'}")
        return

    if len(args) == 3:
        op, a_str, b_str = args
        a, b = float(a_str), float(b_str)
        calc = AgileCalculator()
        try:
            print(calc.run(op, a, b))
        except ValueError as e:
            # In Agile, we communicate clearly when a feature isn't ready
            print("Not available yet:", e)
        return

    print(run_cli.__doc__)

if __name__ == "__main__":
    # In Agile, we run tests frequently (e.g., on every run/commit in CI)
    _tests()
    run_cli()
```

---

## How these illustrate the models

* **Waterfall program**

  * Fixed scope (only `add`, `subtract`)
  * Single big release feel (tests once, then “deploy”)
  * Any new feature → change request & new version

* **Agile program**

  * Backlog shows evolving scope
  * Feature toggles simulate incremental delivery (dark launches)
  * Tests run continuously (every run = like CI)
  * Clear errors if a feature isn’t enabled yet

