from flask import Flask, request

api = Flask(__name__)


@api.route("/create_store", methods=["POST"])
def tbd():
    from furniture_class import FancyFurnitureStore

    kwargs = request.json
    my_store = FancyFurnitureStore(**kwargs)

    return my_store.to_dict()


if __name__ == "__main__":
    api.run(host="127.0.0.1", port=8080, debug=True)