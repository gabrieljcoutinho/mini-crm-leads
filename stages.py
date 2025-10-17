from datetime import date

STAGES = ["novo"]

def model_lead(name, company, email):
    today = date.today().strftime("%d/%m/%Y")
    return {
        "name": name,
        "company": company,
        "email": email,
        "stage": "novo",
        "created": today
    }
