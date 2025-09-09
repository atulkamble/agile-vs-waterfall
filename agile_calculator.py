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
