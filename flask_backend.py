from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    with open("data/total_project.txt", "r") as file:
        total_project = len(file.readlines())
    with open("data/total_unmaintained.txt", "r") as file:
        total_lost = len(file.readlines())
    with open("data/total_api.txt", "r") as file:
        total_api = len(file.readlines())
    return render_template("main.html", total_project=total_project, 
    total_unmaintained=total_lost, total_api=total_api)

@app.route("/project")
def project():
    with open("data/total_project.txt", "r") as file:
        all_project = []
        project = file.readlines()
        total_project = len(project)
        for lines in project:
            striped = lines.strip("\n")
            all_project.append(striped)
        string_all_project = ", ".join(all_project)
    with open("data/total_unmaintained.txt", "r") as file:
        all_unmaintained = []
        unmaintained = file.readlines()
        total_unmaintained = len(unmaintained)
        for lines in unmaintained:
            striped = lines.strip("\n")
            all_unmaintained.append(striped)
        string_all_unmaintained = (", ").join(all_unmaintained)
    with open("data/total_api.txt", "r") as file:
        all_api = []
        api = file.readlines()
        total_api = len(api)
        for lines in api:
            striped = lines.strip("\n")
            all_api.append(striped)
        string_all_api = ", ".join(all_api)
    return render_template("project.html", project=string_all_project, 
    total_project=total_project, unmaintained=string_all_unmaintained, 
    total_unmaintained=total_unmaintained, api=string_all_api,
    total_api=total_api)

if __name__ == "__main__":
    app.run(debug=True)