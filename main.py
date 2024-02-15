import gspread
import flask
import pandas as pd
import os.path
from dotenv import load_dotenv

load_dotenv()

credentials = {
    "type": "service_account",
    "project_id": "directed-galaxy-413812",
    "private_key_id": os.getenv('PRIVATE_KEY_ID'),
    "private_key": os.getenv('PRIVATE_KEY'),
    "client_email": os.getenv('CLIENT_EMAIL'),
    "client_id": os.getenv('CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/googlesheetsofteng%40directed-galaxy"
                            "-413812.iam.gserviceaccount.com",

}
app = flask.Flask(__name__)
app.secret_key = "RpOmUT6h21PpAjfa9SIADDfA0GZsHgXc"

# Load credentials and authorize access to Google Sheets
google_credentials = gspread.service_account_from_dict(credentials)

# Open the spreadsheet by its URL
sheet = google_credentials.open_by_url(
    "https://docs.google.com/spreadsheets/d/1eguiRVklWH96TfYFGT88joReDg3enk956vb1Lsio9HE/edit#gid=0")

global sheet_values, student_status

# Select worksheet and store it in 'worksheet'
worksheet = sheet.worksheet('engenharia_de_software')


# Index page with a hyperlink to fetch the data from Google Sheets, creating an HTML table.
@app.route("/")
def index():
    index_options = ('<br<br><table>' +
                     '<tr><td><a href="/fetch_data">Fetch Data</a></td>' +
                     '<td>Fetch data from Google Sheets.</td></tr>'
                     )
    return index_options


@app.route('/fetch_data')
def fetch_data():
    global sheet_values
    sheet_values = sheet.sheet1.get_all_values()  # Select the spreadsheet and store its values in 'sheet_values'.
    df = pd.DataFrame(sheet_values).fillna('')  # Create a Pandas Dataframe with the values from the spreadsheet.
    html_table = df.to_html(header=False)  # Convert Dataframe to Html table

    #  Render Html table
    return (index() + '<tr><td><a href="/update_data">Update Data</a></td>' +
            '<td>Update the Spreadsheet data with the students approval status.</td></tr>' +
            '<tr><td><a href="/reset_data">Reset Data</a></td>' +
            '<td>Restore the Spreadsheet data to its original state.' +
            '</td></tr>' + html_table)


# Update the sheet with the students approval status
@app.route('/update_data')
def update_data():
    # We need to make sure 'sheet_values' is defined before trying to update the spreadsheet.
    try:
        sheet_values
    except NameError:
        return flask.redirect('/')

    # Check the students approval status according to their scores

    def check_approval_status():
        global student_status
        student_status = []  # Store the approval status of the student

        # Iterates over the values of 'sheet_values' in order to calculate
        # the exams average score and check whether the student is pass or fail.
        for student in sheet_values:
            if len(student[0]) <= 2:
                p1 = int(student[3])  # get P1 score
                p2 = int(student[4])  # get P2 score
                p3 = int(student[5])  # get P3 score
                absence_pct = int(student[2])  # get the number of absences
                average = (p1 + p2 + p3) / 30  # calculate the average score
                if absence_pct > 60 * 0.25:  # If the absence percentage is above 25% the student fails.
                    student_status.append(['Reprovado por Falta', 0])
                else:
                    if average >= 7:  # If the average score is equal or above 7, the student passes.
                        student_status.append(['Aprovado', 0])

                    elif average < 5:  # If bellow 5, the student fails.
                        student_status.append(['Reprovado por Nota', 0])
                    else:  # The student whose average score is above 5 and bellow 7 will take a final exam.
                        student_status.append(['Exame Final', f'{10 - average:.1f}'])

    # Send the approval status list to Google Sheets
    def update_approval_status():
        worksheet.update('G4', student_status)

    check_approval_status()
    update_approval_status()

    return flask.redirect('fetch_data')


# Restore the spreadsheet to its original state.
@app.route('/reset_data')
def reset_sheet():
    worksheet.batch_clear(['G4:H27'])
    return flask.redirect('fetch_data')
