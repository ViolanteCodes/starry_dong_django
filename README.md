# Starry Dong Django

![A Screenshot of the Landing Page](root/images/git_screenshots/screenshot_landing.png?raw=True "A screenshot of the landing page")

![A Screenshot of the Short Fiction Page](root/images/git_screenshots/screenshot_fiction.png?raw=True "A screenshot of the Short Fiction page")

Hello! Welcome to Starry_Dong_Django, a Django site built by me,
Maria Violante, using the Django web framework for Python. Although this
is a personal project that's somewhat on the simple side, I'm quite
proud of it! This project is for an author / short fiction writer that
also does developmental and line-editing, so all models and views have
been tailored with that in mind.

## Features
Starry_Dong_Django features:

### Django Apps

This project has been subdivided into a number of functional apps,
including:
- a simple blog app with list and detail views
- a contact app for contact forms
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
- We're in the home stretch! There's just some final styling to do, as
well as the 404 page and all that jazz, and then we'll be moving on
to the next step: deployment on a host server!
