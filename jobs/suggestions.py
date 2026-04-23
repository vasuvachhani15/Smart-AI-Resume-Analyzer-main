"""Module containing job-related data and configurations"""

# Job titles and skills suggestions
JOB_SUGGESTIONS = [
    {"text": "Software Engineer", "icon": "💻"},
    {"text": "Full Stack Developer", "icon": "🔧"},
    {"text": "Data Scientist", "icon": "📊"},
    {"text": "Product Manager", "icon": "📱"},
    {"text": "DevOps Engineer", "icon": "⚙️"},
    {"text": "UI/UX Designer", "icon": "🎨"},
    {"text": "Python Developer", "icon": "🐍"},
    {"text": "Java Developer", "icon": "☕"},
    {"text": "React Developer", "icon": "⚛️"},
    {"text": "Machine Learning Engineer", "icon": "🤖"},
    {"text": "Backend Developer", "icon": "🖧"},
    {"text": "Frontend Developer", "icon": "🎨"},
    {"text": "Node.js Developer", "icon": "🌿"},
    {"text": "Angular Developer", "icon": "📐"},
    {"text": "PHP Developer", "icon": "🐘"},
    {"text": "Ruby Developer", "icon": "💎"},
    {"text": "Go Developer", "icon": "🚀"},
    {"text": "C++ Developer", "icon": "🖥️"},
    {"text": "C# Developer", "icon": "🎮"},
    {"text": "Django Developer", "icon": "🛠️"},
    {"text": "Data Analyst", "icon": "📈"},
    {"text": "Big Data Engineer", "icon": "📡"},
    {"text": "Database Administrator", "icon": "🗄️"},
    {"text": "Business Intelligence Analyst", "icon": "📊"},
    {"text": "Cloud Engineer", "icon": "☁️"},
    {"text": "AWS Engineer", "icon": "☁️🔧"},
    {"text": "Azure Engineer", "icon": "☁️🖥️"},
    {"text": "Google Cloud Engineer", "icon": "☁️📡"},
    {"text": "Network Engineer", "icon": "🔌"},
    {"text": "AI Researcher", "icon": "🧠"},
    {"text": "NLP Engineer", "icon": "🗣️"},
    {"text": "Computer Vision Engineer", "icon": "👁️"},
    {"text": "Deep Learning Engineer", "icon": "🧠📚"},
    {"text": "Cybersecurity Analyst", "icon": "🔒"},
    {"text": "Ethical Hacker", "icon": "🕵️‍♂️"},
    {"text": "Security Engineer", "icon": "🛡️"},
    {"text": "Penetration Tester", "icon": "🔍"},
    {"text": "Cryptography Engineer", "icon": "🔑"},
    {"text": "Game Developer", "icon": "🎮"},
    {"text": "Embedded Systems Engineer", "icon": "🖧⚙️"},
    {"text": "Mobile App Developer", "icon": "📱"},
    {"text": "iOS Developer", "icon": "🍏"},
    {"text": "Android Developer", "icon": "🤖"},
    {"text": "Blockchain Developer", "icon": "🔗"},
    {"text": "IoT Developer", "icon": "🌐"},
    {"text": "AR/VR Developer", "icon": "🕶️"},
    {"text": "Project Manager", "icon": "📋"},
    {"text": "Technical Writer", "icon": "✍️"},
    {"text": "QA Engineer", "icon": "✅"},
    {"text": "Scrum Master", "icon": "🔄"},
    {"text": "Support Engineer", "icon": "📞"},
    {"text": "IT Consultant", "icon": "🧑‍💼"},
    {"text": "Technical Support Specialist", "icon": "🎧"}
]

# Location suggestions - organized by European regions and major cities
LOCATION_SUGGESTIONS = [
    # Work modes
    {"text": "Remote", "icon": "🏠", "type": "work_mode"},
    {"text": "Work from Home", "icon": "🏠", "type": "work_mode"},
    {"text": "Hybrid", "icon": "🏢", "type": "work_mode"},
    
    # Major tech hubs (Top Level)
    {"text": "Dublin", "icon": "📍", "type": "city", "state": "Ireland"},
    {"text": "London", "icon": "📍", "type": "city", "state": "United Kingdom"},
    {"text": "Berlin", "icon": "📍", "type": "city", "state": "Germany"},
    {"text": "Amsterdam", "icon": "📍", "type": "city", "state": "Netherlands"},
    {"text": "Paris", "icon": "📍", "type": "city", "state": "France"},
    {"text": "Cork", "icon": "📍", "type": "city", "state": "Ireland"},
    
    # "States" (Using Countries/Regions for the European market)
    {"text": "Ireland", "icon": "🗺️", "type": "state"},
    {"text": "United Kingdom", "icon": "🗺️", "type": "state"},
    {"text": "Germany", "icon": "🗺️", "type": "state"},
    {"text": "Netherlands", "icon": "🗺️", "type": "state"},
    {"text": "France", "icon": "🗺️", "type": "state"},
    {"text": "Spain", "icon": "🗺️", "type": "state"},
    {"text": "Sweden", "icon": "🗺️", "type": "state"},
    {"text": "Switzerland", "icon": "🗺️", "type": "state"},
    
    # Ireland Cities
    {"text": "Galway", "icon": "📍", "type": "city", "state": "Ireland"},
    {"text": "Limerick", "icon": "📍", "type": "city", "state": "Ireland"},
    {"text": "Waterford", "icon": "📍", "type": "city", "state": "Ireland"},
    
    # UK Cities
    {"text": "Belfast", "icon": "📍", "type": "city", "state": "United Kingdom"},
    {"text": "Edinburgh", "icon": "📍", "type": "city", "state": "United Kingdom"},
    {"text": "Manchester", "icon": "📍", "type": "city", "state": "United Kingdom"},
    {"text": "Cambridge", "icon": "📍", "type": "city", "state": "United Kingdom"},
    {"text": "Bristol", "icon": "📍", "type": "city", "state": "United Kingdom"},
    
    # Germany Cities
    {"text": "Munich", "icon": "📍", "type": "city", "state": "Germany"},
    {"text": "Frankfurt", "icon": "📍", "type": "city", "state": "Germany"},
    {"text": "Hamburg", "icon": "📍", "type": "city", "state": "Germany"},
    
    # Netherlands Cities
    {"text": "Rotterdam", "icon": "📍", "type": "city", "state": "Netherlands"},
    {"text": "The Hague", "icon": "📍", "type": "city", "state": "Netherlands"},
    {"text": "Utrecht", "icon": "📍", "type": "city", "state": "Netherlands"},
    
    # France Cities
    {"text": "Lyon", "icon": "📍", "type": "city", "state": "France"},
    {"text": "Toulouse", "icon": "📍", "type": "city", "state": "France"},
    
    # Other Major EU Tech Hubs
    {"text": "Stockholm", "icon": "📍", "type": "city", "state": "Sweden"},
    {"text": "Zurich", "icon": "📍", "type": "city", "state": "Switzerland"},
    {"text": "Geneva", "icon": "📍", "type": "city", "state": "Switzerland"},
    {"text": "Barcelona", "icon": "📍", "type": "city", "state": "Spain"},
    {"text": "Madrid", "icon": "📍", "type": "city", "state": "Spain"}
]

# Function to get cities by state/country
def get_cities_by_state(state_name):
    """Get list of cities for a specific state/country"""
    return [loc for loc in LOCATION_SUGGESTIONS if loc.get("type") == "city" and loc.get("state") == state_name]

# Function to get all states/countries
def get_all_states():
    """Get list of all states/countries"""
    return [loc for loc in LOCATION_SUGGESTIONS if loc.get("type") == "state"]

# Job types
JOB_TYPES = [
    {"id": "all", "text": "All Types"},
    {"id": "full-time", "text": "Full Time"},
    {"id": "part-time", "text": "Part Time"},
    {"id": "contract", "text": "Contract"},
    {"id": "internship", "text": "Internship"},
    {"id": "remote", "text": "Remote"}
]

# Experience levels
EXPERIENCE_RANGES = [
    {"id": "all", "text": "All Levels"},
    {"id": "junior", "text": "Junior (0-2 years)"},
    {"id": "mid", "text": "Mid-Level (2-5 years)"},
    {"id": "senior", "text": "Senior (5-8 years)"},
    {"id": "lead", "text": "Lead (8-12 years)"},
    {"id": "principal", "text": "Principal/Director (12+ years)"}
]

# Salary ranges (Updated to Euros)
SALARY_RANGES = [
    {"id": "all", "text": "All Ranges"},
    {"id": "0-30k", "text": "Up to €30k"},
    {"id": "30k-50k", "text": "€30k - €50k"},
    {"id": "50k-80k", "text": "€50k - €80k"},
    {"id": "80k-120k", "text": "€80k - €120k"},
    {"id": "120k+", "text": "€120k+"}
]