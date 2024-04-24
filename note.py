import flask

app = flask.Flask("note")

def get_html(page_name) :
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_note():
    notedb = open("note.txt")
    content = notedb.read()
    notedb.close()
    note_to_display = content.split("\n")
    return note_to_display


@app.route("/")
def homepage():
    return get_html("index")

@app.route("/viewnotes")
def view_note():
    html_page = get_html("viewnotes")
    notes = get_note()
    actual_notes = ""
    for note in notes:
        actual_notes += "<p>" + note + " </p>"
    
    if len (actual_notes) != 0:
            return html_page.replace("$$notes$$", actual_notes)
    else:
         return html_page.replace("$$notes$$", "<p> There is no note yet. Please create a note! </p>")
    
            

@app.route("/search")
def note_search():
    html_page = get_html("viewnotes")
    notes = get_note()
    note_query = flask.request.args.get("q")
    note_found = ""
    for note in notes:
        if note.lower().find (note_query.lower()) != -1 :
            note_found += "<p>" + note + "</p>"
    if note_found == "":
            note_found = "No note with this/these word(s) were found."
    return html_page.replace("$$notes$$", note_found)

