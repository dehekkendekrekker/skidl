from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

Zilog = SchLib(tool=SKIDL).add_parts(*[
        Part(name='Z80CPU',dest=TEMPLATE,tool=SKIDL,keywords='Z80 CPU uP',description='8-bit General Purpose Microprocessor, DIP-40',ref_prefix='U',num_units=1,fplist=['DIP*', 'PDIP*'],do_erc=True,pins=[
            Pin(num='1',name='A11',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='A12',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='A13',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='A14',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='A15',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='~CLK~',do_erc=True),
            Pin(num='7',name='D4',func=Pin.BIDIR,do_erc=True),
            Pin(num='8',name='D3',func=Pin.BIDIR,do_erc=True),
            Pin(num='9',name='D5',func=Pin.BIDIR,do_erc=True),
            Pin(num='10',name='D6',func=Pin.BIDIR,do_erc=True),
            Pin(num='20',name='~IORQ~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='30',name='A0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='40',name='A10',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='21',name='~RD~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='31',name='A1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='D2',func=Pin.BIDIR,do_erc=True),
            Pin(num='22',name='~WR~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='32',name='A2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='13',name='D7',func=Pin.BIDIR,do_erc=True),
            Pin(num='23',name='~BUSACK~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='33',name='A3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='D0',func=Pin.BIDIR,do_erc=True),
            Pin(num='24',name='~WAIT~',do_erc=True),
            Pin(num='34',name='A4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='D1',func=Pin.BIDIR,do_erc=True),
            Pin(num='25',name='~BUSRQ~',do_erc=True),
            Pin(num='35',name='A5',func=Pin.OUTPUT,do_erc=True),
            Pin(num='16',name='~INT~',do_erc=True),
            Pin(num='26',name='~RESET~',do_erc=True),
            Pin(num='36',name='A6',func=Pin.OUTPUT,do_erc=True),
            Pin(num='17',name='~NMI~',do_erc=True),
            Pin(num='27',name='~M1~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='37',name='A7',func=Pin.OUTPUT,do_erc=True),
            Pin(num='18',name='~HALT~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='28',name='~RFSH~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='38',name='A8',func=Pin.OUTPUT,do_erc=True),
            Pin(num='19',name='~MREQ~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='29',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='39',name='A9',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='Z8530',dest=TEMPLATE,tool=SKIDL,keywords='SCC Serial Communication',description='SCC Serial Communication Controller, DIP-40',ref_prefix='U',num_units=1,fplist=['DIP*', 'PDIP*'],do_erc=True,pins=[
            Pin(num='1',name='D1',do_erc=True),
            Pin(num='2',name='D3',do_erc=True),
            Pin(num='3',name='D5',do_erc=True),
            Pin(num='4',name='D7',do_erc=True),
            Pin(num='5',name='~INT',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='6',name='IEO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='IEI',do_erc=True),
            Pin(num='8',name='~INTACK',do_erc=True),
            Pin(num='9',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='10',name='~W/REQA~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='20',name='PCLK',do_erc=True),
            Pin(num='30',name='~W/REQB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='40',name='D0',do_erc=True),
            Pin(num='11',name='~SYNCA~',func=Pin.BIDIR,do_erc=True),
            Pin(num='21',name='~DCDB',do_erc=True),
            Pin(num='31',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='12',name='~RTXCA',do_erc=True),
            Pin(num='22',name='~CTSB',do_erc=True),
            Pin(num='32',name='D/~C~',do_erc=True),
            Pin(num='13',name='RXDA',do_erc=True),
            Pin(num='23',name='~RTSB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='33',name='~CE',do_erc=True),
            Pin(num='14',name='~TRXCA',func=Pin.BIDIR,do_erc=True),
            Pin(num='24',name='~DTR/REQB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='34',name='A/~B~',do_erc=True),
            Pin(num='15',name='TXDA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='25',name='TXDB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='35',name='~WR',do_erc=True),
            Pin(num='16',name='~DTR/REQA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='26',name='~TRXCB',func=Pin.BIDIR,do_erc=True),
            Pin(num='36',name='~RD',do_erc=True),
            Pin(num='17',name='~RTSA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='27',name='RXDB',do_erc=True),
            Pin(num='37',name='D6',do_erc=True),
            Pin(num='18',name='~CTSA',do_erc=True),
            Pin(num='28',name='~RTXCB',do_erc=True),
            Pin(num='38',name='D4',do_erc=True),
            Pin(num='19',name='~DCDA',do_erc=True),
            Pin(num='29',name='~SYNCB',func=Pin.BIDIR,do_erc=True),
            Pin(num='39',name='D2',do_erc=True)])])