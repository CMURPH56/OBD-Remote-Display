import time
import obd
print('hello')
connection = obd.OBD()
print('hello again')
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



while True:
    for k,v in pidSens.items():
        cmd = obd.commands.RPM
        response = connection.query(cmd)
        pidSens[k]=response

print(pidSens)
time.sleep(1)
