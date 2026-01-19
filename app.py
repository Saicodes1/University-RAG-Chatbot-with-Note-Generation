from LLM_response import response
from flask import Flask,request,jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask import send_from_directory

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_question=db.Column(db.String(10000))
    bot_answer=db.Column(db.String(10000))

class Chat1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_question=db.Column(db.String(10000))
    bot_answer=db.Column(db.String(10000))
@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/compiler_construction", methods=["GET","POST"])
def compiler_construction():
    if request.method=="POST":
        data = request.get_json()
        user_query = data["message"]

        reply = response(user_query,"Compiler_Construction", Chat)
        if reply.startswith("generated"):
            download_url=f"/download/{os.path.basename(reply)}"
            return jsonify({"reply":"Notes generated","filepath": download_url})
        else:
            chat_entry = Chat(user_question=user_query,bot_answer=reply)
            db.session.add(chat_entry)
            db.session.commit()
            return jsonify({"reply": reply})

    return render_template("compiler_construction.html")

@app.route("/computer_networks",methods=["POST","GET"])
def computer_networks():
    if request.method=="POST":
        data=request.get_json()
        user_query=data["message"]

        reply = response(user_query,"Computer_Networks", Chat1)
        chat_entry = Chat1(user_question=user_query,bot_answer=reply)
        db.session.add(chat_entry)
        db.session.commit()
        return jsonify({"reply": reply})
    return render_template("computer_networks.html")

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory("generated_notes", filename, as_attachment=True)

if __name__ == "__main__":
    app.run()