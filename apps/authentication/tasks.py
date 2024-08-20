from celery import shared_task


@shared_task
def send_auth_code_task(phone_number, code):
    print(f"Auth code {code} sent to {phone_number}")