from flask import Flask, request, jsonify


from src.types.income import Income

api = Flask(__name__)
api.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

incomes: list[Income] = [Income("Salary", 5000)]


@api.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!", 200


@api.route("/incomes", methods=["GET"])
def get_incomes():
    response= {"incomes": [income.__dict__ for income in incomes]}
    return jsonify(response), 200


@api.route("/incomes", methods=["POST"])
def add_income():
    if not (r_data := request.get_json(force=True)):
        return {"error": "Request must be JSON"}, 400

    if not (description := r_data.get("description")):
        return {"error": "Missing description"}, 400

    if not (amount := r_data.get("amount")):
        return {"error": "Missing amount"}, 400

    if any(income.description.lower() == description.lower() for income in incomes):
        return {
            "error": f"Income with '{description.lower}' description already exists"
        }, 400

    incomes.append(Income(description, amount))
    return "", 200
