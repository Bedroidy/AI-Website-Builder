from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form["user_name"]
        bio = request.form["bio"]
        template_type = request.form["template"]

        # Redirect to the appropriate template page
        return redirect(url_for(template_type, user_name=user_name, bio=bio))

    return render_template("home.html")


@app.route("/portfolio")
def portfolio():
    user_name = request.args.get("user_name")
    bio = request.args.get("bio")

    # Sample project data; in a real-world app, this would be dynamic
    projects = [
        {"title": "Project 1", "description": "A great project about AI."},
        {"title": "Project 2", "description": "A web development project."},
        {"title": "Project 3", "description": "A data science project."},
    ]
    
    return render_template("portfolio_template.html", user_name=user_name, bio=bio, projects=projects)


@app.route("/blog")
def blog():
    user_name = request.args.get("user_name")
    bio = request.args.get("bio")

    # Sample blog posts; this data would normally come from a database
    posts = [
        {"title": "First Post", "content": "Welcome to my blog! Here's my first post."},
        {"title": "Second Post", "content": "Learning how to build a website with Flask."},
    ]
    
    return render_template("blog_template.html", user_name=user_name, bio=bio, posts=posts)


@app.route("/photography")
def photography():
    user_name = request.args.get("user_name")
    bio = request.args.get("bio")

    # Sample photo data; in a real application, this would come from user input or a database
    photos = [
        {"url": "/static/photo1.jpg", "title": "Nature", "description": "A beautiful landscape."},
        {"url": "/static/photo2.jpg", "title": "City", "description": "The skyline at dusk."},
    ]
    
    return render_template("photography_template.html", user_name=user_name, bio=bio, photos=photos)


if __name__ == "__main__":
    app.run(debug=True)
