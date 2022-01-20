
						SYSTEM MANUAL
		--- Instructions on how to compile and run the programs (submitted code)  ---

Nota Bene:
	Operating System (OS) compiled on Linux (Ubuntu) environment.

Compile code - Locally:

	1. Open a terminal

	2. Go to the location of the code (client.cpp , server.cpp & Makefile etc.)

	3. Run the following command:
		make all			[press enter]

	4. Code should now have been compiled and can be run locally
	
	5. Now, you should have a server and a client operating, thus able to run
	   client commands. But to be able to process server commands as well, 
	   you must start another client (as a server) - step 6
	   
	6. Run the following command:
		g++ -pthread --std=c++11 client.cpp -o server		[press enter]
		
	7. Code for server and client are now ready to be run, as well as a client
	   operating as a server for server commands.
	
	

Compile code - Skel:
	1. Open a terminal within Skel
	
	2. Go to the location of server.cpp file
	
	3. Run the following command:
		g++ --std=c++11 server.cpp -o tsampgroup32		[press enter]
	
	4. Code for server has now been compiled and is ready to run
	
	5. Open another terminal, now locally
	
	6. Go to the location of client.cpp file
	
	7. Run the following command:
		g++ -pthread --std=c++11 client.cpp -o client		[press enter]
	
	8. Code for client has now been compiled and is ready to run
	
	9. Now, you should have a server and a client operating, thus able to run
	   client commands. But to be able to process server commands as well, 
	   you must start another client (as a server) - step 6
	   
	10. Run the following command (locally where client.cpp file is located):
		g++ -pthread --std=c++11 client.cpp -o server		[press enter]
		
	11. Code for server and client are now ready to be run, as well as a client
	   operating as a server for server commands.



Run submitted code:

	1. To start up the server, run the following command in server terminal:
		./tsampgroup32 <portno>	[press enter]
	
	    Where <portno> is a port between 4000 and 4100 (on Skel)
	
	2. Then, to start up the client run the following command in client terminal:
		./client <ipaddress> <portno>
		
	   Where <ipaddress> is the IP address where the server is running,
	   and <portno> is <port number> + 1. For example, the server port is
	   4032, then the client port should be set as 4033.
	 
	   When the client is up and running, the list of command that can be
	   given is printed out.
	   
	4. Now, to start up a server for server commands, run the following in another
	   seperate terminal (locally):
	   	./server <ipaddress> <portno>
	   	
	   Where <ipaddress> is the IP address where the server is running (step 1)
	   and <portno> is the same port number as the server is running on (step 1).
	 
	3. The following are the client commands that can be operated through
	   the client terminal (along with short explanations):
	   	GETMSG,GROUP_ID		[press enter]
	   		- Retrieve message stored on server side for the group_id given
	   	SENDMSG,GROUP_ID		[press enter]
	   		- A message is created and stored on server side for the group_id provided
	   	LISTSERVERS		[press enter]
	   		- Lists up all the servers that are connected to the running server
	   	CONNECT <clientName>		[press enter]
	   		- Connects the client, with given name of client, to the server running
	   	WHO		[press enter]
	   		- Lists up all the clients that are connected to the running server
	   	MSG <clientName> <msg content>		[press enter]
	   		- Sends the message content written to the client name given
	   	MSG ALL <msg content>		[press enter]
	   		- Messages all the connected clients the message content given
	   	LEAVE		[press enter]
	   		- Disconnect the client from the running server
	
	
	   The following are the server commands, which are given through the running client
	   terminal (along with short explanations):
	   	QUERYSERVERS,FROM_GROUP_ID		[press enter]
	   		- Provides a list of directly connected servers to the running server
	   	GET_MSG,GROUP_ID		[press enter]
	   		- Retrieves a message (singular) from the running server, 
	   		  if there are any stored for the given group_id
	   	SEND_MSG,TO_GROUP_ID,FROM_GROUP_ID,<msg content>		[press enter]
	   		- A message is stored on the running server for the given group_id, 
	   		  from given group_id, along with the message content provided
	   	STATUSREQ,FROM_GROUP_ID		[press enter]
	   		- Gives a comma seperated list of servers and number of messages
	   		  the running server has for them
	   	LEAVE,SERVER_IP,PORT		[press enter]
	   		- Disconnects the running server from the server with the given
	   		  IP address and port number.
	
	
	5. Other features:
		- A KeepAlive message is sent to connected servers with a two minute
		  time delay. If the message was not able to be sent, the running
		  server will disconnect to the server that it was trying to contact
		  with the KeepAlive message.
		- If the client terminal is closed, it will automatically disconnect
		  from the running server (or so it should).
		  The client can also be closed with CTRL+C command given on keyboard.



	-------------------------------NOTE---------------------------------------
		  For clarification on how to run program, after compiling,
	see the attached picture RunProgram.png (in folder ScreenshotAssignment)
	--------------------------------------------------------------------------

