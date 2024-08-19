from datetime import datetime, timedelta
import pytz
import re

dt = datetime

def add_hours_to_time(start_time, hours):
    """Add hours to a given datetime object."""
    return start_time + timedelta(hours=hours)

def parse_date(date_str):
    """Parse a date string with assumed current year and set time to 8:00 PM GMT."""
    current_year = datetime.now().year
    datetime_str = f"{date_str}/{current_year} 20:00"
    return datetime.strptime(datetime_str, "%m/%d/%Y %H:%M").replace(tzinfo=pytz.utc)

def format_date(date):
    """Format a datetime object to a string."""
    return date.strftime("%m/%d/%Y %H:%M")

def get_next_month_date():
    """Get the datetime object for the first day of the next month."""
    now = datetime.now()
    next_month = (now.month % 12) + 1
    return datetime(now.year, next_month, 1)

def add_days_to_date(date, days):
    """Add days to a given datetime object."""
    return date + timedelta(days=days)

def get_current_utc_time():
    """Get the current UTC time as a formatted string."""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def convert_timestamp_to_iso8601(timestamp):
    """Convert a Unix timestamp to an ISO 8601 formatted string."""
    return datetime.utcfromtimestamp(timestamp).isoformat()

def extract_timestamp_from_line(line):
    """Extract a Unix timestamp from a line of text."""
    match = re.search(r"\d{10}", line)
    if match:
        return int(match.group(0))
    raise ValueError("Timestamp not found in line")

def utc_from_timestamp(timestamp):
    """Convert a Unix timestamp to a timezone-aware UTC datetime object."""
    return datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)

def parse_date_str(date_str):
    """Parse a date string into a timezone-aware datetime object, handling multiple formats."""
    if date_str is None:
        raise ValueError("Date string is None")

    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.replace(tzinfo=pytz.utc)
    except ValueError:
        pass

    try:
        dt = datetime.strptime(date_str, '%d %B %Y %H:%M')
        return dt.replace(tzinfo=pytz.utc)
    except ValueError:
        pass

    raise ValueError(f"Date format is incorrect: {date_str}")


def iso_format(dt):
    """Return ISO 8601 format of a datetime object."""
    return dt.isoformat()


def parse_duration_from_title(title):
    """Extracts duration in days from the event title."""
    match = re.search(r'\((\d+) days?\)', title)
    if match:
        return int(match.group(1))
    return 0

def calculate_end_time(start_time, duration_days):
    """Calculates the end time of an event based on the start time and duration."""
    return start_time + timedelta(days=duration_days)
