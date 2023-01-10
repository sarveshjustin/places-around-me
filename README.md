# Places Around Me
## AIM:
To develop a website to display details about saveetha block of medical.

## Design Steps:

### Step 1:
Create a new django project and app
### Step 2:
Add a new imagemap html file in templates and neede images in static folder and define it in settings.
### Step 3:
Type ur image map code in the html with coordinates and target file to redirect on click
### Step 4:
Define your components pages and create content in such a way that it gives information about place which is being clicked
### Step 5:
Include pictures and contents for your subpages and map them using urls and views

## Code:
```
{% load static %}

<html>
    <head>
        <title>SEC</title>
        <link rel="stylesheet" type="text/css" href="{% static 'css/index.css' %}">
    </head>
    <body>

        <h3>Address:</h3><p> Maduravoyal, Chennai, Tamil Nadu 600077</p>
        
        <img id="Image-Maps-Com-image-maps-2023-01-10-032237" src="{% static 'img/place.png' %}" border="0" width="1518" height="786" orgWidth="1518" orgHeight="786" usemap="#image-maps-2023-01-10-032237" alt="" />
<map name="image-maps-2023-01-10-032237" id="ImageMapsCom-image-maps-2023-01-10-032237">
<area id="scop" alt="" title="scop" href="scop" shape="rect" coords="678,173,861,305" style="outline:none;" target="_self"     />
<area id="physiotheraphy" alt="" title="physiotheraphy" href="physiotheraphy" shape="rect" coords="393,151,580,277" style="outline:none;" target="_self"     />
<area id="ahs" alt="" title="ahs" href="ahs" shape="rect" coords="365,321,537,469" style="outline:none;" target="_self"     />
<area id="ot" alt="" title="ot" href="ot" shape="rect" coords="178,237,355,334" style="outline:none;" target="_self"     />
<area id="control care" alt="" title="control care" href="controlcare" shape="rect" coords="1199,0,1505,776" style="outline:none;" target="_self"     />
<area shape="rect" coords="1516,784,1518,786" alt="Image Map" style="outline:none;" title="Image Map" href="https://www.image-maps.com/" />
</map>


    </body>
</html>
```
## Output:
![output](place%20around.png)

## Result:
Thus a website is developed to display details about saveetha block of medical.
