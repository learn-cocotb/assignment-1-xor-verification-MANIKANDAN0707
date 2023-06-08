import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def dut_test(dut):
    #expected input a,b possibilities in a tuple(immutable)
    a=(0,0,1,1)
    b=(0,1,0,1)
    #expected output y possibilities
    y=(0,1,1,1)
    #Test verification y , iteration of a ,b
    for i in range(4):
    dut.a.value = a[i]
    dut.b.value = b[i]
    #wait for 1 nanosecond before proceeding to
    #allow the DUT to process the in and produce out
    await Timer(1,'ns')
    assert 0, "Test Not Implemented Error"
