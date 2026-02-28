from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Custom Calculator</title>
<h2>Custom Calculator</h2>
<form method="POST">
  <input type="number" step="any" name="num1" placeholder="First number" required>
  <select name="operation">
    <option value="add">+</option>
    <option value="subtract">-</option>
    <option value="multiply">*</option>
    <option value="divide">/</option>
  </select>
  <input type="number" step="any" name="num2" placeholder="Second number" required>
  <button type="submit">Calculate</button>
</form>
{% if result is not none %}
  <h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        op = request.form["operation"]

        if op == "add":
            result = num1 + num2
        elif op == "subtract":
            result = num1 - num2
        elif op == "multiply":
            result = num1 * num2
        elif op == "divide":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
