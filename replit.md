# Number Microscope

## Overview

Number Microscope is a Flask-based web application that analyzes numeric patterns by extracting and examining the first digits of integer and fractional parts of numbers. The application implements a custom "microscope" algorithm that transforms any number into a pattern format "X.Y" where X is the first digit of the integer part and Y is the first digit of the fractional part. Users can analyze single numbers or sequences of numbers through a web interface, with results displayed in a clean, dark-themed Bootstrap UI.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask's built-in rendering
- **UI Framework**: Bootstrap 5 with dark theme for responsive design
- **Styling**: Custom CSS with Font Awesome icons for enhanced user experience
- **Structure**: Base template with inheritance for consistent layout across pages

### Backend Architecture
- **Web Framework**: Flask with modular route organization
- **Application Structure**: 
  - Main application factory in `app.py` with configuration setup
  - Route handlers separated in `routes.py` for clean separation of concerns
  - Core algorithm logic isolated in `number_microscope.py` module
- **Session Management**: Flask sessions with configurable secret key
- **Error Handling**: Try-catch blocks with user-friendly flash messages
- **Input Processing**: Custom parsing functions to handle various number formats

### Core Algorithm
- **Number Microscope Function**: Extracts first digits from integer and fractional parts
- **Sequence Analysis**: Batch processing of multiple numbers with error tolerance
- **Pattern Recognition**: Transforms numeric inputs into standardized X.Y format
- **Validation**: Robust input validation with graceful error handling

### Deployment Configuration
- **WSGI Setup**: ProxyFix middleware for proper header handling behind reverse proxies
- **Environment Variables**: Configurable session secrets for production deployment
- **Debug Mode**: Development-friendly debugging enabled for local testing

## External Dependencies

### Python Packages
- **Flask**: Core web framework for application routing and templating
- **Werkzeug**: WSGI utilities including ProxyFix middleware

### Frontend Libraries
- **Bootstrap 5**: CSS framework loaded via CDN for responsive design
- **Font Awesome**: Icon library loaded via CDN for enhanced UI elements

### Development Tools
- **Python Logging**: Built-in logging module for debugging and monitoring
- **Flask Development Server**: Built-in server for local development

### Hosting Environment
- **Replit**: Platform-optimized with host configuration for '0.0.0.0' binding
- **Environment Variables**: Support for production configuration via environment variables