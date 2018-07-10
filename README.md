# GenomicPredictionCodingAssessment
Simple webserver running django 2.0 and MySQL for coding assessment.
Asynchronous Email service using Amazon SQS, Sendgrid, and Celery 3.1.25
Implemented middleware to force user login to view any of the pages.

  Front-end was designed by simply using Bootstrap 4.1.1 and Django's built in templating tool. 
For the following requirement:
"Use any of the many standard front-end frameworks to enhance the presentation of the site
(Angular, React, Vue etc.)."
  I wasn't sure whether using one of those javascript frameworks was a requirement, or if "standard front-end framework" included
Bootstrap, Semantic UI, and other CSS libraries. 

  I forewent the Single Page App route with the javascript frameworks primarily because
it was somewhat counterintuitive with the Django's templating tools. I could have used Vue/React to create components and loaded them 
onto a Django template, but I felt that it did not provide much functionality. I apologize if I misinterpretted the requirement.


Future Improvements
  - Improved error messages on forms
  - Refactor code to be more DRY, especially the templating and views.
  - Optimizing the database queries. I didn't take any special consideration for redundant or inefficient database queries simply because of the scale of this app.
  - Split single "monolithic" app into multple smaller apps for improved modularity and maintainability.
  - Perhaps add a RESTful API, which would allow for full utilization of a Front-end JS framework.
  - Create tests for further development
  - Dynamic forms for adding items to an order. Add Line button, instead of generating 5 extra lines initially.
