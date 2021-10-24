from flask import Flask, render_template, request
import redis


app = Flask(__name__) # instanciation de la classe Flask
cache = redis.Redis(host='redis', port=6379, db=0)

@app.route("/")
def citationForm():
  if len(request.args) == 0: # pas de QueryString
    return render_template("citationForm.html")
  else: # QueryString présente, contient des paramères
    citation = request.args["citation"]
    author = request.args["author"]

    cache.incr('hits')
    hitNumber = cache.get('hits')
    cache.set({str(hitNumber): {"citation": citation , "author": author}})
    return f"You filled up the database with -> citation: {citation} --- author: {author} (Input number {hitNumber})"
  

app.run(host="0.0.0.0", port=8080)