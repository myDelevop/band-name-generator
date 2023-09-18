from flask import Flask, render_template, request
import requests
import os
import smtplib

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

#
#
# @app.route("/form-entry", methods=["POST", "GET"])
# def receive_data():
#     return "<h1> Successfully sent your message</h1>"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    method = request.method
    if method == "GET":
        print("I am here GET")
        return render_template("contact.html", msg_sent=False)
    elif method == "POST":
        print("I am here POST")
        send_email(request.form)

        return render_template("contact.html", msg_sent=True)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(contact_data):
    from_address = contact_data["email"]
    to_address = "rockdesires@gmail.com"
    password = os.environ.get("EMAIL_PROVIDER_TOKEN")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=to_address, password=password)

        connection.sendmail(from_addr=from_address,
                            to_addrs=to_address,
                            msg=f"Subject:Message from {contact_data['name']} No. {contact_data['phone']}\n\n"
                                f"{contact_data['message']}")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
