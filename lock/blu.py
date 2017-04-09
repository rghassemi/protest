import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.settimeout(0.33)
sock.bind(("", bluetooth.PORT_ANY))
sock.listen(10)
bluetooth.advertise_service(sock, 'foo',
                            service_id='1234',
                            service_classes=['1234', bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])

