from email import encoders
import email
from email.mime.base import MIMEBase
import pickle
import os
import base64
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.message import EmailMessage
import mimetypes
import imghdr

#Previous Infrastructure
suites = ['1', '2', '12A', '21', '22']

dates = {31:'Tuesday, June 14th', 32:'Wednesday, June 15th', 33:'Thursday, June 16th', 34:'Friday, June 17th', 35:'Saturday, June 18th', 36:'Sunday, June 19th', 37:'Tuesday, June 21st', 38:'Wednesday, June 22nd', 39:'Thursday, June 23rd', 40:'Friday, June 24th', 41:'Saturday, June 25th', 42:'Sunday, June 26th',
43:'Monday, July 4th', 44:'Wednesday, July 6th', 45:'Thursday, July 7th', 46:'Friday, July 8th', 47:'Saturday, July 9th', 48:'Sunday, July 10th',
49:'Friday, July 22nd', 50:'Sautrday, July 23rd', 51:'Sunday, July 24th',
52:'Tuesday, August 2nd', 53:'Wednesday, August 3rd', 54:'Thursday, August 4th', 55:'Friday, August 5th', 56:'Saturday, August 6th', 57:'Sunday, August 7th',
58:'Tuesday, August 16th', 59:'Wednesday, August 17th', 60:'Thursday, August 18th', 61:'Friday, August 19th', 62:'Saturday, August 20th', 63:'Sunday, August 21st'}

suiteOccupants = {
    '1':['Henry Whittier','Choi'],
    '2':['Walt Giard','Dalton'],
    '12A':['Phoenix Marketing','Ryan'],
    '21':['Jennifer Clarke','Ryan'],
    '22':['','Corp']
}

suiteParking = {'1':['49', '50'], '2': ['51', '52'], '12A': ['53', '54'], '21': ['55', '56'], '22': ['57', '58']}

email_dir = {'Corp': 'sturner@woosox.com', 'Tom':'tsteiger@woosox.com', 'Dalton':'dbodreau@woosox.com', 'Caroline':'cmeizen@woosox.com', 'Ryan':'rNesbit@woosox.com', 
'Choi':'jchoi@woosox.com', 'Joe':'jfoley@woosox.com', 'Jim':'jcain@woosox.com', 'Brian':'bkallajian@woosox.com', 'Sarah':'smalone@woosox.com', 
'Diggins':'ddiggins@woosox.com', 'Mia':'mmcauliffe@woosox.com', 'Max':'mferrucci@woosox.com'}

# Get the path to the pickle file
home_dir = os.path.expanduser('~')
pickle_path = os.path.join(home_dir, 'gmail.pickle')

# Load our pickled credentials
creds = pickle.load(open(pickle_path, 'rb'))

# Build the service
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

def WalkingDog(game):
    for current_suite in suites:
        # Create a message
        rec_email = email_dir[suiteOccupants[current_suite][1]]
        my_email = 'woosoxsuiteinfo@gmail.com'
        msg = MIMEMultipart('mixed')
        msg['Subject'] = f"{dates[game]} - {suiteOccupants[current_suite][0]} - Suite {current_suite}"
        msg['From'] = my_email
        msg['To'] = rec_email

        #Message Body
        msgPlain = f"Hello,\n\nWe are looking forward to welcoming you to Polar Park on {dates[game]}. Enter the ballpark on Madison Street, Gate D and head upstairs to the DCU Club level. Attached to this email are two VIP Passes that you can utilize to park in the purple lot (right next to the Green Island Boulevard Garage) for this date. With Suite {current_suite}, you are welcome to park in Spots {suiteParking[current_suite][0]} and {suiteParking[current_suite][1]}. You will see additional parking details in the “Know Before You Go” Suite Edition.\n\nGo WooSox,\n\nSam Turner"

        msg.attach(MIMEText(msgPlain, 'plain'))

        #Attatch Know Before You Go Sheet
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("Suite-Know-Before-You-Go.pdf", "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="Suite-Know-Before-You-Go.pdf"')
        msg.attach(part)

        #Attach Parking Pass 1

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(os.path.join(home_dir, f"Nightly-Suite-Parking-Passes/Spot {suiteParking[current_suite][0]}/Nightly Suite - Spot {suiteParking[current_suite][0]} {game}.pdf"), "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="Nightly Suite - Spot {suiteParking[current_suite][0]} {game}.pdf"')
        msg.attach(part)

        #Attach Parking Pass 2

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(os.path.join(home_dir, f"Nightly-Suite-Parking-Passes/Spot {suiteParking[current_suite][1]}/Nightly Suite - Spot {suiteParking[current_suite][1]} {game}.pdf"), "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="Nightly Suite - Spot {suiteParking[current_suite][1]} {game}.pdf"')
        msg.attach(part)

        raw = base64.urlsafe_b64encode(msg.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}

        message1 = body
        message = (
            service.users().messages().send(
                userId="me", body=message1).execute())
        print('Message Id: %s' % message['id'])

WalkingDog(42)