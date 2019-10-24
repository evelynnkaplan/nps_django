# Digital Ecosystem for National Park Service Annual Passholder Program
#### Capstone Project - Evelynn Kaplan - Ada Developers' Academy

## Table of Contents

* [Introduction and Technologies](#introduction-and-technologies)
* [Django webapp](#django-webapp)
* [Data visualization dashboard](#data-visualization-dashboard)
* [React Native app](#react-native-app)

## Introduction and Technologies

**The problem**: 

The National Park Service of the United States has no database or other digital system storing records of annual passes sold to park visitors. Park rangers cannot look up visitors' annual passes at the gate, so passholders must have a physical pass to be admitted without paying an entrance fee.

[**The product plan**](https://gist.github.com/evelynnkaplan/aa86a18597134093e3f1d5f3a4e5a0e0)

**The solution**: 

A three-part digital ecosystem:
  * Database, custom REST API, interfaces for park rangers and passholders
    * [Deployed webapp](https://mynpspass.herokuapp.com/)
    * Built with Django 2.2, Python 3.7 and PostgreSQL 11.3
    * Stored in this repository
    
  * Data visualization dashboard
    * [Deployed site](https://npspassdashboard.herokuapp.com/)
    * Built with Python 3.7 and Plotly 4.0/Dash 1.0
    * Data from the custom Django REST API
    * [Github repository](https://github.com/evelynnkaplan/nps_dashboard)
    
  * Mobile app with digital annual pass that can be accessed offline
    * [Video demo](https://drive.google.com/file/d/1M_hOIoXD3JjD6FjJD7LrM_jP_-v37EG9/view?usp=sharing)
    * [Expo build of app](https://expo.io/@ekaplan/nps_app)
    * Built with React Native 0.59 and Expo 3.0
    * Data from the custom Django REST API
    * [Github repository](https://github.com/evelynnkaplan/nps_app)

## Django webapp

### Use cases

* Customized Django admin interface for park rangers enables park rangers to search for passholders by name and check them in at park gates. Park rangers can add new passholders to the database after selling a new pass. See [example in slide deck](https://docs.google.com/presentation/d/1c0iNtTjD489KFqzCfr8Unnl3YNIbn_qqdi5WxMbl59I/edit#slide=id.g5e2c72d3ff_0_2).
* [Interface for passholders](https://mynpspass.herokuapp.com/) enables passholders who bought their passes at a point-of-sale other than a national park gate (for example, through REI) to register their pass information for quicker look-up at park gates.

### Installation Instructions
1. If this is your first time using Django, follow [Django's quick install guide](https://docs.djangoproject.com/en/2.2/intro/install/).
2. If this is your first time using PostgreSQL, [download PostgreSQL](https://www.postgresql.org/download/).
3. Clone this repository and `cd nps_django`
4. `pip install -r requirements.txt`
5. `python3 manage.py runserver`
6. Visit http://127.0.0.1:8000/ or whatever localhost your server is running in.

## Data visualization dashboard

### Use case

* This [data visualization dashboard](https://npspassdashboard.herokuapp.com/) allows the National Park Service to easily understand passholder data. Now that the National Park Service has a database with information about passholders and pass usage, the National Park Service can use that data to make better decisions about its annual pass program, and to more effectively market to potential passholders.  _Note: the data shown is based on fake seed data and does not represent real statistics._

### Installation Instructions
1. Clone this repository and `cd nps_dashboard`
2. `pip install -r requirements.txt`
3. `python3 app.py`
4. Visit http://127.0.0.1:8050/ or whatever localhost your server is running in.

## React Native app

### Use cases

* This cross-platform mobile app allows users to access their annual pass and pass visit history offline. Passholders can access a scannable barcode of their annual pass that park rangers with scanning devices can scan to find the user in the database. The barcode corresponds to the passholder's pass ID.
* New users can get access to their annual pass and visit history if they create an account using the email address tied to their annual pass.
* Users can access their data offline if they are already logged in to the app with the email address tied to their annual pass.
* [Video showing user flow of a logged-in user](https://drive.google.com/file/d/1M_hOIoXD3JjD6FjJD7LrM_jP_-v37EG9/view?usp=sharing), including offline mode

### Installation Instructions
1. If this is your first time using Node.js and npm, [download Node.js](https://nodejs.org/en/).
2. Install the Expo command line utility with `npm install -g expo-cli`
3. Clone the repository and `cd nps_app`
4. `npm install`
5. [Download the Expo client](https://docs.expo.io/versions/v35.0.0/get-started/installation/#2-mobile-app-expo-client-for-ios) for the cell phone you want to test the app on.
6. `npm start` -- this will open up your localhost. If it doesn't open, navigate to whatever localhost your server is running in.
7. Use your cell phone to scan the QR code that appears in the Expo metro bundler and this will open the app on your phone's Expo client.



