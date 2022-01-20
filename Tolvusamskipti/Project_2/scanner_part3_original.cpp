/* 
University of Reykjavik
Computer Networks (TSAM)
Project 2 - Part 3
Student: Benjamin Aage Birgisson (benjamin18@ru.is)
Group no.32
*/

#include <arpa/inet.h>         
#include <unistd.h>            
#include <string.h> 
#include <string> 
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

/*
Reference:
https://stackoverflow.com/questions/755835/how-to-add-element-to-c-array
*/

std::string oracle_content;
std::vector<int> ports;


int KnockOnPorts() 
{
    printf("-------------------------\n");

    // Loop through the first four ports, and send a 'knock' message
    int count = 1;      // for print output
    for(int index = 0; index < 4; index++) 
    {
        std::cout << "Sending 'knock' message no." << count << " to port number " << ports[index] << "...";
        count++;

        // Initalizing variables to send to knock port
        int knock_sock;
        char buffer[100];
        memset(buffer, 0, sizeof(buffer)); 
        socklen_t length;
        struct sockaddr_in server_addr;
    
        // Message to send to server
        strcpy(buffer, "knock");                // Used to be: "Each knock must contain the message ”knock”, except for the last knock, which should contain the secret phrase from part 2."
        int msg_len = strlen(buffer) + 1;

        // If not able to create a socket, send error message
        if((knock_sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) 
        {
            perror("Not able to create UDP socket (knock port).");
            return -1;
        }
    
        // Setup socket address structure
        server_addr.sin_family = AF_INET;
        inet_aton("130.208.243.61", &server_addr.sin_addr);
        length = sizeof(server_addr);
        server_addr.sin_port = htons(ports[index]); 

        // Make a connection to socket
        connect(knock_sock, (sockaddr*)&server_addr, length);
        
        // Send message to socket with 'knock' message
        if(sendto(knock_sock, buffer, msg_len, 0, (const struct sockaddr *)&server_addr, length) < 0) 
        {
            perror("Not able to send to server (knock port).");
            return -1;
        } 
        close(knock_sock);
        std::cout << "done!" << std::endl;
    }
    
    // Send to the last port in array the 'secret phrase' message from Part 2
    int last_port = ports[4];
    std::cout << "\nSending 'secret phrase' message to port number " << last_port << "...";

    // Initalizing variables to send to 'secret phrase' port
    int last_sock;
    char buffer[1000];
    memset(buffer, 0, sizeof(buffer)); 
    socklen_t length;
    struct sockaddr_in server_addr;
    
    // Variables for reading the 'secret phrase' textfile into a string
    std::ifstream MyFile("secretphrase.txt");
    std::string str_out;
    std::string secret_content;

    // Getting the content of the file and output to the text string
    while (std::getline(MyFile, str_out))
    {
        secret_content += str_out;
    }

    // Message to send to server
    strcpy(buffer, secret_content.c_str());
    int msg_len = strlen(buffer) + 1;

    // If not able to create a socket, send error message
    if((last_sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) 
    {
        perror("Not able to create UDP socket (last port).");
        return -1;
    }
    
    // Setup socket address structure
    server_addr.sin_family = AF_INET;
    inet_aton("130.208.243.61", &server_addr.sin_addr);
    length = sizeof(server_addr);
    server_addr.sin_port = htons(last_port); 

    // Make a connection to socket
    connect(last_sock, (sockaddr*)&server_addr, length);
        
    // Send message to socket with 'knock' message
    if(sendto(last_sock, buffer, msg_len, 0, (const struct sockaddr *)&server_addr, length) < 0) 
    {
        perror("Not able to send to server (last port).");
        return -1;
    } 
    std::cout << "done!" << std::endl;


    // When final port has been sent the secret phrase, print out the received message from port

    // Buffer for receiving message from server / port
    char recvBuffer[4000];
    memset(recvBuffer, 0, sizeof(recvBuffer));
    int len = sizeof(recvBuffer);

    // Create a textfile to store the message from port
    ofstream MyLastFile("lastmessage.txt");

    // Try to retrieve message from port
    int msg_recv = recvfrom(last_sock, recvBuffer, sizeof(recvBuffer), 0, (sockaddr *)&server_addr, &length);

    // Send error message if not able to collect message from port
    if(msg_recv < 0) 
    {
        std::cout << "Could not get message from server (last port)." << std::endl;
        printf("-------------------------\n");

    } 

    // ... else, retrieve message from port
    else
    {
        // Write return message into textfile
        MyLastFile << recvBuffer << std::endl;

        // Variables for reading the textfile into a string
        std::ifstream MyLastFile("lastmessage.txt");
        std::string str_out;
        std::string lastport_content;

        // Getting the content of the file and output to the text string
        while (std::getline(MyLastFile, str_out))
        {
            lastport_content += str_out;
        }

        // Find the second hidden port number within the string
        std::cout << "\nMessage retrieved from port number " << last_port << "..." << std::endl;
        std::cout << "The message is:\n" << lastport_content << std::endl;
        printf("-------------------------\n");
         
        }                        

    close(last_sock);
    return 0;
}



int main()
{
    // Variables for reading the textfile into a string
    std::ifstream MyFile("oracle.txt");
    std::string str_out;

    // Getting the content of the file and output to the text string
    while (std::getline(MyFile, str_out)) { oracle_content += str_out; }

    // Find the ports in textstring, and add to an array
    int index1 = oracle_content.find(",");
    ports.push_back(atoi(oracle_content.substr(index1-4, index1).c_str()));      //index0 - index 3
    ports.push_back(atoi(oracle_content.substr(index1+1, index1+4).c_str()));    // index5 - index8
    ports.push_back(atoi(oracle_content.substr(index1+6, index1+9).c_str()));    // index10 - index13
    ports.push_back(atoi(oracle_content.substr(index1+11, index1+14).c_str()));  // index15 - index18
    ports.push_back(atoi(oracle_content.substr(index1+16, index1+19).c_str()));  // index20 - index23

    KnockOnPorts();
}