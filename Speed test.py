import time
import obd

connection = obd.OBD()

pidSens = {
            'COOLANT_TEMP':'',
            'FUEL_PRESSURE':'',
            'INTAKE_PRESSSURE':'',
            'RPM':'',
            'SPEED':'',
            'THROTTLE_POS':'',
            'RUN_TIME','FUEL_LEVEL'
            }

while True:
    for k,v in pidSens:
        cmd = obd.commands.k
        response = connection.query(cmd)
        pidSens[k]=response

print(pidSens)
time.sleep(1)
