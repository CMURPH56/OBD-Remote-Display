import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import time
#https://rakibul.net/fb-realtime-db-python/

# Fetch the service account key JSON file contents
cred = credentials.Certificate('obdII.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://obdiidata.firebaseio.com/'
})

#function to scale values with count
def translate(value, leftMin, leftMax, rightMin, rightMax,):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

ref = db.reference('/')
count = 1
runTime = 0
dataStart = ('ECU_Data: ' + str(datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S")))



while True:

    runTime = runTime + 1
    count = count+1
    if count == 250:
        count = 1

    ref.set({
            ('object'):
                {
                    ('rpm'): int(translate(count,0,250,0,55)),
                    ('speed'): int(translate(count,0,250,0,99)),
                    ('manidPres'): int(translate(count,0,250,-14,14)),
                    ('oilTemp'): int(translate(count,0,250,30,210)),}
                })
    time.sleep(.1)
    count = count+1
