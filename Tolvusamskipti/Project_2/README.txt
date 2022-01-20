
						SYSTEM MANUAL
		--- Instructions on how to compile and run the programs (submitted code)  ---


Compile code:

	1. Open up a terminal window

	2. Go to the location of the code (scanner_part1.cpp, scanner_part2.cpp , scanner_part3.cpp & Makefile)

	3. Run the following command:
		make all			[press enter]

	4. Code should now be compiled and ready to use.



Run submitted code:

	1. Open a terminal window

	2. Go to the location of the code in your local computer

	3. To run the first part of the program (scanner1), run the following command line in terminal:

		./scanner1 130.208.243.61 4000 4100			[press enter]

	4. The program runs a port scanner process, where the ports that are open are displayed on the terminal.
	   The total number of open ports should always be four, so the program continues until all four ports have been found.

	5. Now that the open ports have been found, the second part of the program (scanner2) can be run for solving the puzzle ports.
	   Run the following command line in terminal:

		sudo ./scanner2			[press enter]

	As shown, the command is done with sudo-privilege (root permission). 
	That is, to be able to run the command as 'any user', with the default generally being the root.

	5. The process of communication between program and the open ports are displayed, 
	   showing the hidden ports found and the 'secret phrase', as well as the sequence of knocks for part 3.

	6. Afterwards, the final part of the program (scanner3) can be run.
	   Run the following command line in terminal:

		./scanner3			[press enter]

	7. The sequence of knocks and what ports are being contacted are displayed,
	   as well as the final message by the last port given in the sequence.


     -------------------------------------------------------------------------------------------------
	Nota Bene: 
		Was not able to retrieve the 'secret phrase' in part 2 of the program (scanner2), 
	    	due to NAT connection from home address (VPN not working).
     -------------------------------------------------------------------------------------------------

