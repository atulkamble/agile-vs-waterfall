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
