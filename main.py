import sys
import os
import json

def main(cdir, mdir, argv):
    # Creating the boilerplate for the filetype
    try:
        author_name = argv[1] # Author name
        file_type = argv[2].lower() # File type
        JSON_data = True if len(argv) == 4 else False
        # check if consfig.JSON is wanted
        report_name = author_name + "_report"
    except:
        sys.exit("Error in arguments, code: 235")
    
    os.system(f"mkdir " + mdir + f"/{report_name} && cd " + mdir \
              + f"/{report_name} && mkdir " + mdir + f"/{report_name}/images")

    if JSON_data:
        with open(cdir + "/config.JSON", "r") as f:
            data = json.load(f)
            author: str = data["author"]
            title: str = data["title"]
            subtitle: str = data["subtitle"]
            headings: bool = data["headings"]
    else: # Use default data
        author = author_name
        title = "Title"
        subtitle = "Subtitle"
        headings = True

    file_end = ""  # Initialize the variable outside the match statement

    if file_type in ["md", "markdown", "mdown", "markup"]:
        file_end = "md"
    elif file_type in ["html", "page", "webpage"]:
        file_end = "html"
    elif file_type in ["tex", "latex"]:
        file_end = "tex"

    print(author, title, subtitle, headings, file_end)

    # Grab data from content directory

    if file_end == "md" or file_end == "html":
        if headings:
            with open(cdir + "/content/headings.txt", "r") as f:
                headings_style = f.read()
        
        with open(cdir + "/content/mathjax.txt", "r") as f:
            heading_jax = f.read()

        with open(cdir + "/content/titlepage.txt", "r") as f:
            title_page = f.read()
    
        # Edit title page to include the author, title and subtitle
        title_page = title_page.replace("report_author", author)
        title_page = title_page.replace("report_title", title)
        title_page = title_page.replace("report_subtitle", subtitle)
        
        # Order of writing is mathjax script, then headings, then title page
        with open(mdir + f"/{report_name}/{report_name}.{file_end}", "w") as f:
            f.write(heading_jax)
            if headings:
                f.write(headings_style)
            f.write(title_page)
    
    # Support for latex not included yet lol
            
    #unlucky
    
    sys.exit("Created file, exiting program")



if __name__ == '__main__':
    cdir = os.path.dirname(os.path.abspath(__file__))
    mdir = os.getcwd()
    main(cdir, mdir, sys.argv)