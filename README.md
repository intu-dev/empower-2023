# Empower 2023

Commercial Intuition were proud to support the CyberFirst Empower event in 2023.  

We ran an activity which challenged the girls to fix a "hacked" football VAR system so they could score a goal.  Along the way they had to solve a number of clues to find passwords, and then modify some Python code.

This is the application which contained the password and coding challenge.

For more information on CyberFirst, see here:
https://www.ncsc.gov.uk/cyberfirst/overview


## Running Locally

To run & debug locally:

`pip install -r requirements.txt`

`flask --app app/__init__.py --debug run`

View the site at http://127.0.0.1:5000/


## Creating a docker image

The docker image hosts the app in Waitress, which exposes port 80.

To build:
`docker build -t empower .`

Or on an Apple Silicon Mac: 
`docker buildx build --platform linux/amd64 -t empower .`

To run the image locally:
`docker run -p 5000:80 empower`


## Credits

Many thanks to the following:
* Terminal styling borrowed from - Advent of Code (https://adventofcode.com/) 
* CSS Fireworks from https://alvaromontoro.com/blog/68002/creating-a-firework-effect-with-css