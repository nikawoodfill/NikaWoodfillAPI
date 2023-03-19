from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hiya! I am a software engineer that enjoys linking humanities questions to real-world data and technology. I studied data science and history at Wesleyan University and worked in insights and analytics. I decided I wanted to spend more time coding and building tools so I attended Hack Reactor this winter.I currently live in Brooklyn and you can usually find me in a coding rabbit hole or on a mountain!!"


@app.route('/skills/')
def skills():
    return jsonify(["JavaScript (ES5 and ES6)", "TypeScript", "Python", "HTM5", "CSS", "Python", "R", "Markdown", "React", "Node.js", "Next.js", "Express", "PostgreSQL", "MongoDB", "Docker", "AWS", "Flask"])


@app.route('/experience/')
def experience():
    return jsonify(
        {"Role": "Software Engineering Immersive Resident",
         "Company": "Galvanize Inc",
         "Description": "Three-month residency supporting the delivery of Galvanize Software Engineering curriculum. Conducted office hours with junior engineers on programming fundamentals, data structures/algorithms, and modern web development technologies",
         "Date": "Present"},
        {"Role": "Insights Fellow",
         "Company": "Bully Pulpit Institute",
         "Description": "Proofed survey results and questionnaires for a variety of clients. Automated Topline production using R and Crunch.io. Assembled research and polling briefs to provide relevant information for clients",
         "Date": "2022"},
        {"Role": "Data Research Analyst",
         "Company": "LivLet", "Description": "Spearheaded data and research projects for an intelligent home management start-up. Engineered data infrastructure based on growth and priorities. Advised marketing and UX designers using Google Analytics and market research.",
         "Date": "2021-2022"},
        {"Role": "Computer Science Teaching Assistant",
         "Company": "Wesleyan University",
         "Description": "Graded student homework and coding assignments, oversaw review sessions and lab tutorials",
         "Date": "2020"},
        {"Role": "Code Coach",
            "Company": "The Coder School",
            "Description": "Taught students beginning to intermediate computer science concepts. Created individualized learning plans for each client based on interests and learning styles",
            "Date": "2018"})


@app.route('/joke/')
def joke():
    return "A programmer was arrested for writing unreadable code. He refused to comment"
