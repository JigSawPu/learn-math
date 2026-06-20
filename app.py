from flask import Flask, render_template
from sympy import Eq, latex, solve, symbols

app = Flask(__name__)

x = symbols("x")

# Five quadratic equations.
quadratic_equations = [
    Eq(x**2 - 5*x + 6, 0),
    Eq(2*x**2 + 3*x - 2, 0),
    Eq(x**2 + 4*x + 4, 0),
    Eq(3*x**2 - 12, 0),
    Eq(x**2 + x - 1, 0),
]


@app.route("/")
def home():
    equations = []

    for number, equation in enumerate(quadratic_equations, start=1):
        solutions = solve(equation, x)

        equations.append(
            {
                "number": number,
                "equation_latex": latex(equation),
                "solutions_latex": latex(solutions),
            }
        )

    return render_template("index.html", equations=equations)


if __name__ == "__main__":
    # Used for local development.
    app.run(host="0.0.0.0", port=5000, debug=True)
