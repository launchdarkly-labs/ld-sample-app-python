import os
from flask import Flask
from flask import render_template
from flask import make_response
from flask_cors import CORS
import ldclient
from ldclient.config import Config

app = Flask(__name__)
CORS(app)


class change_tracker:
    def __call__(self, changed):
        print(
            "Old value: "
            + str(changed.old_value)
            + ", New value: "
            + str(changed.new_value)
        )


changer = change_tracker()

ldclient.set_config(Config(os.environ["LD_SDK_KEY"]))

if ldclient.get().is_initialized():
    print("SDK successfully initialized!")
else:
    print("SDK failed to initialize")

mycontext = ldclient.Context.from_dict(
    {
        "key": "018e7bd4-ab96-782e-87b0-b1e32082b481",
        "kind": "user",
        "name": "Could be anyone",
    }
)

ldclient.get().flag_tracker.add_flag_value_change_listener(
    "test-flag", mycontext, changer
)


@app.route("/")
def show_page():
    retval = make_response(render_template("index.html"))
    return retval


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
