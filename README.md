# 2021 CA229 Project02
<h1> Django Project </h1>
<p>This is a social cataloguing website built with Django.</p>
<h2>Project Summary</h2>
<p>Worththeread is a social cataloguing website that allows users to scan various books and provides individuals with the opportunity to truly gage a book before purchasing.
 The website also facilitates users discussions about a specific book(s) with other people via the blog post comment section.</p>
<h2> Code Logic </h2>
<p>
There was only one app called pages, this was where all site pages were created.
All site pages were created on the django admin interface using the Page model.
This also enables the admin to add and remove pages as they see fit.
There were 2 views:</p>

<b>1. Index view <b>

* This accessed the sites saved in the Page model
* Although every page(bar the index.html) had a html file associated with it which inherited the navbar and style from the base.html file
* Pages in sections such as the blog section and invidual book pages also inherited from their respective bases e.g bookbase.html and blogbase.html
* The view would only load if the page is stored in the database within the Page model

<b>2. Contact view <b>

* If it is the users first time (i.e has not submitted a response) on the form, the view will load render a form from contact.py
* When the form is submitted data is validated and a thank you message is rendered.

<p> It is also important to note that a Bootstrap template from a CDN was used to help with site appearance more specifically
     the entire blog section which consists of the blog home and its respective blog posts. </p>
<h2> Web Demo </h2>
<img src="https://j.gifs.com/oZRJVA.gif" alt="pic" />


