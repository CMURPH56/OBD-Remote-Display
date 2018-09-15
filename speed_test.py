import time
import obd

'''
print('hello')
connection = obd.OBD()
print('hello again')

'''
pidSens = {
            'COOLANT_TEMP':'',
            'FUEL_PRESSURE':'',
            'INTAKE_PRESSSURE':'',
            'RPM':'',
            'SPEED':'',
            'THROTTLE_POS':'',
            'RUN_TIME':'',
            'FUEL_LEVEL':'',

            }


def get_rpm():
    return 'RPM'

while True:
    for k,v in pidSens.items():

        command = get_rpm()
        print(command)
        cmd = obd.commands.get_rpm()
        
        response = connection.query(cmd)
        pidSens[k]=response

print(pidSens)
time.sleep(1)
