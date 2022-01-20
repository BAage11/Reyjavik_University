import time

class VM_Manager():
    def __init__(self):
        """ Initialization of the physical memory (PM). """
        # Physical memory divided into 1024 frames of 512 words each (page) == 524,288 integers
        self.size = 524288
        self.PM = [None] * self.size

        # Initialize the paging disk (number of blocks = 1024, block size = 512)
        self.D = [None] * self.size

        # Keep track of free frames
        self.free_frames = list(range(0, 1023))


    def PM_initialized(self, segment, size, frame):
        """ Physical memory (PM) initialized with given commands, definition of segment table (ST) - A segment which resides in a frame, as well as the size of the segment. """
        # Get the index into the physical memory list
        index = segment * 2
        # Size of the segment (number of words)
        self.PM[index] = size
        # Frame number holding the page table of segment
        self.PM[index+1] = frame

        # Update free frames list, if allocated to physical memory (PM)
        if frame >= 0:
            self.free_frames.remove(frame)


    def page_table(self, segment, page, frame):
        """ With the given segment (s), the specific frame (p) is located, which then again can locate the correct page table, to insert the entry (value) of that page table. """
        # Calculate the given segment for the frame
        index = segment * 2
        # Find the frame for the segment
        PM_frame = self.PM[index+1]

        if PM_frame == None:
            quit
        else:
            # Check if page table should be stored on disk block (negative), or in physical memory (positive)
            if PM_frame >= 0:
                # Input the page for the frame into the right place in the page table (512 words == frame size)
                self.PM[PM_frame * 512 + page] = frame
                # Updated the list of free frames (if on physical memory)
                if frame > 0:
                    self.free_frames.remove(frame)
                else:
                    # ... else, initalize the frame on disk block
                    self.D[abs(frame) * 512 + page] = 0
            else:
                # Input the page for the frame into disk block
                self.D[abs(PM_frame) * 512 + page] = frame

                # If frame is positive, the free frame list must be updated
                if frame >= 0:
                    self.free_frames.remove(frame)


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

        # Update free frames list
        if p >= 0:
            for i in self.free_frames:
                if i == p:
                    self.free_frames.remove(p)

        # If page table is not resident...
        if self.PM[2*s + 1] < 0:
            # Store 'old' page table number
            old = self.PM[2*s + 1]
            # Allocate a free frame using list of free frames
            try:
                free_frame = self.free_frames.pop(0)
            except:
                return -1
            
            # Update segment table entry
            self.PM[2*s + 1] = free_frame
            # Read disk block b into PM (page table reference), with old offset absolute (non-negative) value
            for i in range(0,511):
                self.PM[self.PM[2*s + 1] * 512 + i] = self.D[abs(old) * 512 + i]

        # Or/And, if page is not resident within existing page table in physical memory...
        if self.PM[self.PM[2*s + 1] * 512 + p] < 0:
            # Allocate free frame using list of free frames
            try:
                free_frame2 = self.free_frames.pop(0)  
            except:
                return -1
            
            # Update segment table entry
            self.PM[self.PM[2*s + 1] * 512 + p] = free_frame2

        # Return the physical address
        return self.PM[self.PM[2*s + 1] * 512 + p] * 512 + w


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


with open("init-dp.txt", 'r') as initialize_PM, open("input-dp.txt", 'r') as VA_commands, open("output-dp.txt", 'w') as output_file:
    command = VM_Manager()
    print("\nPhysical memory (PM) being created with input file 'init-dp.txt'...")
    
    # Start by initializing the physical memory, creating the segment table and the page tables
    line_one = True
    while True:
        line = str(initialize_PM.readline())
        line_listed = line.split(" ")

        if line_listed[-1] == "\n":
            line_listed.remove("\n")
        
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
    print("Virtual addresses (VA's) being translated with input file 'input-dp.txt'...")
    time.sleep(1)
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
    print("Output file named 'output-dp.txt' with translated virtual addresses (VA's) to physical addresses (PA's) has hereby been created!")
