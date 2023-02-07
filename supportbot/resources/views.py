from fastapi import APIRouter
from .models import Placeholder
from .send_mail.send_mail import EmailSender
from .send_mail.template import TemplateReader
from .apis.youtube import youtube
from .apis.google_drive import google_drive



router = APIRouter(
    prefix="/supportbot",
    tags=["supportbot"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def srscore(placeholder:Placeholder):
    """calculate social reputations score"""
    print(placeholder)
    intent = placeholder.intent.intent
    nft_type = placeholder.intent.nft_type
    r_email = placeholder.intent.email
    
    # process email automation with user information
    if intent == "balance":
        email = EmailSender()
        template = TemplateReader()
        email_message = template.read_course_template(nft_type)
        email.send_email_to_user(r_email, email_message)
        
    elif intent == "youtube":
        youtube()
    elif intent == "google_drive":
        google_drive()
    return {"message": "HEllO FASTAPI"}



