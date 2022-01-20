/* 
University of Reykjavik
Computer Networks (TSAM)
Project 2 - Part 2
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
#include <errno.h>
#include <unistd.h>            
#include <netdb.h>              
#include <iostream>  
#include <string.h> 
#include <string> 
#include <sstream> 
#include <fstream>
#include <algorithm>
#include <netinet/ip.h>
#include <netinet/udp.h>
#include <fstream>
using namespace std;


/* 
References:
Coding during TA session (09/09/20) - Benedikt Hólm Þórðarson (raw sockets)
https://stackoverflow.com/questions/13035674/how-to-read-line-by-line-or-a-whole-text-file-at-once
https://man7.org/linux/man-pages/man2/bind.2.html 
https://www.tenouk.com/Module43a.html 
https://www.binarytides.com/tcp-syn-portscan-in-c-with-linux-sockets/ 
https://www.binarytides.com/raw-sockets-c-code-linux/
https://linux.die.net/man/3/strcpy 
https://tools.ietf.org/html/rfc1071 
https://www.securitynik.com/2015/08/calculating-udp-checksum-with-taste-of.html 
https://www.geeksforgeeks.org/converting-strings-numbers-cc/ 
*/


int FirstHiddenPort = 0;
int SecondHiddenPort = 0;
char* SecretPhrase;
std::string file_contents;
int target_checksum = 0;
int ChecksumPort;


// Needed for udp header checksum calculations - Taken from: https://www.binarytides.com/raw-sockets-c-code-linux/  
struct pseudo_header
{
	u_int32_t source_address;
	u_int32_t dest_address;
	u_int8_t placeholder;
	u_int8_t protocol;
	u_int16_t udp_length;
};


// Generic checksum calculation function - Taken from: https://www.binarytides.com/raw-sockets-c-code-linux/ 
unsigned short csum(unsigned short *ptr, int nbytes) 
{
    register long sum;
    unsigned short oddbyte;
    register short answer;
 
    sum = 0;
    while(nbytes > 1) 
    {
        sum += *ptr++;
        nbytes -= 2;
    }

    if(nbytes == 1) 
    {
        oddbyte = 0;
        *((u_char*)&oddbyte) = *(u_char*)ptr;
        sum += oddbyte;
    }
 
    sum = (sum >> 16) + (sum & 0xffff);
    sum = sum + (sum >> 16);
    answer = (short)~sum;

/* Decimal to hex value:
    std::stringstream ss;
    ss<< std::hex << answer << "\n"; 
    std::string res ( ss.str() );
    std::cout << res;
*/

    return(answer);
}



// Send to the oracle the hidden ports, format: <firstport>, <secondport>
int sendOracle() 
{
    // Find number of fourth (oracle) port found in Part 1
    int index1 = file_contents.find("\nI am the oracle");
    int oracle_port = atoi(file_contents.substr(index1 - 4).c_str());

    // Initalizing variables to send to oracle port
    int oracle_sock;
    char buffer[9];
    memset(buffer, 0, sizeof(buffer)); 
    socklen_t length;
    struct sockaddr_in server_addr;
    
    // Message to send to server
    std::string message;
    message = std::to_string(FirstHiddenPort) + "," + std::to_string(SecondHiddenPort);
    strcpy(buffer, message.c_str());
    int msg_len = strlen(buffer) + 1;

    // If not able to create a socket, send error message
    if((oracle_sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) 
    {
        perror("Not able to create UDP socket (oracle port).");
        return -1;
    }
    
    std::cout << "\nSending the Oracle the hidden port numbers: '" << message << "'" << std::endl;
    // Setup socket address structure
    server_addr.sin_family = AF_INET;
    inet_aton("130.208.243.61", &server_addr.sin_addr);
    length = sizeof(server_addr);
    server_addr.sin_port = htons(oracle_port); 

    // Make a connection to socket
    connect(oracle_sock, (sockaddr*)&server_addr, length);

    // Send message to socket with the hidden port numbers
    if(sendto(oracle_sock, buffer, msg_len, 0, (const struct sockaddr *)&server_addr, length) < 0) 
    {
        perror("Not able to send to server (oracle port).");
        return -1;
    } 
    std::cout << "Done!" << std::endl;
    
    // Buffer for receiving message from oracle port
    char recvBuffer[4000];
    memset(recvBuffer, 0, sizeof(recvBuffer));
    int len = sizeof(recvBuffer);

    // Create a textfile to store the message from oracle port
    ofstream MyFile("oracle.txt");

    // Try to retrieve message from oracle port
    int msg_recv = recvfrom(oracle_sock, recvBuffer, len, 0, (sockaddr *)&server_addr, &length);

    // Send error message if not able to collect message from port
    if(msg_recv < 0) 
    {
        std::cout << "Could not get message from server (oracle port)." << std::endl;
    } 

    // ... else, retrieve message from port
    else
    {
        // Write return message into textfile
        MyFile << recvBuffer << std::endl;

        // Variables for reading the textfile into a string
        std::ifstream MyFile("oracle.txt");
        std::string str_out;
        std::string oracle_content;

        // Getting the content of the file and output to the text string
        while (std::getline(MyFile, str_out))
        {
            oracle_content += str_out;
        }

        // Display the message given by the Oracle port
        std::cout << "\nMessage retrieved from the Oracle port:" << std::endl;
        std::cout << oracle_content;
           
    }                        

    close(oracle_sock);
    printf("\n-------------------------\n");        
    return 0;
}


// Create a valid UDP checksum via raw socket, for sending to the 'secret phrase' port
// Large part used from source: https://www.binarytides.com/raw-sockets-c-code-linux/ 
int SendChecksum() 
{
    std::cout << "Creating a raw socket to send calculated checksum...\n";

    // Create a raw socket connection, excluding protocol headers
    int raw_sock = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);    

    // Bind socket to network interface - https://stackoverflow.com/questions/14478167/bind-socket-to-network-interface 
    //    int optionValue = 1;
    //    setsockopt(raw_sock, SOL_SOCKET, SO_BINDTODEVICE, (void *)&optionValue, sizeof(optionValue));

    // Check if socket has been created, else send error message
    if(raw_sock < 0) 
    {
        perror("Not able to open raw socket (checksum port)...");
        return -1;
    }

    // Data in headers to be sent via packet
	char packet[4000], source_ip[32], *data, *pseudogram;
	memset (packet, 0, sizeof(packet));

    // Pointers on packet
	struct iphdr *iph = (struct iphdr *) packet;
	struct udphdr *udph = (struct udphdr *) (packet + sizeof(struct ip));
	struct sockaddr_in sin;
	struct pseudo_header psh;
	data = packet + sizeof(struct iphdr) + sizeof(struct udphdr);
    strcpy(data , "Hello");     // Message written into packet
	
	// Address resolution
	strcpy(source_ip, "192.168.1.112");            // My IP address     - checked also 85.220.100.53
	sin.sin_family = AF_INET;
	sin.sin_port = htons(ChecksumPort);
	sin.sin_addr.s_addr = inet_addr("130.208.243.61");         // Skel IP address

    // IP Header
	iph->ihl = 5;
	iph->version = 4;
	iph->tos = 0;
	iph->tot_len = sizeof (struct iphdr) + sizeof (struct udphdr) + strlen(data);
	iph->id = htonl (54321);
	iph->frag_off = htons(0x8000);             // Setting the 'evil bit' or the reserved bit
	iph->ttl = 255;
	iph->protocol = IPPROTO_UDP;
	iph->check = 0;
	iph->saddr = inet_addr(source_ip);
	iph->daddr = sin.sin_addr.s_addr;
	
	// Calculate IP checksum
    // iph->check = csum((unsigned short *)packet, iph->tot_len);
	
	// UDP Header
    udph->source = htons(1337);
	udph->dest = htons(ChecksumPort);
    udph->len = htons(8 + strlen(data));    // Header size
	udph->check = 0;	                    //leave checksum 0 now, filled later by pseudo header

    // Create UDP checksum
	psh.source_address = inet_addr(source_ip);
	psh.dest_address = sin.sin_addr.s_addr;
	psh.placeholder = 0;
	psh.protocol = IPPROTO_UDP;
	psh.udp_length = htons(sizeof(struct udphdr) + strlen(data));
	
	int psize = sizeof(struct pseudo_header) + sizeof(struct udphdr) + strlen(data);
    pseudogram = (char*) malloc(psize);             

    memcpy(pseudogram, (char*)&psh , sizeof(struct pseudo_header));
	memcpy(pseudogram + sizeof(struct pseudo_header), udph, sizeof(struct udphdr) + strlen(data));
	
	udph->check = csum((unsigned short*)pseudogram, psize);
	
    //Send message (packet) to server / port
    std::cout << "\nSending calculated checksum back to port " << ChecksumPort << "...";

	int sending_msg = sendto(raw_sock, packet, iph->tot_len, 0, (struct sockaddr *)&sin, sizeof(sin));

    // If not possible to send to server, display error message
    if(sending_msg < 0)
	{
        perror("Was not able to send message to server (checksum port)...");
        return -1;	
    }

    std::cout << "done!" << std::endl;
    printf ("Packet Sent - Length: %d \n" , iph->tot_len);

    // Create UDP socket to receive message from server
    int new_sock;
    if((new_sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_ICMP)) < 0)
    {
        perror("Not able to create UDP socket (checksum port).");
        return -1;
    }

    // Buffer for receiving message from server
    char portBuffer[1024];
    memset(portBuffer, 0, sizeof(portBuffer)); 

    // Create a textfile to store the message (secret phrase) from port
    ofstream MySecretFile("secretphrase.txt");

    std::cout << "\nRetreiving message back from server..." << std::endl;
    // Setup select() option for timeout (ignoring ports that don't respond in time)
    fd_set curr_socket;
    FD_SET(raw_sock, &curr_socket);
    struct timeval timeout;      
    timeout.tv_sec = 8;             // X second timeout
    timeout.tv_usec = 0;            // Y millisecond timeout
            
    // select() uses a timeout that is a struct timeval (with seconds and microseconds), checking to see if anything is being received
    if(select(new_sock + 1, &curr_socket, NULL, NULL, &timeout) > 0) 
    {
        // Checking to see if anything is being received from server on given port
        socklen_t serverlen = sizeof(sin);
        int return_msg = recvfrom(new_sock, (char *)portBuffer, sizeof(portBuffer), 0, (struct sockaddr *)&sin, &serverlen);
            
        // If not, send an error message
        if(return_msg < 0) 
        {
            std::cout << "Could not get message from server (checksum port)." << std::endl;
        }         
                
        // ... else, display the message received from server by extracting from buffer and printing it out
        else 
        {
            // Write return message into textfile
            MySecretFile << portBuffer << std::endl;

            // Variables for reading the textfile into a string
            std::ifstream MySecretFile("secretphrase.txt");
            std::string str_out;
            std::string secret_content;

            // Getting the content of the file and output to the text string
            while(std::getline(MySecretFile, str_out))
            {
                secret_content += str_out;
            }

            std::cout << "Secret phrase:\n" << secret_content << "\n";
        } 
    }
    else {
        std::cout << "Not able to retrieve message from port " << ChecksumPort << "..." << std::endl;
    }

    return 0;
}



// Contacting second port with group name (group_32), and later a valid checksum
int SecondPort() {
    // Find number of second port number found in Part 1
    int index1 = file_contents.find("\nSend me");
    int second_port = atoi(file_contents.substr(index1 - 4).c_str());
    std::cout << "Sending group name to (checksum) port number " << second_port << "...";

    // Make the port number a global variable, to be used in checksum-function
    ChecksumPort = second_port;

    // Initalizing variables to send to port
    int contact_sock;
    char newBuffer[1400];
    memset(newBuffer, 0, sizeof(newBuffer)); 
    socklen_t length;
    struct sockaddr_in server_addr;
    
    // Message to send to port
    strcpy(newBuffer, "$group_32$");
    int msg_len = strlen(newBuffer) + 1;

    // If not able to create a socket, send error message
    if((contact_sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) 
    {
        perror("Not able to create UDP socket (contact port).");
        return -1;
    }
    
    // Setup socket address structure
    server_addr.sin_family = AF_INET;
    inet_aton("130.208.243.61", &server_addr.sin_addr);
    length = sizeof(server_addr);
    server_addr.sin_port = htons(second_port); 

    // Make a connection to socket
    connect(contact_sock, (sockaddr*)&server_addr, length);

    // Send message to socket with group name (32)
    if(sendto(contact_sock, newBuffer, msg_len, 0, (const struct sockaddr *)&server_addr, length) < 0) 
    {
        perror("Not able to send to server (contact port).");
        return -1;
    } 
    std::cout << "done!" << std::endl;
    std::cout << "\nRetrieving the checksum value given by port " << second_port << "..." << std::endl;

    // Buffer for receiving message from server / port
    char recvBuffer[4000];
    memset(recvBuffer, 0, sizeof(recvBuffer));
    int len = sizeof(recvBuffer);

    // Create a textfile to store the message (incl. checksum value) from port
    ofstream MyChecksumFile("checksum.txt");

    // Try to retrieve message from port
    int msg_recv = recvfrom(contact_sock, recvBuffer, len, 0, (sockaddr *)&server_addr, &length);

    // Send error message if not able to collect message from port
    if(msg_recv < 0) 
    {
        std::cout << "Could not get message from server (contact port)." << std::endl;
    } 
        
    // ... else, write message into textfile and retrieve the checksum value given
    else
    {
        // Write return message into textfile
        MyChecksumFile << recvBuffer << std::endl;

        // Variables for reading the textfile into a string
        std::ifstream MyChecksumFile("checksum.txt");
        std::string str_out;
        std::string checksum_content;

        // Getting the content of the file and output to the text string
        while (std::getline(MyChecksumFile, str_out))
        {
            checksum_content += str_out;
        }

        // Find the hexnumber for the checksum value within the string
        unsigned firstIndex = checksum_content.find("of ");
        unsigned lastIndex = checksum_content.find(" from");
        string checksum = checksum_content.substr(firstIndex + sizeof("of"), lastIndex - firstIndex - sizeof("of"));
        std::cout << "Checksum value: " << checksum << "\n" << std::endl;

        close(contact_sock);
            
        // Convert checksum string to integer
        stringstream geek(checksum);
        geek >> target_checksum;

        // Call function for sending the calculated checksum header to the same port
        SendChecksum();
    }                        
    return 0;
}


// Function for contacting the third port with my group name (group_32)
int ThirdPort() 
{
    // Find number of third port number found in Part 1
    int index1 = file_contents.find("\nWell done young padawan");
    int third_port = atoi(file_contents.substr(index1 - 4).c_str());
    std::cout << "\nSending group name to padawan port number " << third_port << "...";

    // Initalizing variables to send to padawan port
    int padawan_sock;
    char buffer[1400];
    memset(buffer, 0, sizeof(buffer)); 
    socklen_t length;
    struct sockaddr_in server_addr;
    
    // Message to send to server
    strcpy(buffer, "$group_32$");
    int msg_len = strlen(buffer) + 1;

    // If not able to create a socket, send error message
    if((padawan_sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) 
    {
        perror("Not able to create UDP socket (padawan port).");
        return -1;
    }
    
    // Setup socket address structure
    server_addr.sin_family = AF_INET;
    inet_aton("130.208.243.61", &server_addr.sin_addr);
    length = sizeof(server_addr);
    server_addr.sin_port = htons(third_port); 

    // Make a connection to socket
    connect(padawan_sock, (sockaddr*)&server_addr, length);
        
    // Send message to socket with group name (32)
    if(sendto(padawan_sock, buffer, msg_len, 0, (const struct sockaddr *)&server_addr, length) < 0) 
    {
        perror("Not able to send to server (evil port).");
        return -1;
    } 
    std::cout << "done!" << std::endl;
    
    // Buffer for receiving message from server / port
    char recvBuffer[4000];
    memset(recvBuffer, 0, sizeof(recvBuffer));
    int len = sizeof(recvBuffer);

    // Create a textfile to store the message from port
    ofstream MyFile("padawan.txt");

    // Try to retrieve message from port
    int msg_recv = recvfrom(padawan_sock, recvBuffer, sizeof(recvBuffer), 0, (sockaddr *)&server_addr, &length);

    // Send error message if not able to collect message from port
    if(msg_recv < 0) 
    {
        std::cout << "Could not get message from server (evil port)." << std::endl;
    } 

    // ... else, retrieve message from port
    else
    {
        // Write return message into textfile
        MyFile << recvBuffer << std::endl;

        // Variables for reading the textfile into a string
        std::ifstream MyFile("padawan.txt");
        std::string str_out;
        std::string padawan_content;

        // Getting the content of the file and output to the text string
        while (std::getline(MyFile, str_out))
        {
            padawan_content += str_out;
        }

        // Find the second hidden port number within the string
        std::cout << "\nMessage retrieved from port number " << third_port << "..." << std::endl;
        int index = padawan_content.find(":");
        SecondHiddenPort = atoi(padawan_content.substr(index + 1).c_str()); 
        std::cout << "Second hidden port number is: " << SecondHiddenPort << "\n" << std::endl;
            
        }                        
    close(padawan_sock);
    return 0;
}


int FirstPort() 
{
    printf("-------------------------\n");
    // Variables for reading the textfile from part 1 into a string
    std::ifstream MyFile("ports.txt");
    std::string str_output;

    // Getting the content of the file and output to text string, line by line
    while (std::getline(MyFile, str_output))
    {
        file_contents += str_output;
        file_contents.push_back('\n');
    }

    // Find the number of the first port found in Part 1
    int index1 = file_contents.find("4");
    int first_port = atoi(file_contents.substr(index1, index1 + 4).c_str());

    // Find the first hidden port stored in string
    int index2 = file_contents.find(" 4");
	FirstHiddenPort = atoi(file_contents.substr(index2).c_str());
    std::cout << "Message retrieved from port number " << first_port << "..." <<"\nFirst hidden port number is: " << FirstHiddenPort << std::endl;

    return 0;
}



int main() 
{
    FirstPort();            // Get first hidden port 
    ThirdPort();            // Get second hidden port
    SecondPort();           // Get secret phrase - here, also called function SendChecksum()
    sendOracle();           // Send oracle information about hidden ports: <port1>, <port2>
}    

