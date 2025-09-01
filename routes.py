from flask import render_template, request, flash, redirect, url_for
from app import app
from number_microscope import number_microscope, analyze_sequence, parse_number_input


@app.route('/')
def index():
    """Main page with input form for numbers."""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Process the submitted numbers and show results."""
    try:
        # Get input from form
        numbers_input = request.form.get('numbers', '').strip()
        
        if not numbers_input:
            flash('Please enter at least one number to analyze.', 'warning')
            return redirect(url_for('index'))
        
        # Parse the input numbers
        numbers = parse_number_input(numbers_input)
        
        if not numbers:
            flash('No valid numbers found in the input. Please check your format.', 'error')
            return redirect(url_for('index'))
        
        # Analyze the sequence
        analysis = analyze_sequence(numbers)
        
        # Check if all numbers failed to process
        valid_results = [r for r in analysis['results'] if r['error'] is None]
        if not valid_results:
            flash('All entered numbers were invalid. Please check your input format.', 'error')
            return redirect(url_for('index'))
        
        # Show warning if some numbers failed
        failed_results = [r for r in analysis['results'] if r['error'] is not None]
        if failed_results:
            failed_numbers = [r['original'] for r in failed_results]
            flash(f'Some numbers could not be processed: {", ".join(failed_numbers)}', 'warning')
        
        return render_template('results.html', 
                             analysis=analysis,
                             total_numbers=len(numbers),
                             valid_numbers=len(valid_results))
    
    except Exception as e:
        app.logger.error(f"Error in analyze route: {str(e)}")
        flash('An error occurred while processing your numbers. Please try again.', 'error')
        return redirect(url_for('index'))


@app.route('/single', methods=['POST'])
def analyze_single():
    """Analyze a single number via AJAX-like form submission."""
    try:
        single_number = request.form.get('single_number', '').strip()
        
        if not single_number:
            flash('Please enter a number to analyze.', 'warning')
            return redirect(url_for('index'))
        
        # Analyze single number
        try:
            pattern = number_microscope(single_number)
            analysis = {
                'results': [{
                    'original': single_number,
                    'pattern': pattern,
                    'error': None
                }],
                'fractional_sequence': [pattern.split('.')[1]],
                'fractional_pattern': pattern.split('.')[1]
            }
            
            return render_template('results.html', 
                                 analysis=analysis,
                                 total_numbers=1,
                                 valid_numbers=1,
                                 single_mode=True)
        
        except ValueError as e:
            flash(f'Invalid number format: {single_number}', 'error')
            return redirect(url_for('index'))
    
    except Exception as e:
        app.logger.error(f"Error in analyze_single route: {str(e)}")
        flash('An error occurred while processing your number. Please try again.', 'error')
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('base.html', 
                         content='<div class="text-center"><h2>Page Not Found</h2><p>The page you are looking for does not exist.</p></div>'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    app.logger.error(f"Internal server error: {str(e)}")
    return render_template('base.html', 
                         content='<div class="text-center"><h2>Internal Server Error</h2><p>Something went wrong. Please try again later.</p></div>'), 500
