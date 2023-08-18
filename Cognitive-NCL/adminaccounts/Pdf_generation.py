import os
from django.conf import settings
from fpdf import FPDF

# # Margin
# m = 10
# # Page width: Width of A4 is 210mm
# pw = 210 - 2*m
# # Cell height
# ch = 50
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', '', 12)
# pdf.cell(w=0, h=20, txt="Header", border=1, ln=1)
# pdf.cell(w=0, h=ch, txt="User Info", border=1, ln=1)
# pdf.ln(30)
# pdf.cell(w=(0.2*pw), h=120, txt="", border=0, ln=0)
# pdf.cell(w=(0.6*pw), h=120, txt="Competency Matrix", border=1, ln=0, align ='C')
# pdf.cell(w=(0.2*pw), h=120, txt="", border=0, ln=1)
# pdf.ln(38)
# pdf.cell(w=0, h=8, txt="Footer", border=1, ln=0)

# pdf.output(f'./example.pdf', 'F')
# matrix, User[0], qualification, str(res_id[0]), year_of_birth, designation, date_created, organization, email)


def report(matrix, user, qual, ID, yob, date, email):

    pdf = FPDF()
    pdf.add_page()

    pdf.image('Header.png',
              x=5, y=None, w=200, h=0, type='PNG')
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=10, txt="Corporate Cognitive Assessment", ln=1, align='C')
    pdf.ln(5)
    pdf.set_font('Arial', '', 12)
    # pdf.cell(w=0, h=20, txt="Header", ln=1, align='C')
    pdf.cell(w=0, h=10, txt="Name: " + user, ln=0, align='L')
    pdf.cell(w=0, h=10, txt="Qualification: " + qual[0], ln=1, align='R')
    pdf.cell(w=0, h=10, txt="Reg ID: " + ID, ln=0, align='L')
    # print("_________________", yob)
    pdf.cell(w=0, h=10, txt="Year of Birth: " + str(yob[0]), ln=1, align='R')
    # pdf.cell(w=0, h=10, txt="Occupation: " + designation, ln=0, align='L')
    pdf.cell(w=0, h=10, txt="Contact: " + str(email[0]), ln=0, align='L')

    pdf.cell(w=0, h=10, txt="Test Date: " +
             str(date[0])[:11], ln=1, align='R')

    # pdf.cell(w=0, h=10, txt="Organization: " + org, ln=0, align='L')
    # pdf.cell(w=0, h=10, txt="Contact: " + email, ln=1, align='R')
    pdf.cell(w=0, h=10, txt=" ", ln=1, align='L')
    pdf.ln(7)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=10, txt="Competency Matrix:", ln=1, align='L')
    pdf.ln(5)
    matrix = "Matrices/" + matrix + ".png"
    pdf.image(matrix,
              x=30, y=None, w=150, h=150, type='PNG')

    pdf.ln(10)
    # pdf.cell(w=0, h=10, txt="Footer", ln=1, align='C')
    pdf.image('Footer.png',
              x=5, y=None, w=200, h=0, type='PNG')

    pdf.image('Header.png',
              x=0, y=None, w=200, h=0, type='PNG')

    pdf.ln(5)
    pdf.image('mental_health.png',
              x=0, y=None, w=210, h=35, type='PNG')

    pdf.ln(10)
    pdf.image('mem.png',
              x=50, y=None, w=100, h=60, type='PNG')

    pdf.ln(5)
    pdf.image('visual.png',
              x=50, y=None, w=100, h=60, type='PNG')

    pdf.ln(5)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=10, txt="Observations: ", ln=1, align='L')

    pdf.ln(48)
    # pdf.cell(w=0, h=10, txt="Footer", ln=1, align='C')
    pdf.image('Footer.png',
              x=5, y=None, w=200, h=0, type='PNG')

    name = user
    user_id = ID
    # 'report' folder in the Django project root
    directory = os.path.join(settings.BASE_DIR, 'report')
    # Create the 'report' folder if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    prompt = os.path.join(directory, name + ".pdf")
    pdf.output(dest='F', name=prompt)
    os.remove(os.path.join(settings.BASE_DIR, 'visual.png'))
    os.remove(os.path.join(settings.BASE_DIR, 'mental_health.png'))
    os.remove(os.path.join(settings.BASE_DIR, 'mem.png'))
    os.remove(os.path.join(settings.BASE_DIR, 'anx.png'))
    os.remove(os.path.join(settings.BASE_DIR, 'ls.png'))
    os.remove(os.path.join(settings.BASE_DIR, 'dep.png'))
    os.remove(os.path.join(settings.BASE_DIR, 'ws.png'))
    return prompt
