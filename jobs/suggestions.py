"""Module containing job-related data and configurations"""

# Job suggestions
JOB_SUGGESTIONS = [
    {"text": "Software Engineer", "icon": "💻"},
    {"text": "Full Stack Developer", "icon": "🔧"},
    {"text": "Data Scientist", "icon": "📊"},
    {"text": "Product Manager", "icon": "📱"},
    {"text": "DevOps Engineer", "icon": "⚙️"},
    {"text": "UI/UX Designer", "icon": "🎨"},
    {"text": "Python Developer", "icon": "🐍"},
]

# European Locations
LOCATION_SUGGESTIONS = [
    {"text": "Remote", "icon": "🏠", "type": "work_mode"},
    {"text": "Hybrid", "icon": "🏢", "type": "work_mode"},

    {"text": "Dublin", "icon": "📍", "type": "city", "state": "Ireland"},
    {"text": "Cork", "icon": "📍", "type": "city", "state": "Ireland"},
    {"text": "Galway", "icon": "📍", "type": "city", "state": "Ireland"},

    {"text": "London", "icon": "📍", "type": "city", "state": "UK"},
    {"text": "Berlin", "icon": "📍", "type": "city", "state": "Germany"},
    {"text": "Amsterdam", "icon": "📍", "type": "city", "state": "Netherlands"},

    {"text": "Ireland", "icon": "🗺️", "type": "state"},
    {"text": "UK", "icon": "🗺️", "type": "state"},
    {"text": "Germany", "icon": "🗺️", "type": "state"},
]

# Salary in Euros
SALARY_RANGES = [
    {"id": "all", "text": "All Ranges"},
    {"id": "0-30k", "text": "Up to €30k"},
    {"id": "30k-50k", "text": "€30k - €50k"},
    {"id": "50k-80k", "text": "€50k - €80k"},
    {"id": "80k-120k", "text": "€80k - €120k"},
    {"id": "120k+", "text": "€120k+"}
]

JOB_TYPES = [
    {"id": "all", "text": "All Types"},
    {"id": "full-time", "text": "Full Time"},
    {"id": "contract", "text": "Contract"},
]

EXPERIENCE_RANGES = [
    {"id": "all", "text": "All Levels"},
    {"id": "junior", "text": "Junior"},
    {"id": "mid", "text": "Mid-Level"},
    {"id": "senior", "text": "Senior"},
]

def get_cities_by_state(state_name):
    return [loc for loc in LOCATION_SUGGESTIONS if loc.get("state") == state_name]

