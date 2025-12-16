import os
from flask import Flask
from flask import render_template
from flask import make_response
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def show_page():
    current_route_rule = str(request.url_rule)
    retval = make_response(
        render_template(
            "index.html",
            current_route_rule=current_route_rule,
        )
    )
    return retval


@app.route("/about")
def show_about():
    current_route_rule = str(request.url_rule)
    retval = make_response(
        render_template("about.html", current_route_rule=current_route_rule)
    )
    return retval


@app.route("/products")
def show_products():
    current_route_rule = str(request.url_rule)
    retval = make_response(
        render_template("products.html", current_route_rule=current_route_rule)
    )
    return retval


@app.route("/contact")
def show_contact():
    current_route_rule = str(request.url_rule)
    retval = make_response(
        render_template("contact.html", current_route_rule=current_route_rule)
    )
    return retval


@app.route("/api/banner")
def home_page_banner():
    primary_banner = ldclient.get().variation(
        "banner-text", mycontext, "No banner text found!"
    )
    return {"primaryBanner": primary_banner}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
