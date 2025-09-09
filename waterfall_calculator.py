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
