# Starry Dong Django

![A Screenshot of the Landing Page](static/images/git_screenshots/screenshot_landing.png?raw=True "A screenshot of the landing page")

![A Screenshot of the Short Fiction Page](static/images/git_screenshots/screenshot_fiction.png?raw=True "A screenshot of the Short Fiction page")

Hello! Welcome to Starry_Dong_Django, a Django site built by me,
Maria Violante, using the Django web framework for Python. 
Although this is a personal project and somewhat on the simple side,
with primarily function-based vs class-based views, it's my first
Django project, and I'm quite proud of it!

This project is for an author / short fiction writer that
also does developmental and line-editing, so all models and views have
been tailored with that in mind.

## Features
Starry_Dong_Django features:

### Django Apps

This project has been subdivided into a number of functional apps,
including:
- a simple blog app with list and detail views
- a contact app for contact forms, using django simple-recaptcha
- testimonials app for editorial testimonials, which generates an
internally-linked testimonials page (pull quotes linked to full reviews
by leveraging primary keys.)
- And a short fiction/writing app, which features a number of models,
including: Piece, which allows for cover-image upload and utilizes a 
Many-to-Many relationship with Genre model, as well as a Review model
for short fiction reviews and Publisher model for markets that 
utilize one-to-many Foreign-Key relationships.
- The short fiction app also includes custom views, including detailed
views for all pieces, a condensed bibliographic view, and genre-sorted
views for pieces only in specific fiction genres.

Additionally, secrets required by the project (keys, email passwords,
etc, are stored in a secrets.json file, with a get_secret() function
written into settings to make for easier and more secure deployment.)

### CSS and Javascript
- A custom javascript + CSS theme, "Starry Dong", which features high-
contrast text and larger than average fonts chosen for readability, in
in an effort to increase accessibility for those with visual impairments.
- Beautiful, full-screen parallax scrolling display with animation.
- Fully responsive; mobile-breakpoints implemented through media
queries, viewport and other relative units, and a frankly ridiculous
amount of flexbox.
- Slideout menu with flexbox header for mobile devices.

### Current Status:
- This project was recently deployed to mariadong.com - first via
shared hosting, but then switched over to pythonanywhere due to some
issues with updating through the admin panel and the limitations of 
shared hosting (django 2.1 only, etc.). 

### Current Plans:

There are some changes that are planned for when I get around to it:
- Add a browser query option to disable animations for improved 
accessibility.
- Figure out how to integrate espeak with django-simple-recatpcha for 
audio captcha option, as it appears python anywhere doesn't currently
support flite.

### Notes on Cloning:

If you'd like to run this project yourself, you can either set up a 
secrets.json file and put in key,value pairs for the options currently
listed with a get_secrets() function in settings.py, or you can just
change those options to your keys for testing.

Additionally, static files will not load in a local environment unless
DEBUG is set to True--as DEBUG==False instead loads them from a local 
environment folder on my hosting server.

Note: Is this great security? Am I breaking the "static root and static
files shouldn't be the same folder rule?" (Yep and yep! But I like 
the convenience of doing a git pull to update my page on PA, and 
nobody pushes into this repo but me!)