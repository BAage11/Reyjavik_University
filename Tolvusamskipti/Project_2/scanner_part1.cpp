/* 
University of Reykjavik
Computer Networks (TSAM)
Project 2 - Part 1
Student: Benjamin Aage Birgisson (benjamin18@ru.is)
Group no.32
*/

#include <sys/types.h>          
#include <netinet/in.h>        
#include <sys/socket.h>       
#include <arpa/inet.h>         
#include <stdio.h>             
#include <stdlib.h>            
#include <string.h>            
#include <string>              
#include <unistd.h>            
#include <netdb.h>              
#include <iostream>  
#include <fstream>
using namespace std;


/* 
References:
https://stackoverflow.com/questions/15718299/what-will-be-the-result-of-atoiargv1
Slides from lecture 2 & 7 - Tölvusamskipti (TSAM)
Coding done by headteacher Jacky Mallett (16/09/20) - https://reykjavik.instructure.com/courses/3814/assignments/33482 
https://man7.org/linux/man-pages/man2/select.2.html 
https://stackoverflow.com/questions/4181784/how-to-set-socket-timeout-in-c-when-making-multiple-connections
Project 1, select() function in server.cpp - Tölvusamskipti (TSAM)
https://www.w3schools.com/cpp/cpp_files.asp 
*/


// Scan from-to (low-high) ports given, and print out open ports
int scanPorts(char *ip_addr, int low_port, int high_port) 
{
    // Initalizing variables
    int udp_sock;
    char buffer[1400];
    memset(buffer, 0, sizeof(buffer));
    socklen_t length;
    struct sockaddr_in server_addr;
    
    // Message to send to server
    strcpy(buffer, "Open?");
    int msg_len = strlen(buffer) + 1;

    // If not able to create a socket, send error message
    if((udp_sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) 
    {
        perror("Not able to create UDP socket.");
        return -1;
    }
    
    // Setup socket address structure
    server_addr.sin_family = AF_INET;
    inet_aton(ip_addr, &server_addr.sin_addr);
    length = sizeof(server_addr);
    
    // Iterate through ports given (from low, to high) until 4 open ports are found
    int count = 0;
    while(count != 4) {
        printf("\nTrying to find all (four) open ports...:\n");
        printf("-------------------------\n");

        // Create a textfile to store the open ports and messages given by open ports (for part 2)
        ofstream MyFile("ports.txt");

        count = 0;      // Initialize to 0 in beginning of for-loop (while-loop starting again)
        int portNoOutput = 1;           // For print output
        for(int nextPort = low_port; nextPort <= high_port; nextPort++) 
        {
            // Send message to server via the (next) given port number
            server_addr.sin_port = htons(nextPort); 
            if(sendto(udp_sock, buffer, msg_len, 0, (const struct sockaddr *)&server_addr, length) < 0) 
            {
                perror("Not able to send to server.");
            } 

            // If message was sent, try to receive message from server
            else 
            {
                // Buffer for receiving message from server
                char newBuffer[4000];
                memset(newBuffer, 0, sizeof(newBuffer));

                // Setup select() option for timeout (ignoring ports that don't respond in time)
                fd_set curr_socket;
                FD_SET(udp_sock, &curr_socket);
                struct timeval timeout;      
                timeout.tv_sec = 0;             // X second timeout
                timeout.tv_usec = 150000;       // Y millisecond timeout: timeout here after 0.15 sec
            
                // select() uses a timeout that is a struct timeval (with seconds and microseconds), 
                // checking to see if anything is being received
                if(select(udp_sock + 1, &curr_socket, NULL, NULL, &timeout) > 0) 
                {
                    int msg_recv = recvfrom(udp_sock, newBuffer, sizeof(newBuffer), 0, (sockaddr *)&server_addr, &length);

                    // Send error message if not able to collect message from server
                    if(msg_recv < 0) 
                    {
                        std::cout << "Could not get message from server." << std::endl;
                    } 
                    
                    // ... else, print out the current port in the iteration, and store port/message in textfile
                    else 
                    {
                        std::cout << "Port no." << portNoOutput << ": " << nextPort << std::endl;
                        portNoOutput++;

                        MyFile << nextPort << std::endl;
                        MyFile << newBuffer << std::endl;
                        count++;
                    }
                }
            } 
        } MyFile.close();       // Close textfile to be used in part 2 of project
    }

    printf("--------- Done! ---------\n\n");
    close(udp_sock); 
    return 0;
}


int main(int argc, char* argv[]) {
    // If command line does not include 4 arguments, send error message and exit.
    if(argc != 4) 
    {
        printf("Command to run program must be:\n /.scanner <IP address> <low port number> <high port number>");
        exit(0);
    }

    // Else, use input to scan ports, and print out the open ports numbers found in range given.
    char *ip_address = argv[1];
    int low_port = atoi(argv[2]);
    int high_port = atoi(argv[3]);

    scanPorts(ip_address, low_port, high_port);

}
