# Astronomy-CAS---Observation-Prototype
Prototype application to track local light pollution data, celestial object trajectories and weather to aid astronomy observation.

## Overview
This project helps users choose better locations and times for observing the night sky. By selecting a point on the map, users can view:

- local weather conditions
- light pollution data
- the position of selected celestial objects

The goal is to make astronomy observation more accessible and practical for students and beginners.

## Features
-Retrieve weather data for a selected coordinate
-Use Nasa Horizons API to track positions of celestial objects
-Use VIIRS Satellite data to find local artificial light levels
-Combines data into a dashboard on the web application

## Roadmap:
1. Core data/API work:
   Weather API (Open Weather Map)
   Celestial Object trajectories with NASA horizons system
   Light pollution dataset with NASA Black Marble

2. User Interface:
   Global Map for users to pick location
   Home pages, dashboard
   
3. Testing and feedback
   Bug fixing
   Design improvements  

## Installation
1. Clone the repository
2. Create and activate a Python virtual environment
3. Install dependencies (in requirements.txt)
4. Run backend app.py
5. Open frontend pages with browser

## Credits
NASA Horizons System for celestial object ephemeris data
OpenMeteo for weather data
NASA Black Marble / VIIRS-based night light data for light pollution analysis

 - Developed as part of the Astronomy CAS initiative, combining astronomy with computer science to create a practical observation tool.