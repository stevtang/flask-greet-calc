# Put your app in here.
from flask import Flask, request
from operations import add, div, mult, sub

app = Flask(__name__)

OPERATIONS = {"add": add, "sub": sub, "div": div, "mult": mult}

"""Basic math operations."""


@app.get("/math/<operation>")
def show_operation_result(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    math_operation = OPERATIONS.get(operation)

    return str(math_operation(a, b))

