from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def math_help(query):
    # Simple rule-based responses for Math questions
    if "derivative" in query:
        return "To find the derivative of a function, you can use the power rule, product rule, quotient rule, or chain rule."
    elif "integral" in query:
        return "To calculate the integral of a function, you can use techniques such as substitution, integration by parts, or partial fractions."
    elif "solve" in query and "equation" in query:
        return "To solve an equation, isolate the variable on one side of the equation."
    else:
        return "Sorry, I can help with basic Math questions such as derivatives, integrals, and solving equations."

