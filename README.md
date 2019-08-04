# Digital Ecosystem for National Park Service Annual Passholder Program
#### Capstone Project - Evelynn Kaplan - Ada Developers' Academy

## Table of Contents

* [Introduction and Technologies](#introduction-and-technologies)

## Introduction and Technologies

**The problem**: 

The National Park Service of the United States has no database or other digital system storing records of annual passes sold to park visitors. Park rangers cannot look up visitors' annual passes at the gate, so passholders must have a physical pass to be admitted without paying an entrance fee.

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
    
  * Mobile app with digital annual pass 
    * [Expo build of app](https://expo.io/@ekaplan/nps_app)
    * Built with React Native 0.59 and Expo 3.0
    * Data from the custom Django REST API
    * [Github repository](https://github.com/evelynnkaplan/nps_app)
