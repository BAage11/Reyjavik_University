import time

class VM_Manager():
    def __init__(self):
        """ Initialization of the physical memory (PM). """
        # Physical memory divided into 1024 frames of 512 words each (page) == 524,288 integers
        self.size = 524288
        self.PM = [None] * self.size


    def PM_initialized(self, segment, size, frame):
        """ Physical memory (PM) initialized with given commands, definition of segment table (ST) - A segment which resides in a frame, as well as the size of the segment. """
        # Get the index into the physical memory list
        index = segment * 2
        # Size of the segment (number of words)
        self.PM[index] = size
        # Frame number holding the page table of segment
        self.PM[index+1] = frame


    def page_table(self, segment, page, frame):
        """ With the given segment (s), the specific frame (p) is located, which then again can locate the correct page table, to insert the entry (value) of that page table. """
        # Calculate the given segment for the frame
        index = segment * 2
        # Find the frame for the segment
        PM_frame = self.PM[index+1]
        
        if PM_frame == None:
            quit
        else:
            # Input the page for the frame into the right place in the page table (512 words == frame size)
            self.PM[PM_frame * 512 + page] = frame


    def va_to_pa(self, va_number):
        """ Translate virtual address (VA) into a physical address (PA). """
        # Begin to translate given VA to [p,s,w] binary representation
        binary_addresses = self.decimalToBinary(va_number)

        s = self.binaryToDecimal(binary_addresses[0])   # segment number
        p = self.binaryToDecimal(binary_addresses[1])   # page number
        w = self.binaryToDecimal(binary_addresses[2])   # offset within page

        # Get the pw (offset within a segment)
        pw = self.binaryToDecimal(binary_addresses[1] + binary_addresses[2])

        # If pw >= PM[2s], then VA is outside of the segment boundary and an error is returned
        if pw >= self.PM[2*s]:
            return -1

        # Return the physical address, within the given segment table / page table / page
        # First, retrieve the frame number, multiply it by 512 (frame size) and add p (page number)
        # Then, multiply this by 512 again (page size) and add the offset within the page (w) to get the physical address (PA)
        try:
            return self.PM[self.PM[2*s + 1] * 512 + p] * 512 + w
        except:
            return -1
        
    def decimalToBinary(self, n):  
        """ Function that changes a decimal number into its expected binary number. """
        binary = bin(int(n)).replace("0b", "")  
        
        # VA = (s, p, w), s is segment number, p is page number, w is offset within page
        s = ""
        p = ""
        w = ""

        count = 0
        # Go from rigth to left within the calculated binary number, to get the binary number for s,p, and w
        for num in range(len(binary)-1, -1, -1):
            if count < 9:
                # w (offset) is the first 9 numbers from right to left within the binary
                w = str(binary[num]) + w
            elif count >= 9 and count < 18:
                # p (page number) is the numbers 10-18 winthin the binary number
                p = str(binary[num]) + p
            else:
                # and s (segment number) is the first digits of the binary number
                s = str(binary[num]) + s
            count += 1

        # If VA is equal to zero, then return binary numbers of [s,p,w] as such
        if s == "":
            s = "0"
        if p == "":
            p = "0"
        if w == "":
            w = "0"

        return [s,p,w]
    

    def binaryToDecimal(self, n): 
        """ Convert binary number into its decimal representation. """
        # Base 2 of the binary number, to convert binary into its decimal number
        return int(n,2) 


##############################################################################################################
##############################################################################################################


with open("init-no-dp.txt", 'r') as initialize_PM, open("input-no-dp.txt", 'r') as VA_commands, open("output-no-dp.txt", 'w') as output_file:
    command = VM_Manager()
    print("\nPhysical memory (PM) being created with input file 'init-no-dp.txt'...")
    
    # Start by initializing the physical memory, creating the segment table and the page tables
    line_one = True
    while True:
        line = str(initialize_PM.readline())
        line_listed = line.split(" ")

        for i in line_listed:
            if i.endswith("\n"):
                line_listed[-1] = i.replace("\n", "")
        
        if line_listed == ['']:
            break
        elif line_one == True:
            # Initialize the physical memory (PM) with definition of segment table (ST)
            n = 3
            while line_listed:
                # Get the segment, frame, and segment size from the command line
                segment = int(line_listed[0])
                size = int(line_listed[1])
                frame = int(line_listed[2])
                # call the PM initialization function to create the segment table
                command.PM_initialized(segment,size,frame)
                # Update the command line, removing the first three elements (already created segments)
                line_listed = line_listed[n:]
            # When all segments have been implemented, the next line can be processed, entried of the page tables (PT)
            line_one = False
        elif line_one == False:
            # Define page tables (PTs) for the segment specified within commands
            n = 3
            while line_listed:
                # Retrieve the segment, page, and frame from the command line
                segment = int(line_listed[0])
                page = int(line_listed[1])
                frame = int(line_listed[2])
                # call the page_table function to create the page for the particular segment/frame
                command.page_table(segment,page,frame)
                # Update the command line, removing the first three elements (already created pages)
                line_listed = line_listed[n:]
    time.sleep(2)
    print("Physical Memory (PM) has hereby been initialized.\n")

    # Translate the given virtual addresses (VAs) in input file, to physical addresses (PAs) written in output file
    time.sleep(1)
    print("Virtual addresses (VA's) being translated with input file 'input-no-dp.txt'...")
    while True:
        line = str(VA_commands.readline())
        if not line:
            break
        else:
            # Split line into a list of VA-addresses to be translated
            va_listed = line.split(" ")
            while va_listed:
                PA = command.va_to_pa(va_listed[0])
                va_listed.pop(0)
                output_file.write(str(PA) + " ")

    time.sleep(2)
    print("Output file named 'output-no-dp.txt' with translated virtual addresses (VA's) to physical addresses (PA's) has hereby been created!")
