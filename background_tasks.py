from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email_notification(email: str):
    print(f"Sending email notification to {email}")


@app.post("/send-email")
async def send_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_notification, email)
    return {"message": "Email notification is being sent in the background."}

