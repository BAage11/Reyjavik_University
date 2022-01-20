
						SYSTEM MANUAL
		--- Instructions on how to compile and run the programs (submitted code)  ---


Compile code:

	1. Open a terminal

	2. Go to the location of the code (client.cpp , server.cpp & Makefile etc.)

	3. Run the following command:
		make all			[press enter]

	4. Code should now have been compiled (error message still given here, not working fully...)



Run submitted code:

	1. Open three terminal windows

	2. Go to the location of the code in each of the terminals (server on Skel, and client/tcpdump on your local computer)

	3. On terminal 1, run the following command lines for the server:
		g++ -Wall -std=c++11 server_modified.cpp -o server_mod		[press enter]
		./server_mod 4052						[press enter]

	4. The following message should be presented on terminal 1 (server):
		"Listening on port: 4052"
			"(range of available ports on skel.ru.is is 4000-4100"

	5. On terminal 2, run the following command line for tcpdump:
		sudo tcpdump -X -i wlp4s0 host 130.208.243.61 and port 4052	[press enter]

	   NOTICE: Here, the interface used is 'wlp4s0' but this can differ between computer networks.
	           Therefore, to find your networks use the following command to see connections: 
				tcpdump -D					[press enter]

	6. Display of TCP/IP and other packets being transmitted or received over the network should be running now on terminal 2 (tcpdump).

	7. On terminal 3, run the following command line for the client:
		g++ -Wall -std=c++11 client_modified.cpp -o client_mod		[line 1, press enter]
		./client_mod 130.208.243.61 4052				[line 2, press enter]

	8. The following message should be presented on terminal 3 (client):
		"To quit, press 'Q' on keyboard."
		"> "

	9. The following message should be presented on terminal 1 (server) as well: 
		"Client connected on server"

	10. On terminal 3 (client), the user can now type in (only) SYS-commands and receive message from the server. 
	    For example:
		SYS ls			[press enter]
		SYS w			[press enter]
		SYS who			[press enter]

	11. On terminal 2 (tcpdump), all packets transmitted or received between server and client are displayed.

	12. On terminal 1 (server), the commands given are printed out, as well as the output of the command are sent over to
	    the client side (user interface).

	13. If a command is given on client side which is not supported by the server, an error message is displayed.

	14. To quit communication, in terminal 3 (client) the user shall enter "q" or "Q" and press enter.

	15. The same steps can be done as described here above with client and server that have not 
	    been modified (client.cpp & server.cpp), where the user/client can only enter one (single) command 
	    and will not be given back any message.
