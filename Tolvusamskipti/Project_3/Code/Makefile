# For compiling both client and server locally, open up a terminal within the folder the code is in, and write "make all". 

# To connect to Instructor server (or other student servers), the server code should be stored in Skel, and the client code on local computer. To compile, run the given command lines here below (server & client), server on Skel and client on local computer.


all:
	g++ --std=c++11 server.cpp -o tsampgroup32
	g++ -pthread --std=c++11 client.cpp -o client
	g++ -pthread --std=c++11 client.cpp -o server


tsampgroup32:
	g++ --std=c++11 server.cpp -o tsampgroup32


client: 
	g++ -pthread --std=c++11 client.cpp -o client


server:
	g++ -pthread --std=c++11 client.cpp -o server
	
