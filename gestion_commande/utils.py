from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.core.mail import EmailMessage

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None



def envoyer_facture_email(to_email, sujet, message, pdf_bytes, nom_pdf):
    email = EmailMessage(
        sujet,
        message,
        'no-reply@votresite.com',
        [to_email],
    )
    email.attach(nom_pdf, pdf_bytes, 'application/pdf')
    email.send()
