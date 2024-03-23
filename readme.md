# Script writer
<sup>Written by Harry Hescott</sup>

### Why?

I created this software to assist in developing lab scripts for my course, it is very simple and creates folders similar to a venv command

### Structure

- foldername
    - report_author
    - /images

### Usage

This tool is to be added to your path or git cloned via the use of the `git` command on your chosen os.

A config.JSON file can be supported, a template is included to modify if needed, otherwise see appendix for JSON structure.

`git clone https://site.com`

Linux: `python3 makescript.py [folder name] [JSON]`

JSON can be true / "JSON" or false / blank entirely

Note: Windows uses `python`, not `python3`

### Supported filetypes - case insensitive

Markdown:
- md
- markdown
- mdown
- markup

HTML:
- HTML
- page
- webpage

Latex (JSON unsupported):
- LaTeX
- TeX

### Notes

This project was designed with a barebones approach in mind, I personally use a few extensions on VSCode - markdown PDF specifically - to add some richtext features to my documents.

```JSON
report = {
    "author": "Name",
    "title": "Report title",
    "sub": "subtitle",
    "headings": ""
}
```

Headings are similar to how they work in word but instead are written in CSS and only work for MD and HTML.

Headings options are:
- Default: The same options I use, which can be seen in headings.css
- None: Does not add headings, the JSON object can be left blank or have "None"
- Custom: Creates headings 1 through 4 with no values other than the custom CSS fields, i.e `font-size`, `font-family` etc.