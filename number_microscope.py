def number_microscope(number):
    """
    This function acts as a microscope for numbers.
    It zooms in on the first digit of the integer part and the first digit of the fractional part.
    
    Args:
        number: A numeric value (int, float, or string representation)
    
    Returns:
        str: A pattern in the format "X.Y" where X is the first digit of integer part
             and Y is the first digit of fractional part
    """
    try:
        # Convert the number to a string to work with its digits
        num_str = str(float(number))
        
        # Split the number into integer and fractional parts
        parts = num_str.split('.')
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else '0'
        
        # Handle negative numbers - remove the minus sign for digit extraction
        if integer_part.startswith('-'):
            integer_part = integer_part[1:]
        
        # Get the first digit of the integer part (or 0 if it's zero)
        first_int_digit = integer_part[0] if integer_part != '0' else '0'
        
        # Get the first digit of the fractional part
        first_frac_digit = fractional_part[0] if fractional_part != '0' else '0'
        
        # Return the transformed pattern
        return f"{first_int_digit}.{first_frac_digit}"
    
    except (ValueError, TypeError, IndexError) as e:
        raise ValueError(f"Invalid number format: {number}")


def analyze_sequence(numbers):
    """
    Analyze a sequence of numbers using the number microscope algorithm.
    
    Args:
        numbers: List of numbers to analyze
    
    Returns:
        dict: Contains original numbers, patterns, and fractional digit analysis
    """
    results = []
    fractional_digits = []
    
    for number in numbers:
        try:
            pattern = number_microscope(number)
            results.append({
                'original': number,
                'pattern': pattern,
                'error': None
            })
            # Extract fractional digit for sequence analysis
            fractional_digits.append(pattern.split('.')[1])
        except ValueError as e:
            results.append({
                'original': number,
                'pattern': None,
                'error': str(e)
            })
    
    return {
        'results': results,
        'fractional_sequence': fractional_digits,
        'fractional_pattern': ''.join(fractional_digits)
    }


def parse_number_input(input_str):
    """
    Parse input string containing numbers separated by commas, spaces, or newlines.
    
    Args:
        input_str: String containing numbers
    
    Returns:
        list: List of parsed numbers
    """
    if not input_str.strip():
        return []
    
    # Replace common separators with commas and split
    import re
    # Split on commas, spaces, semicolons, or newlines
    number_strings = re.split(r'[,\s;]+', input_str.strip())
    
    numbers = []
    for num_str in number_strings:
        num_str = num_str.strip()
        if num_str:  # Skip empty strings
            try:
                # Try to convert to float first, then keep as string for display
                float(num_str)  # Validate it's a number
                numbers.append(num_str)
            except ValueError:
                # Skip invalid numbers but could be collected for error reporting
                continue
    
    return numbers
