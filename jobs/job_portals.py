
"""Module for handling job portal integrations"""

class JobPortal:
    def __init__(self):
        self.portals = [
            {
                "name": "LinkedIn",
                "icon": "fab fa-linkedin",
                "color": "#0A66C2",
                "url": "https://www.linkedin.com/jobs/search/?keywords={}&location={}"
            },
            {
                "name": "Indeed IE",
                "icon": "fas fa-search",
                "color": "#003A9B",
                "url": "https://ie.indeed.com/jobs?q={}&l={}"
            },
            {
                "name": "Glassdoor IE",
                "icon": "fas fa-glass-whiskey",
                "color": "#0CAA41",
                "url": "https://www.glassdoor.ie/Job/jobs.htm?sc.keyword={}&locKeyword={}"
            }
        ]

    def search_jobs(self, job_title, location):
        if not location:
            location = "Dublin, Ireland"

        results = []

        for portal in self.portals:
            job = job_title.replace(" ", "+")
            loc = location.replace(" ", "+")

            url = portal["url"].format(job, loc)

            results.append({
                "portal": portal["name"],
                "icon": portal["icon"],
                "color": portal["color"],
                "title": f"{job_title} jobs in {location}",
                "url": url
            })

        return results
