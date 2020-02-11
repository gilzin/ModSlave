from pymodbus.server.async import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [0]*100),
    co = ModbusSequentialDataBlock(0, [0]*100),
    hr = ModbusSequentialDataBlock(0, [0]*100),
    ir = ModbusSequentialDataBlock(0, [0]*100))
context = ModbusServerContext(slaves=store, single=True)

def read_context(a):
     context  = a[0]
     register = 3
     slave_id = 0
     address  = 10
     value = context[slave_id].getValues(register,address,10)
#     print value[0]
#     print value[1]


StartTcpServer(context)
