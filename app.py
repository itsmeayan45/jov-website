from flask import Flask, render_template

app = Flask(__name__)

# Dummy job data
jobs = [
    {
        "title": "Frontend Developer",
        "company": "Google",
        "location": "Bangalore, India",
        "type": "Full-time",
        "salary": "₹12-18 LPA"
    },
    {
        "title": "Backend Developer",
        "company": "Amazon",
        "location": "Hyderabad, India",
        "type": "Full-time",
        "salary": "₹15-22 LPA"
    },
    {
        "title": "UI/UX Designer",
        "company": "Zomato",
        "location": "Delhi, India",
        "type": "Contract",
        "salary": "₹8-10 LPA"
    },
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jobs')
def jobs_page():
    return render_template('jobs.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
