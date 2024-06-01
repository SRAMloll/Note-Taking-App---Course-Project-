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

#route 1: welcome page
@app.route("/")
def homepage():
    return get_html("index")

#route 2: defining the route for saving a new note to the TXT file
@app.route("/createnote")
def create_note():
    html_page = get_html("createnote")
    notedb = open("note.txt", "a" )
    new_note = flask.request.args.get("newnote")
    notedb.write(new_note + "\n")
    notedb.close 
    return html_page.replace("$$note$$","Your note is saved!")


#route 3: defining the route for reading the txt file
@app.route("/viewnotes")
def view_note():
    html_page = get_html("viewnotes")
    notes = get_note()
    actual_notes = ""
    for note in notes:
        
        #providing alternative text if the txt file is empty
        if len(actual_notes) == 0:
            actual_notes = "<p> There is no note yet. Please create a note! </p>"

        #providing result if the TXT file contains notes
        else:
            actual_notes += "<p>" + note + " </p>"
    
    return html_page.replace("$$notes$$", actual_notes)
    
    
         
#route 4: defining the route for searching within the txt file
@app.route("/search")
def note_search():
    html_page = get_html("search")
    notes = get_note()
    note_query = flask.request.args.get("query")
    note_found = ""
    for note in notes:
        if note.lower().find (note_query.lower()) != -1 :
            note_found += "<p>" + note + "</p>"

    #alternative text is the search result is negative
    if note_found == "":
            note_found = "No note with this/these word(s) were found."
    return html_page.replace("$$notes$$", note_found)



