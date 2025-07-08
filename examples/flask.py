from flask import Flask, request, jsonify, Response
from miru.callbacks import Callback, CallbackVerificationError

app = Flask(__name__)

SECRET = "cbsec_WrtItCFkZWrP8h9q4FgnoZsS3QlwUt3o/7juCWkGc1c="


@app.route("/path/to/callback", methods=["POST"])
def callback_endpoint() -> tuple[Response, int]:
    print("Callback received")

    headers = dict(request.headers)
    payload = request.get_data()

    # verify the callback
    try:
        cb = Callback(SECRET)
        cfgInstDeployment = cb.verify(payload, headers)
    except CallbackVerificationError as e:
        return jsonify({
            'valid': False,
            'message': str(e),
            'errors': []
        }), 400

    # TODO: check if the config instances being deployed are valid
    print(cfgInstDeployment)

    # return a valid response
    return jsonify({
        'valid': True,
        'message': 'ok',
        'errors': []
    }), 200


if __name__ == "__main__":
    app.run()
