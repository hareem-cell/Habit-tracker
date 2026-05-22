**1. HOW TO RUN**

**Step 1**: Install dependencies
Run:
pip install -r requirements.txt
**Step 2**: Start the application
Run:
python app.py
**Step 3:** Open in browser
Go to:
http://127.0.0.1:5000

**2. STACK & DESIGN CHOICES**

I used Flask with HTML, CSS, and JSON storage because it allows fast development of a lightweight web app without complex setup.
**Design decision 1: Weekly grid layout**
I used a grid instead of a list because habits need to be visually tracked across days of the week. The grid makes comparison between days easier and more intuitive.
**Design decision 2: Dark green dashboard theme**
I used a dark green container with muted tones to reduce eye strain and create a focused productivity environment. The contrast between sections improves 
readability.

**3. RESPONSIVE AND ACCESSIBILITY**
......Responsive behavior:
On larger screens (laptops), the grid displays all 7 days clearly in one row. On smaller screens (mobile), the layout compresses but remains readable due to grid 
flexibility.
......Accessibility consideration:
I used checkbox inputs for each day, which supports keyboard navigation and screen readers.
.....Skipped accessibility feature
I did not fully implement ARIA labels or advanced screen-reader optimizations due to my knowledge limits.

**4. AI usage**

I used AI (ChatGPT) for:
may be i used it a lot due to my limitations , i only knew python and c++ basics but c++ is not suggested in web application development then i got to know that i 
can use python with the help of flask web app can be made , my code or developing process of application was more like learning new things beacuse the code written
json, css, html is all from ai , i just prompted it , checked by running if my tequirements are fulfilled
but one thing i liked abou my work i didn't gave the whole project statement to ai to make it and give me readymade version, i moved step by step , then a little
modification , then test it then next step and so on
for example i first just amde files that needed then created link between them if needed then just set simple style to test then changed style , color etc and 
similarly everything else

**5. honest gap**
i am not satisfied with past and next week setting yet
its also not polished for small screen mobile devices
improve grid design
