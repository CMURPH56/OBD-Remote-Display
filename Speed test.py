import time
import obd

connection = obd.OBD()
while True:
    cmd = obd.commands.RPM
    #print (connection.query(cmd))
    revCount = connection.query(cmd)
    #recCount = revCount.replace("revolutions_per_minute","")
    revCountVal = str(revCount)
    print((revCountVal).replace(" revolutions_per_minute",""))
    time.sleep(1)
