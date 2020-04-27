import tkinter as tk
import bluetooth 

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)


window = tk.Tk()

client_socket.send('010D') 
mph = client_socket.recv(1024)
client_socket.send('010C') 
rpm = client_socket.recv(1024)


Speed = tk.Label(text="Speed is %s mph" %mph)
Speed.pack()
RPM = tk.Label(text="Speed is %s rpm" %rpm)
RPM.pack()
window.mainloop()