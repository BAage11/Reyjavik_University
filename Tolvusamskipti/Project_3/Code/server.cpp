// Simple chat server for TSAM-409
// Command line: ./chat_server 4000 
// Author: Jacky Mallett (jacky@ru.is)

// Project 3: The Botnet Rises
// Co-Author(student):  Benjamín Aage Birgisson (benjamin18@ru.is)
// Group No.32

#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <iostream>
#include <sstream>
#include <thread>
#include <unistd.h>

#define BACKLOG  5          // Allowed length of queue of waiting connections

// Added:
#include <ifaddrs.h>
#include <fstream>
#include <net/if.h>
#include <dirent.h>
#include <ctime>
#include <list>
using std::string;
using std::cout;

/* ----------------------------------------------------------------------------------
References:
    Simple client/server example, by Jacky Mallett (head-teacher of TSAM)
    Code to find local ip address, by Jacky Malled (head-teacher of TSAM)
    http://www.cplusplus.com/reference/sstream/ostringstream/     
    https://github.com/kristinbjorg112/Project3
    https://github.com/dbgs2/TSAM-Project-3
    https://www.tutorialspoint.com/cplusplus/cpp_date_time.htm  
    http://www.cplusplus.com/reference/string/string/find/
    https://www.geeksforgeeks.org/substring-in-cpp/ 
    https://www.softwaretestinghelp.com/cpp-sleep/ 
------------------------------------------------------------------------------------*/

std::string MyGroupName = "P3_GROUP_32";
std::string MyIP;
std::string MyPort;
int maxfds;         // Passed to select() as max fd in set


// Simple class for handling connections from clients.
// Client(int socket) - socket to send/receive traffic from client.
class Client
{
    public:
        int sock;                   // socket of client connection
        std::string name;           // Limit length of name of client's user

        Client(int socket) : sock(socket){} 

        ~Client(){}                 // Virtual destructor defined for base class
};

// Simple class for handling connections from servers.
// Server(int socket) - socket to send/receive traffic from server.
class Server
{
    public:
        int sock;                   // socket of server connection
        std::string groupName;      // name of the server
        std::string groupIP;        // ip address of server
        std::string groupPort;      // port number of connected server

        Server(int socket) : sock(socket){} 

        ~Server(){}                 // Virtual destructor defined for base class
};


// Structure for storing message being sent between clients / servers
struct StoreMessage
{
    std::string messageSender;
    std::string messageContent;
};


// Lookup table for per Client / per Server information
std::map<int, Client*> clients; 
std::map<int, Server*> servers; 

// Lookup table for messages
std::map<std::string, std::vector<StoreMessage>> messages;

// List of servers to be removed (have called the serverCommand 'LEAVE')
std::vector<int> removeServers;


// Open socket for specified port.
// Returns -1 if unable to create the socket for any reason.
int open_socket(int portno)
{
    struct sockaddr_in sk_addr;   // address settings for bind()
    int sock;                     // socket opened for this port
    int set = 1;                  // for setsockopt

    // Create socket for connection. Set to be non-blocking, so recv will
    // return immediately if there isn't anything waiting to be read.
    if((sock = socket(AF_INET, SOCK_STREAM | SOCK_NONBLOCK, 0)) < 0)
    {
        perror("Failed to open socket");
        return(-1);
    }

    // Turn on SO_REUSEADDR to allow socket to be quickly reused after program exit.
    if(setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &set, sizeof(set)) < 0)
    {
        perror("Failed to set SO_REUSEADDR:");
    }
    set = 1;
    memset(&sk_addr, 0, sizeof(sk_addr));

    sk_addr.sin_family      = AF_INET;
    sk_addr.sin_addr.s_addr = INADDR_ANY;
    sk_addr.sin_port        = htons(portno);

    // Bind to socket to listen for connections from clients
    if(bind(sock, (struct sockaddr *)&sk_addr, sizeof(sk_addr)) < 0)
    {
        perror("Failed to bind to socket:");
        return(-1);
    }
   
    else
    {
        return(sock);
    }
}


// Close a client's connection, remove it from the client list, and tidy up select sockets afterwards.
void closeClient(int clientSocket, fd_set *openSockets, int *maxfds)
{
    printf("Client closed connection: %d\n", clientSocket);

    // If this client's socket is maxfds then the next lowest one has to be determined. 
    // Socket fd's can be reused by the Kernel, so there aren't any nice ways to do this.
    close(clientSocket);      
    if(*maxfds == clientSocket)
    {
        for(auto const& p : clients)
        {
            *maxfds = std::max(*maxfds, p.second->sock);
        }
    }

    // And remove from the list of open sockets.
    FD_CLR(clientSocket, openSockets);
}


// Close a server's connection, remove it from the server list, and tidy up select sockets afterwards.
void closeServer(int serverSocket, fd_set *openSockets, int *maxfds)
{
    printf("Server closed connection: %d\n", serverSocket);

    // If this client's socket is maxfds then the next lowest one has to be determined. 
    // Socket fd's can be reused by the Kernel, so there aren't any nice ways to do this.
    close(serverSocket);      
    if(*maxfds == serverSocket)
    {
        for(auto const& p : servers)
        {
            *maxfds = std::max(*maxfds, p.second->sock);
        }
    }

    // And remove from the list of open sockets.
    FD_CLR(serverSocket, openSockets);
}



// Get a timestamp in the form: Weekday Month Date HH:MM:SS Year
// f.x. Sun Oct 20 18:13:22 2020
std::string timeStamp()
{
    // Current date/time
    time_t now = time(0);

    // Convert to string
    char* timestamp = ctime(&now);
    
    return timestamp;
};


// Log the commands sent and received, with timestamp, from client to server
void logCommand(std::string logContent)
{
    // Change string into buffer content
    char writeToBuffer[logContent.length()];
    memset(writeToBuffer, 0, sizeof(writeToBuffer));
    strcpy(writeToBuffer, logContent.c_str());

    // Get date and time
    std::string time = timeStamp();

    // Write (log) into textfile message sent, with date
    std::ofstream file;
    file.open("./logs.txt", std::ios::in | std::ios::app | std::ios::out);
    file << time;
    file << writeToBuffer << std::endl;
    file.close();
}

 
// Adding token parameters (SOH and EOH) before sending message to another server
void sendMessage(int socket, std::string message)
{
    // Creating the string format, including the token characters at start/end of message
    std::string SOH = "*";
    std::string EOH = "#";
    std::string sendMsg = SOH + message + EOH + "\n";

    // Send message over to server
    send(socket, sendMsg.c_str(), sendMsg.length(), 0);
}


// Remove token parameters from a serverCommand
std::string removeTokens(std::string message)
{
    std::string removedTokenFromMsg;
    
    // Removing backend of message, which should always be '#'
    removedTokenFromMsg = message.erase(message.length() - 2, 1);

    // Removing frontend of message, which should always be '*'
    removedTokenFromMsg = removedTokenFromMsg.erase(0, 1);

    return removedTokenFromMsg;
}


// Check if a serverCommand message is valid 
// That is, that token parameters (SOH & EOH) are included
std::string validateMsg(char *message)
{
    // Create a string from the char* buffer, and strings for the two tokens to be found
    std::string command(message);
    std::string token1 = "*";
    std::string token2 = "#";

    // Search for SOH token. If found, create new string beginning with SOH token
    std::size_t found1 = command.find(token1);
    if (found1 != std::string::npos)
    {
        command.substr(found1, command.length());
    }

    // If SOH token not found, return False (command string not valid)
    else
    {
        return "False";
    }
    
    // If SOH found, search for EOH. If EOH token found... 
    std::size_t found2 = command.find(token2);
    if (found2 != std::string::npos)
    {
        // create new string starting with SOH and ending with EOH tokens  
        command.substr(0, found2);

        // And then remove token characters from command, to be processed within serverCommand() function
        command = removeTokens(command);
        
        // Return the newly created (sub-)string
        return command;
    }

    // If EOH token not found, return False (command string not valid)
    else
    {
        return "False";
    }
}


// Function for removing all commas within a given command from client / server
std::string removeCommasFromCommand(std::string command)
{
    for (char &letter : command)
    {
        if (letter == ',')
        {
            letter = ' ';
        }
    }
    return command;
};


// List servers this server is connected to
// eg. LISTSERVERS,<ThisServerName>,<ServerConnected1>,<ServerConnected2>,....;
std::string listServers()
{
    // Create start of return string
    std::string listServers = "LISTSERVERS:" + MyGroupName + ",";

    // Check if servers list is empty. 
    // If not empty, add connected servers to return string
    if (!servers.empty())
    {
        for (auto const &item : servers)
        {
            // If groupId of server is listed, add to the return string
            if (!item.second->groupName.empty())
            {
                listServers += item.second->groupName + ",";
            }
        }

        // Remove the last ',' from the string, and add a ";" instead
        listServers = listServers.substr(0, listServers.size() - 1);
        listServers += ";";

        // Return the string of servers connected to this server
        return listServers;
    }

    // Remove the last ',' from the string, and add a ";" instead
    listServers = listServers.substr(0, listServers.size() - 1);
    listServers += ";";

    // Return the string, only containing this server (as no other is connected)
    return listServers;
}


// Function for connecting this server to another server 
// Based on client.cpp code snippers, for connecting to a server
bool CONNECTSERVERS(fd_set *openSockets, std::string connectingIP, std::string connectingPort)
{
    struct addrinfo hints, *svr;              // Network host entry for server
    int serverSocket;                         // Socket used for server 
    int set = 1;                              // Toggle for setsockopt

    memset(&hints,   0, sizeof(hints));

    hints.ai_family   = AF_INET;              // IPv4 only addresses
    hints.ai_socktype = SOCK_STREAM;
    
    const char *ipAddress = connectingIP.c_str();
    const char *portNo = connectingPort.c_str();

    if(getaddrinfo(ipAddress, portNo, &hints, &svr) != 0)
    {
        perror("getaddrinfo failed: ");
        return 0;
    }

    serverSocket = socket(svr->ai_family, svr->ai_socktype, svr->ai_protocol);

    // Turn on SO_REUSEADDR to allow socket to be quickly reused after program exit.
    if(setsockopt(serverSocket, SOL_SOCKET, SO_REUSEADDR, &set, sizeof(set)) < 0)
    {
        printf("Failed to set SO_REUSEADDR for port %s\n", portNo);
        perror("setsockopt failed: ");
        return 0;
    }
   
    if(connect(serverSocket, svr->ai_addr, svr->ai_addrlen) < 0)
    {
        printf("Failed to open socket to server: %s\n", ipAddress);
        perror("Connect failed: ");
        return 0;
    }

    FD_SET(serverSocket, openSockets);
    maxfds = std::max(maxfds, serverSocket);

    servers[serverSocket] = new Server(serverSocket);

    // Send Queryservers message to newly connected server
    std::cout << "Sending QUERYSERVERS command to newly connected server." << std::endl;
    std::string queryMsg = "QUERYSERVERS," + MyGroupName;
    sendMessage(serverSocket, queryMsg);

    // Log message within textfile
    logCommand(queryMsg);

    return 1;
};


// Process command from client on the server
void clientCommand(int clientSocket, fd_set *openSockets, int *maxfds, char *buffer) 
{
    // Output the command given by the client
    std::string command(buffer);
    std::string time = timeStamp();
    std::cout << "\n--------\n" << time << "clientCommand: " << command << std::endl;

    std::vector<std::string> tokens;
    std::string token;

    // Remove commas from command, so tokens can be processed properly
    if (command.find(",") != std::string::npos)
    {
        std::string temp;
        temp = removeCommasFromCommand(command);
        command = temp;
    }

    // Split command from client into tokens for parsing
    std::stringstream stream(command);
    while(stream >> token)
        tokens.push_back(token);

    if((tokens[0].compare("CONNECT") == 0) && (tokens.size() == 2))
    {
        std::cout << "Connecting client: '" << tokens[1] << "'... Done!" << std::endl;
        clients[clientSocket]->name = tokens[1];

        std::string returnMsg = "Client '" + tokens[1] + "' has hereby been connected to server " + MyGroupName;
        send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);
    }

    else if(tokens[0].compare("LEAVE") == 0)
    {
        std::cout << "Processing command 'LEAVE'" << std::endl;
        // Close the socket, and leave the socket handling code to deal with tidying up clients etc. 
        // when select() detects the OS has torn down the connection.
        std::cout << "Disconnecting client..." << std::endl;
        closeClient(clientSocket, openSockets, maxfds);

        std::string returnMsg = "Disconnection established, see you later!";
        send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);
    }
 
    else if(tokens[0].compare("WHO") == 0)
    {
        std::cout << "Who is logged on? \nThe following clients:\n";
        std::string msg;

        for(auto const& names : clients)
        {
            msg += names.second->name + ",";
        }

        // Removing the last ',' in string
        msg = msg.substr(0, msg.size() - 1);

        // Checking the string, and change if no client is connected (to send back)
        if (msg == "")
        {
            msg = "No client is currently connected...";
        }

        std::cout << msg << std::endl;
        send(clientSocket, msg.c_str(), msg.length(), 0);
    }

    else if((tokens[0].compare("MSG") == 0) && (tokens[1].compare("ALL") == 0))
    {
        std::cout << "Processing command 'MSG ALL <MsgContent>'" << std::endl;
        std::string msg;
        for(auto i = tokens.begin() + 2; i != tokens.end(); i++) 
        {
            msg += *i + " ";
        }
        // Remove the last ' ' from the string
        msg = msg.substr(0, msg.size() - 1);

        for(auto const& pair : clients)
        {
            send(pair.second->sock, msg.c_str(), msg.length(),0);
        }
        std::cout << "The following message was sent to all clients:" << std::endl;
        std::cout << msg << std::endl;
    }

    else if(tokens[0].compare("MSG") == 0)
    {
        std::cout << "Processing command 'MSG GroupId <MsgContent>'" << std::endl;
        std::string msg;
        for(auto const& pair : clients)
        {
            for(auto i = tokens.begin() + 2; i != tokens.end(); i++) 
            {
                msg += *i + " ";
            }
            // Remove the last ' ' from the string
            msg = msg.substr(0, msg.size() - 1);

            if(pair.second->name.compare(tokens[1]) == 0)
            {
                send(pair.second->sock, msg.c_str(), msg.length(), 0);

                std::cout << "The following message was sent to client '" << tokens[1] << "':" << std::endl;
                std::cout << msg << std::endl;  

                std::string returnMsg = "The message '" + msg + "' has hereby been sent to " + tokens[1] + ".";
                send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);
            }

            else
            {
                std::string returnMsg = "The client '" + tokens[1] + "' is currently not connected.\nNot able to send direct message.";
                std::cout << returnMsg << std::endl;
                send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);
            }
        }
    }

    // Command: GETMSG <GroupId>
    // Get a single message from the server for the GROUP ID
    else if ((tokens[0].compare("GETMSG") == 0) && (tokens.size() == 2))
    {
        std::cout << "Processing command 'GETSG <GroupId>'" << std::endl;
        // Iterate throught message map, to see if the groupId given has any messages
        for (auto const &server : messages) 
        {
            // If groupId found, check if there are any messages unsent left
            if (tokens[1].compare(server.first) == 0)
            {
                // If no messages found...
                if (server.second.size() != 0)
                {
                    // Retrieve and send back the first (singular) message for given groupId
                    for (auto &mail : server.second)
                    {
                        std::string returnMsg = "SEND_MSG," + tokens[1] + "," + mail.messageSender + "," + mail.messageContent + ";";

                        // Send to requesting client the message for groupId (if any)
                        send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);
                        std::cout << returnMsg << std::endl;
                        
                        // Log the sent message to client
                        logCommand(returnMsg);        

                        break;
                    }
                }
            }
        }
    }

    // Command: SENDMSG <GroupId>
    // Send a message to the server for the GROUP_ID
    else if ((tokens[0].compare("SENDMSG")) == (0 && tokens.size() == 2))
    {
        std::cout << "Processing command 'SENDMSG <GroupId>'" << std::endl;

        // Create a 'random' string to be sent, as it is not included in the command
        std::string msg = "Hello there!";

        // Create mail content
        StoreMessage mail;
        mail.messageSender = MyGroupName;
        mail.messageContent = msg;

        // Store mail content for server being sent to
        messages[tokens[1]].push_back(mail);

        // Send confirmation back to client
        std::string returnMsg = "The message '" + msg + "' hereby stored for client '" + tokens[1] + "'.";
        send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);
        std::cout << "Message stored for client '" << tokens[1] << "'" << std::endl;

        // Log the message sent
        logCommand(returnMsg);
    }

    // Command: LISTSERVERS
    // Returns a list of connecterd servers to this server
    else if ((tokens[0].compare("LISTSERVERS") == 0) && (tokens.size() == 1))
    {
        std::cout << "Processing command 'LISTSERVERS'" << std::endl;
        // Call the function listServers(), which lists all connected servers in a string
        std::string returnMsg = listServers();
        std::cout << returnMsg << std::endl;

        // Send the list of servers back to requesting client
        send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);

        // Log the message sent
        logCommand(returnMsg);
    }

    // Command: CONNECTSERVERS <IPaddress> <PortNo>
    // Try and connect this server to another server, with given IP address and port number
    else if ((tokens[0].compare("CONNECTSERVERS") == 0) && (tokens.size() == 3))
    {
        std::cout << "Processing command 'CONNECTSERVERS <IPaddress> <PortNo>'" << std::endl;
        // Check if the maximum number of connected servers to this server has been reached (max=15)
        if (servers.size() >= 15)
        {
            std::cout << ">>> The maximum amount of servers (15) has already been reached <<<" << std::endl;
            std::string returnMsg = "The server '" + MyGroupName + "' has already reached its maximum capacity.\nPlease try again later.";
            send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);

            // Log the message sent
            logCommand(returnMsg);
        }

        else
        {
            // Try and connect the two servers
            if(CONNECTSERVERS(openSockets, tokens[1], tokens[2]))
            {
                std::string returnMsg ="Connection to server IP " + tokens[1] + " on port " + tokens[2] + " has been made.";
                send(clientSocket, returnMsg.c_str(), returnMsg.length(),0);
                logCommand(returnMsg);
            }
    
            else
            {
                std::string returnMsg = "Not able to connect to new server at this moment in time.";
                send(clientSocket, returnMsg.c_str(), returnMsg.length(),0);
                logCommand(returnMsg);
            }
        }
    }

    else
    {
        std::cout << "Unknown command from client: " << buffer << std::endl;
        std::string returnMsg = "Unknown command from client...";
        send(clientSocket, returnMsg.c_str(), returnMsg.length(), 0);
    }     
}


// Get the local IP address for this server
std::string getIP()
{
    struct ifaddrs *myaddrs, *ifa;    
    void *in_addr;    
    char buf[64];    
    std::ostringstream returnMsg;
    
    if(getifaddrs(&myaddrs) != 0)    
    {        
        perror("getifaddrs");        
        exit(1);    
    }    
        
    for (ifa = myaddrs; ifa != NULL; ifa = ifa->ifa_next)    
    {        
        if (ifa->ifa_addr == NULL) 
            continue;        
        
        if (!(ifa->ifa_flags & IFF_UP)) 
            continue;        
        
        switch (ifa->ifa_addr->sa_family)        
        {            
            case AF_INET:            
            {                
                struct sockaddr_in *s4 = (struct sockaddr_in *)ifa->ifa_addr;                
                in_addr = &s4->sin_addr;                
                break;            
            }            
            
            case AF_INET6:            
            {                
                struct sockaddr_in6 *s6 = (struct sockaddr_in6 *)ifa->ifa_addr;                
                in_addr = &s6->sin6_addr;                
                break;            
            }            
            
            default:                
                continue;        
        }        
        
        if (!inet_ntop(ifa->ifa_addr->sa_family, in_addr, buf, sizeof(buf)))        
        {            
            printf("%s: inet_ntop failed!\n", ifa->ifa_name);        
        }        
        else        
        {            
            returnMsg << buf << " ";
            // printf("%s: %s\n", ifa->ifa_name, buf);        
        }    
    }

    freeifaddrs(myaddrs);   
    std::string ipAddress = returnMsg.str();
    return ipAddress; 
}


// Directly connected servers to this server formed as a list, 
// the first one being the server sending the command.
// eg. CONNECTED,<MY GROUP ID>,<MY IP>,<MY PORT>;<groupName>,<groupIP>,<groupPort>;....;
std::string CONNECTED()
{
    // Get my local ip address
    std::string getMyIp = getIP();
    std::vector<std::string> ipTokens;
    std::string ipToken;

    // Split string from getMyIP into tokens for parsing
    std::stringstream stream(getMyIp);
    while (stream >> ipToken)
        ipTokens.push_back(ipToken);

    // Retreieve the IP address (token)
    MyIP = ipTokens[1];

    // Creating start of string, including this servers information
    std::string responseString = "CONNECTED," + MyGroupName + "," + MyIP + "," + MyPort + ";";

    // Adding the servers connected to my server to the response string
    for (auto const &item : servers)
    {
        // While still servers to add (server list not empty), continue adding to the return string
        if (!item.second->groupName.empty())
        {
            std::ostringstream addedString;
            addedString << item.second->groupName << ","
                        << item.second->groupIP << ","
                        << item.second->groupPort << ";";

            responseString += addedString.str();
        }
    }
    return responseString;
}


// Function for creating a string with list of connected servers, 
// and the number of messages for each CONNECTED server
// eg. STATUSRESP,FROM GROUP,TO GROUP,<server, msgs held>,...
// eg. STATUSRESP,P3_GROUP_32,I_1,P3_GROUP_4,20,P3_GROUP_71,2....
std::string STATUSRESP(std::string groupId)
{
    // Create beginning of return msg
    std::string statusRespons = "STATUSRESP," + MyGroupName + "," + groupId + ",";

    // Iterate over the lookup table of servers
    for (auto const &item : servers)
    {
        // Retrieve the groupName, to check later for messages
        std::string groupName = item.second->groupName;

        // Iterate through messages, to check if there is any message to server
        for (auto const &msg : messages)
        {
            // Check if the found groupId matches the server being seeked for ("item" in first for-loop)
            if (msg.first.compare(groupName) == 0)
            {
                // Count the number of message to the found server
                std::string count = std::to_string(msg.second.size());

                // Add group name (server) and the number of messages to return string
                statusRespons += groupName + "," + count + ",";
            }
        }
    }
    // Remove the last ',' from the string, and replace with ';' instead
    statusRespons = statusRespons.substr(0, statusRespons.size() - 1);
    statusRespons += ";";

    return statusRespons;
}


// Process command from server on the server
void serverCommand(int serverSocket, fd_set *openSockets, int *maxfds, char *buffer) 
{
    // Trying to delay exessive server commands
    // usleep(1000000);

    // Validate that the command given includes SOH and EOH tokens
    std::string command;
    command = validateMsg(buffer);

    // If not included, send error message
    if (command == "False")
    {
        std::string returnMsg = "Missing SOH and/or EOH from command.";
        sendMessage(serverSocket, returnMsg);

        logCommand(returnMsg);
    }

    // Else, continue with processing the given command from server
    else
    {
        std::cout << "\n\nTokens found, proccessing command from server..." << std::endl;
        // Output the command given by the server, with timestamp
        std::string time = timeStamp();
        std::cout << "\n--------\n" << time << "serverCommand: " << command << std::endl;
        
        std::vector<std::string> tokens;
        std::string token;

        // Remove commas from command, so tokens can be processed properly
        if (command.find(",") != std::string::npos)
        {
            std::string temp;
            temp = removeCommasFromCommand(command);
            command = temp;
        }

        // Split command from server into tokens for parsing
        std::stringstream stream(command);
        while(stream >> token)
            tokens.push_back(token);


        // Command: QUERYSERVERS <FromGroupId>
        // Replies with a CONNECTED message string of directly connected 1-hop servers to this server
        if ((tokens[0].compare("QUERYSERVERS") == 0) && (tokens.size() == 2))
        {
            std::cout << "Processing command 'QUERYSERVERS <FromGroupId>'" << std::endl;

            // Check if the calling server is already connected. If not, send
            // a QUERYSERVERS request, to get a CONNECTED response (incl. the IP address
            // and port number of connected server to be added)
            if ((servers.find(serverSocket) == servers.end()) && (tokens[1] != MyGroupName))
            {
                std::string queryMsg = "QUERYSERVERS," + MyGroupName + ";";
                send(serverSocket, queryMsg.c_str(), queryMsg.length(), 0);
            }

            // Get the connected servers into a string (response message)
            std::string queryResponse = CONNECTED();
            std::cout << queryResponse << std::endl;

            // Send response message back to calling server
            sendMessage(serverSocket, queryResponse);
        }

        // Command: CONNECTED,...
        // Response from a connected server, for a given QUERYSERVERS request
        else if ((tokens[0].compare("CONNECTED") == 0) && tokens.size() > 1)
        {
            std::cout << "\nServer response to QUERYSERVERS command:\n" << buffer << std::endl;

            // If the sending server is not on the connected servers list,
            // add to the list of connecting servers
            if ((servers.find(serverSocket) == servers.end()) && (tokens[1] != MyGroupName))
            {
                // If possible to connect to newly connected server...
                if (CONNECTSERVERS(openSockets, tokens[2], tokens[3]))
                {
                    // ... send a QUERYSERVERS request to the newly connected server
                    std::string queryMsg = "QUERYSERVERS," + MyGroupName + ";";
                    sendMessage(serverSocket, queryMsg);
                }
            }
        }

        // Command: GET_MSG <GroupId>
        // Get messages for the specified groupId (own group or another group)
        else if (tokens[0].compare("GET_MSG") == 0 && tokens.size() == 2)
        {
            std::cout << "Processing command 'GET_MSG <GroupId>'" << std::endl;

            // Lookup messages to see if groupId has a message stored for them
            for (auto const &msg : messages)
            {
                // If groupId found in lookup table of messages...
                if (tokens[1].compare(msg.first) == 0)
                {
                    // Retrieve the messages stored into a return string
                    for (auto &content : msg.second)
                    {
                        // Create a return string for sending message back
                        std::string returnMsg = "SEND_MSG," + tokens[1] + ",";
                        returnMsg += content.messageSender + "," + content.messageContent + ";";

                        // Add starting and ending token characters to return string, and send to calling server (one message at a time)
                        std::cout << returnMsg << std::endl;
                        sendMessage(serverSocket, returnMsg);
                    }
                }
            }
        }

        // Command: SEND_MSG <ToGroupId> <FromGroupId> <msg content>
        // Send message to another group
        else if (tokens[0].compare("SEND_MSG") == 0 && tokens.size() >= 4)
        {
            std::cout << "Processing command 'SEND_MSG <FromGroupId> <ToGroupId> <message>'" << std::endl;

            // Retreive the sent message into a string format
            std::string msg_content;
            for (auto word = tokens.begin() + 3; word != tokens.end(); word++)
            {
                msg_content += *word + " ";
            }

            // Remove the last <whitespace> from the string (" ")
            msg_content = msg_content.substr(0, msg_content.size() - 1);

            // Create the storage for message
            StoreMessage mail;
            mail.messageSender = tokens[2];
            mail.messageContent = msg_content;
                
            // And store the message in message map, for the server being sent to (tokens[1])
            messages[tokens[1]].push_back(mail);

            // Send confirmation to server that message has been stored
            std::string returnMsg = "Message content '" + msg_content + "' has hereby been stored for " + tokens[1] + ".";
            std::cout << returnMsg << std::endl;
            sendMessage(serverSocket, returnMsg);
        }

        // Command: LEAVE <ServerIP> <PortNo>
        // Disconnect from server at specified port
        else if (tokens[0].compare("LEAVE") == 0 && tokens.size() == 3)
        {
            std::cout << "Processing command 'LEAVE <ServerIP> <PortNo>'" << std::endl;

            // Iterate over connected servers in the lookup table for servers
            for (auto const &s : servers)
            {
                // If the given IP address, and the given Port number, is identical to the
                // server found in the lookup table, remove that server (put on a list of servers to be disconnected from)
                if ((tokens[1].compare(s.second->groupIP) == 0) && (tokens[2].compare(s.second->groupPort)== 0))
                {
                    removeServers.push_back(s.first);

                    // Send confirmation back to calling server, that disconnection has been processed
                    std::string returnMsg = "Disconnecting from IP address '" + tokens[1] + "' on port no." + tokens[2] + "... Done!";
                    std::cout << returnMsg << std::endl;
                    sendMessage(serverSocket, returnMsg);
                } 
            }
        }

        // Command: STATUSREQ <FromGroupName>
        // Reply with STATUSRESP string - For more details, see function STATUSRESP(FromGroupId)
        else if (tokens[0].compare("STATUSREQ") == 0 && tokens.size() == 2)
        {
            std::cout << "Processing command 'STATUSREQ <FromGroup>'" << std::endl;

            // Call statusReq() function, for creating the 'StatusResp' string
            std::string returnMsg = STATUSRESP(tokens[1]);

            // Send back to client sending the command, the return string created
            std::cout << returnMsg << std::endl;
            sendMessage(serverSocket, returnMsg);
        }

        else
        {
            std::cout << "Unknown command from server: " << buffer << std::endl;
            std::string returnMsg = "Unknown command from server...\n";
            send(serverSocket, returnMsg.c_str(), returnMsg.length(), 0);
        }   
    }  
}

// Function that sends a KEEPALIVE message to all servers connected, 
// including the number of messages the server has waiting for them
// eg. KEEPALIVE,<No of Messages>
void sendKeepAlive(fd_set *openSockets)
{
    // Iterate over the connected servers, for sending KeepAlive message to all of them
    std::string num;
    for (auto const &item : servers)
    {
        // Check the number of messages for each and every server
        for (auto &msg : messages)
        {
            num = std::to_string(msg.second.size());
        }

        // Check if there where any messages. If not, make count equal to zero (0)
        if (num == "")
        {
            num = "0";
        }

        // Create return string and send KeepAlive message to server, with number of messages stored for specific server
        std::string msg = "KEEPALIVE," + num;
        sendMessage(item.second->sock, msg);

        logCommand(msg);
    }
}


            /* ------------------------------------------------
                             MAIN FUNCTION                       
            ------------------------------------------------- */

int main(int argc, char* argv[])
{
    bool finished;                                  // Boolean for while-loop (below)

    int listenSockClient;                           // Socket for client connections to server
    int listenSockServer;                           // Socket for server connections to server 

    int clientSock;                                 // Socket of connecting client
    int serverSock;                                 // Socket of connecting server

    fd_set openSockets;                             // Current open sockets 
    fd_set readSockets;                             // Socket list for select()        
    fd_set exceptSockets;                           // Exception socket list

    struct sockaddr_in client;                      // Structure for client address
    socklen_t clientLen;                            // Type of length for client sock

    struct sockaddr_in server;                      // Structure for server address
    socklen_t serverLen;                            // Type of length for server sock

    char buffer[1025];                              // buffer for reading from clients

    std::list<Client *> disconnectedClients;        // List of clients being disconnected
    std::list<Server *> disconnectedServers;        // List of servers being disconnected

    // Send error message if server was not initalize correctly
    if(argc != 2)
    {
        printf("Usage: chat_server <ip port>\n");
        exit(0);
    }

    // Sockets created to listen on, with open_socket function
    MyPort = argv[1];
    listenSockServer = open_socket(atoi(argv[1]));    
    listenSockClient = open_socket(atoi(argv[1]) + 1);
    printf("Listening for server connections on port: %d\n", atoi(argv[1])); 
    printf("Listening for client connections on port: %d\n", atoi(argv[1]) + 1);

    // Listen for client(s) to connect to the server
    if(listen(listenSockClient, BACKLOG) < 0)
    {
        printf("Listen (client) failed on port %s\n", argv[1] + 1);
        exit(0);
    }

    // Listen for server(s) to connect to the server
    else if (listen(listenSockServer, BACKLOG) < 0)
    {
        printf("Listen (server) failed on port %s\n", argv[1]);
        exit(0);
    }


    // Add listen socket to socket set we are monitoring
    else 
    {
        FD_ZERO(&openSockets);
        FD_SET(listenSockServer, &openSockets);
        FD_SET(listenSockClient, &openSockets);
        maxfds = std::max(listenSockServer, listenSockClient);
    }


    // Create a struct timeval, for sending KeepAlive messages to servers
    time_t checkTime = time(0);         // initalize timeclock
    time_t timeout = 60;               // send every single minute (60 sec)

    finished = false;
    while(!finished)
    {
        // Get modifiable copy of readSockets
        readSockets = exceptSockets = openSockets;
        memset(buffer, 0, sizeof(buffer));

        // Check if timeout (1 minute) have passed since last KeepAlive message was sent
        // if time has passed, send KeepAlive message to connecting servers
        if (time(0) - checkTime > timeout)      
        {
            sendKeepAlive(&openSockets);
            checkTime = time(0);        // Reset timeclock
        }


        // Look at sockets and see which ones have something to be read()
        int n = select(maxfds + 1, &readSockets, NULL, &exceptSockets, NULL);

        // If select() could not find anything, send error message
        if(n < 0)
        {
            perror("select failed - closing down\n");
            finished = true;
        }

        else
        {
            // First, accept any new connections to the server on the listening client socket
            if(FD_ISSET(listenSockClient, &readSockets))
            {
                // Accept the client socket connection
                clientSock = accept(listenSockClient, (struct sockaddr *)&client, &clientLen);
                printf("\n*** Accepting client ***\n");

                // Add new client to the list of open sockets
                FD_SET(clientSock, &openSockets);

                // And update the maximum file descriptor
                maxfds = std::max(maxfds, clientSock);

                // Create a new client to store information.
                clients[clientSock] = new Client(clientSock);

                // Decrement the number of sockets waiting to be dealt with
                n--;
                printf("Client connected on server: %d\n", clientSock);
            }

            // Second, accept any new connections to the server on the listening server socket
            if (FD_ISSET(listenSockServer, &readSockets))
            {
                // Accept the server socket connection
                serverSock = accept(listenSockServer, (struct sockaddr *)&server, &serverLen);
                printf("\n*** Accepting server ***\n");

                // Add new server to the list of open sockets
                FD_SET(serverSock, &openSockets);

                // And update the maximum file descriptor
                maxfds = std::max(maxfds, serverSock);

                // Check to see if there are now more than 15 servers connected
                if (servers.size() < 15)
                {
                    // If not, connect the new server
                    servers[serverSock] = new Server(serverSock);

                    // Decrement the number of sockets waiting to be dealt with
                    n--;
                    printf("Server connected on server: %d\n", serverSock);

                    // Send a QUERYSERVERS request - first message sent by server, after it connects to another server
//                    std::string welcomeMsg = "QUERYSERVERS," + MyGroupName;
//                    sendMessage(serverSock, welcomeMsg);
                }

                // Else, send message that the maximum capacity has been reached
                else
                {
                    std::string error = "The maximum capacity of connecting servers (15) has already been reached.\nWe'll hopefully see you later when demand has decreased.";
                    std::cout << error << std::endl;
                    sendMessage(serverSock, error);
                }
            }

            // Now check for commands from clients / servers
            while(n-- > 0)
            {
                // Remove the servers that have called the serverCommand 'LEAVE'
                for (auto &item : removeServers)
                {
                    closeServer(item, &openSockets, &maxfds);
                }
                // Clear the vector list, so OS does not try again and again to remove the same server(s)
                removeServers.clear();


                // First, loop through all clients
                for(auto const& pair : clients)
                {
                    Client *client = pair.second;

                    if(FD_ISSET(client->sock, &readSockets))
                    {
                        // recv() == 0 means client has closed connection
                        if(recv(client->sock, buffer, sizeof(buffer), MSG_DONTWAIT) == 0)
                        {
                            disconnectedClients.push_back(client);
                            closeClient(client->sock, &openSockets, &maxfds);
                        }

                        // We don't check for -1 (nothing received) because select()
                        // only triggers if there is something on the socket for us.
                        else
                        {                            
                            // Logging client command into textfile
                            std::string command(buffer);
                            std::string logging = "ClientCommand: " + command;
                            logCommand(logging);

                            clientCommand(client->sock, &openSockets, &maxfds, buffer);
                        }
                    }
                }

                // Remove client from the clients list
                for(auto const& c : disconnectedClients)
                    clients.erase(c->sock);


                // Then, loop through all servers
                for (auto const &pair : servers)
                {
                    Server *server = pair.second;

                    if (FD_ISSET(server->sock, &readSockets))
                    {
                        // recv() == 0 means server has closed connection
                        if (recv(server->sock, buffer, sizeof(buffer), MSG_DONTWAIT) == 0)
                        {
                            disconnectedServers.push_back(server);
                            closeServer(server->sock, &openSockets, &maxfds);
                        }

                        // else, check if there are any messages to be received from server
                        else 
                        {
                            // Logging client command into textfile
                            std::string command(buffer);
                            std::string logging = "ServerCommand: " + command;
                            logCommand(logging);

                            serverCommand(server->sock, &openSockets, &maxfds, buffer);
                        }
                    }
                }
 
                // Remove servers from the servers list
                for(auto const& s : disconnectedServers)
                    servers.erase(s->sock);
            }
        }
    }
}
