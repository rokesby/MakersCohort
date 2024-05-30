from datetime import datetime

def age_checker(dob):

    # Validate a correct date.
    try:
        validated_dob = datetime.strptime(dob, "%Y-%m-%d").date()

    except ValueError:
        # This is a bad date
        return "The date of birth is not in the right format"

    # Grab the current date
    current_date = (datetime.now()).date() 

    # Compare and calculate age
    calculated_age = (current_date - validated_dob).days
    calculated_age_year = int((calculated_age / 365))

    # Compare against 16 year threshold
    if calculated_age_year < 16:
        return f"Access denied, you are {calculated_age_year} and you need to be 16"
    else:
        return "Access granted!"
    