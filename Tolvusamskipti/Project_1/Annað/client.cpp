/* 
University of Reykjavik
Computer Networks (TSAM)
Project 1 - Part 2
Student: Benjamin Aage Birgisson
*/

#include  <sys/types.h>         // http://manpages.ubuntu.com/manpages/trusty/man7/sys_types.h.7posix.html 
#include  <netinet/in.h>        // AF_INET and AF_INET6 address families and their corresponding protocol families, PF_INET and PF_INET6. These include standard IP addresses and TCP and UDP port numbers.
#include  <sys/socket.h>        // Core socket functions and data structures.

#include <arpa/inet.h>          // Functions for manipulating numeric IP addresses.
#include <stdio.h>              // Standard library function for file input and output.
#include <stdlib.h>             // Standard library for the C programming language.
#include <string.h>             // The C programming language has a set of functions implementing operations on strings in its standard library.
#include <string>               // Declare string objects/variables.
#include <unistd.h>             // Header file that provides access to the POSIX operating system API.
#include <netdb.h>              // Functions for translating protocol names and host names into numeric addresses. Searches local data as well as name services. 
#include <iostream>             // Header that defines the standard input/output stream objects.

/* 
References:
Slides from lecture 2 - Tölvusamskipti (TSAM)
Linux Programmer's Manual
https://en.wikipedia.org/wiki/Berkeley_sockets#socket 
https://gist.github.com/codehoose/d7dea7010d041d52fb0f59cbe3826036#file-bbclient-cpp-L42
*/

using namespace std;

int main() {
    string ipAddress = "130.208.243.61";               // ip address for Skel
    int portNo = 4055;                                  // port chosen between 4000-4100 as given

    // Setup a socket
    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);          // socket(domain, type, protocol)
    
    // Check if a socket has been created, else send error message
    if (sock_fd < 0) {
        perror("Not able to open socket...");
        return -1;
    }

    // Setup socket address structure for connection
    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portNo);

    // Creating structure
    inet_pton(AF_INET, ipAddress.c_str(), &serv_addr.sin_addr);

    // Establish connection to the server
    int connection = connect(sock_fd, (sockaddr*)&serv_addr, sizeof(serv_addr));
    if(connection < 0 ) {
        perror("Could not connect to server...");
        return -1;
    }


    // Create while-loop for commands from client to server
    char buffer[1024];                      // Initialize buffer (block of memory)
    string userCommand;                     // Initialize user input as string
    
    // Send message to user on how to stop loop
    cout << "To quit, press 'q' on keyboard." << endl;              // cout: Standard output stream (object)

    do {
        // Get (next) command from user
        cout << "> ";
        getline(cin, userCommand);              // cin: Standard input stream (object)
        
        // If user enters "q" or "Q", break from the while-loop
        if (userCommand == "q" || userCommand == "Q") {
            break;
        } 
        else {    
            // Else, send command to server
            int sendMessage = send(sock_fd, userCommand.c_str(), userCommand.size() + 1, 0);
        
            // If command given that the server cannot process, send error message
            if (sendMessage < 0) {
                cout << "Could not process command. Please try again.\r\n";
                continue; 
            } 
            else {
                // Else, wait for response from server and output message from server
                memset(buffer, 0, 1024);
                int messageRec = recv(sock_fd, buffer, 1024, 0);

                if (messageRec < 0) {
                    cout << "An error occured and message could not be processed from server.";
                } 
                else {
                    cout << "Output: " << string(buffer, messageRec) << endl;
                }
            }
        }        

    } while(true);              // Loop through the process, until user quits ("Q" or "q" entered)

    close(sock_fd);             // Close the socket
    
    return 0;
}



/*
TCP client:
        socket()
        connect()
        write()             --> send
        read()              --> recv
        close()
*/