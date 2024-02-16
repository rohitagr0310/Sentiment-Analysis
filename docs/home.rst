Home Page
=========

The following HTML code is designed for a web application that performs sentiment analysis. It includes a simple form for users to input text and receive sentiment analysis results.

Introduction
------------

1. **HTML Structure:**
   - `<!DOCTYPE html>`: Declares the document type and version of HTML.
   - `<html>`: Root element of the HTML document.
   - `<head>`: Contains metadata like character set and viewport settings.
   - `<body>`: Main content of the HTML document.

2. **Title and Heading:**
   - `<title>`: Sets the title of the web page.
   - `<h1>`: Main heading for the sentiment analysis application.

3. **Documentation Link:**
   - A link to the documentation is provided, pointing to the `serve_docs` route with the filename `index.html`.

4. **Form for Text Input:**
   - A form is created with a text area for users to input text for sentiment analysis.
   - The form uses the `post` method and points to the `home` route for analysis.

5. **Result Display:**
   - If analysis results are available (`result` exists), a section displays the pipeline, VADER, and Roberta model results.


.. raw:: html

   <div style="text-align: center;">
       <a class="btn" href="index.html">Go back to home page</a>
   </div>

.. raw:: html

   <div style="text-align: center;">
       <a class="btn" href="http://127.0.0.1:5000/">Go back to base URL</a>
   </div>

