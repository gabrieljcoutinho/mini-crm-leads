from datetime import date

STAGES = ["novo"]

def model_lead(name, company, email):
    return{
        "name": name,
        "company": company,
        "email": email,
        "stage": "novo",
        "created": date.today().isoformat()
    }