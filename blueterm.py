import bluetooth       #calling for header file which helps in using GPIOs of PI
 
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)
while 1:
 
 data = client_socket.recv(1024)
 print ("Received: %s" % data)
 send_data=data
 client_socket.send(send_data) 
 if (data == "q"):
  print ("Quit")
  break
 
client_socket.close()
server_socket.close()