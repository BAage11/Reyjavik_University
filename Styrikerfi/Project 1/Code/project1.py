import sys

class Process():
    def __init__(self, process = 0, priority = 0, state = "ready", parent = None, children = [], resources = []):
        self.process = process
        self.priority = priority
        self.state = state
        self.parent = parent
        self.children = children
        self.resources = resources

class PCB():
    def __init__(self):
        self.capacity = 16
        self.array = [None] * self.capacity
        self.size = 0
        self.currently_running_process = None

##############################################################################################################

class Node_RCB():
    def __init__(self, resource, state = "free", waiting_list = []):
        self.resource = resource
        self.state = state
        self.waiting_list = waiting_list

class RCB():
    def __init__(self):
        self.resources = [Node_RCB(0), Node_RCB(1), Node_RCB(2), Node_RCB(3)]

##############################################################################################################

class RL():
    def __init__(self):
        self.list0 = []
        self.list1 = []
        self.list2 = []

    def add_to_RL(self, process, priority):
        if priority == 0:
            self.list0.append(process)
        elif priority == 1:
            self.list1.append(process)
        elif priority == 2:
            self.list2.append(process)

##############################################################################################################

class Manager():
    def __init__(self):
        """ Process and Resource Manager of the system. """
        self.control_block = PCB()
        self.ready_list = RL()
        self.resource_control_block = RCB()


    def init(self):
        """ Data structure initialized."""
        # Initialize the available processes in the system to None, and number of processes (size) equal to zero.
        self.control_block.array = [None] * self.control_block.capacity
        self.control_block.size = 0

        # Initialize the system, making process 0 as the running process
        self.control_block.array[0] = self.control_block.currently_running_process = Process(self.control_block.size, 0, "running")
        self.control_block.size += 1

        # Add the process to the appropriate ready list, according to priority
        self.ready_list.list0 = []
        self.ready_list.add_to_RL(self.control_block.currently_running_process, 0)

        # Clear ready lists 1 and ready list 2
        self.ready_list.list1 = []
        self.ready_list.list2 = []

        # Clear waiting lists of resources, and change state to 'free'
        for i in self.resource_control_block.resources:
            i.state = "free"
            i.waiting_list = []

        return self.control_block.currently_running_process.process


    def create(self, priority):
        """ Currently running process can create a new child using this function, thereby a new process is added to 'ready' state in the RL (ready list). If newly created process has highter priority than the currently running process, the new process becomes the currently running process, making the old process 'time-out'."""
        
        # If the capacity of the control block is full, return an error message
        if self.control_block.size == self.control_block.capacity:
            return -1
        # Check if resource priority requested is valid (0, 1 or 2)
        elif int(priority) < 0 or int(priority) > 3:
            return -1
        else:
            # Creation off initial values for new process
            priority = int(priority)
            state = "ready"
            parent = self.control_block.currently_running_process.process
            children = []
            resources = []

            # Create the new process within system, and add to array of processes
            count = 0
            for i in self.control_block.array:
                if i != None:
                    count += 1
                else:
                    self.control_block.array[count] = Process(count, priority, state, parent, children, resources)
                    self.control_block.size += 1
                    break

            # Insert new process into Ready List    
            self.ready_list.add_to_RL(self.control_block.array[count], priority)

            # Add new process as a child of the currently running process
            self.control_block.currently_running_process.children.append(count)

            # Call the scheduler() function, so that the currently highest priority processor, that is not blocked, is running within the system (creating a time-out for the old processor).
            return self.scheduler("create")


    def destroy(self, j):
        """ A processor can destroy its child processors, and/or itself. If the process destroys itself, the function recursively destroys all of its descendants to avoid orphan processes. """

        # Check if process being terminated is the currently running process
        if int(j) == self.control_block.currently_running_process.process:
            # Check if process has any children...
            if self.control_block.currently_running_process.children == []:                
                # If not, remove the process from the appropriate ready list
                if self.control_block.currently_running_process.priority == 2:
                    for i in self.ready_list.list2:
                        if i.process == int(j):
                            self.ready_list.list2.remove(i)
                elif self.control_block.currently_running_process.priority == 1:
                    for k in self.ready_list.list1:
                        if k.process == int(j):
                            self.ready_list.list1.remove(k)
                
                # Check if the process being terminated has any resources, and release them if so
                if self.control_block.currently_running_process.resources != []:
                    for i in self.control_block.currently_running_process.resources:
                        self.release(i)         

                # Free PCB[n] of j
                count = 0
                for i in self.control_block.array:
                    if i != self.control_block.array[0]:
                        count += 1
                    if i != None and i.process == int(j):
                        self.control_block.array[count] = None            

                # Allocate the parent of the process being terminated, to remove from the parent child-list
                parent = self.control_block.currently_running_process.parent
                # Find the parent within the system
                for p in self.control_block.array:
                    if p.process == parent:
                        # Find the process being terminated within the child list of parent
                        for c in p.children:
                            if c == int(j):
                                # Remove the process from the parent's child list
                                p.children.remove(c)
                        break

                # Find a new process to run within the system
                self.control_block.currently_running_process = None
                self.control_block.size -= 1
                return self.scheduler("destroy")

        	# If any children in the currently running process, destroy children
            while self.control_block.currently_running_process.children:
                # Find the child in the control block, to access all elements of the node
                for n in self.control_block.array:
                    if n != None and self.control_block.currently_running_process.children[0] == n.process:
                        destroy_child = n
                        break
                
                # Remove child from its appropriate ready list
                if destroy_child.priority == 2:
                    count = 0
                    for m in self.ready_list.list2:
                        if m != self.ready_list.list2[0]:
                            count += 1
                        if destroy_child.process == m.process:
                            self.ready_list.list2.pop(count)
                elif destroy_child.priority == 1:
                    count = 0
                    for k in self.ready_list.list1:
                        if k != self.ready_list.list1[0]:
                            count += 1
                        if destroy_child.process == k.process:
                            self.ready_list.list1.pop(count)

                # Remove any resources that the child is holding
                while destroy_child.resources != []:
                    for m in destroy_child.resources:
                        self.release_child_resource(destroy_child, m)
                
                # Remove from child-list
                self.control_block.currently_running_process.children.pop(0)

                # Free the PCB[n] spot of child process
                count = 0
                for i in self.control_block.array:
                    if i != self.control_block.array[0]:
                        count += 1
                    if i != None and i.process == destroy_child.process:
                        self.control_block.array.pop(count)  
                        self.control_block.array.append(None) 
                        self.control_block.size -= 1
                        break

            # After destroying all children in currently running process, the currently running process can be terminated as well, starting with removing the process from the appropriate ready list
            if self.control_block.currently_running_process.priority == 2:
                count = 0
                for i in self.ready_list.list2:
                    if i != self.ready_list.list2[0]:
                        count += 1
                    if i.process == int(j):
                        self.ready_list.list2.pop(count)
                        break
            elif self.control_block.currently_running_process == 1:
                count = 0
                for k in self.ready_list.list1:
                    if k != self.ready_list.list1[0]:
                        count += 1
                    if k.process == int(j):
                        self.ready_list.list1.pop(count)
                        break
                
            # Check if the process being terminated has any resources, and release them if so
            while self.control_block.currently_running_process.resources != []:
                for i in self.control_block.currently_running_process.resources:
                    self.release(i)         

            # Allocate the parent of the process being terminated, to remove from the parent child-list
            parent = self.control_block.currently_running_process.parent
            # Find the parent within the system
            for p in self.control_block.array:
                if p.process == parent:
                    # Find the process being terminated within the child list of parent
                    for c in p.children:
                        if c == int(j):
                            # Remove the process from the parent's child list
                            p.children.remove(c)
                    break

            # Free PCB[n] of j
            count = 0
            for i in self.control_block.array:
                if i != self.control_block.array[0]:
                    count += 1
                if i != None and i.process == int(j):
                    self.control_block.array.pop(count)  
                    self.control_block.array.append(None) 
                    self.control_block.size -= 1
                    break

            # Return the new currently running process within the system
            self.control_block.currently_running_process = None
            return self.scheduler("destroy")

        # Check if the process being terminated is a child of the currently running process
        for child in self.control_block.currently_running_process.children:
            if int(j) == child:
                # Find the process of child, with its variables
                for p in self.control_block.array:
                    if p.process == child:
                        destroy_process = p
                        break

                # If the child being deleted has any child(s) itself, destroy childs children
                while destroy_process.children:
                    # Find the child in the control block, to access all elements of the node
                    for n in self.control_block.array:
                        if n != None and destroy_process.children[0] == n.process:
                            destroy_child = n
                            break
                    
                    # Remove child from its appropriate ready list
                    if destroy_child.priority == 2:
                        count = 0
                        for m in self.ready_list.list2:
                            if m != self.ready_list.list2[0]:
                                count += 1
                            if destroy_child.process == m.process:
                                self.ready_list.list2.pop(count)
                    elif destroy_child.priority == 1:
                        count = 0
                        for k in self.ready_list.list1:
                            if k != self.ready_list.list1[0]:
                                count += 1
                            if destroy_child.process == k.process:
                                self.ready_list.list1.pop(count)

                    # Remove any resources that the child is holding
                    while destroy_child.resources != []:
                        for m in destroy_child.resources:
                            self.release_child_resource(destroy_child, m)
                    
                    # Remove from child-list
                    destroy_process.children.pop(0)

                    # Free the PCB[n] spot of child process
                    count = 0
                    for i in self.control_block.array:
                        if i != self.control_block.array[0]:
                            count += 1
                        if i != None and i.process == destroy_child.process:
                            self.control_block.array.pop(count)  
                            self.control_block.array.append(None) 
                            self.control_block.size -= 1
                            break

                # Remove child from its appropriate ready list
                if destroy_process.priority == 2:
                    for j in self.ready_list.list2:
                        if destroy_process.process == j.process:
                            self.ready_list.list2.remove(j)
                elif destroy_process.priority == 1:
                    for k in self.ready_list.list1:
                        if destroy_process.process == k.process:
                            self.ready_list.list1.remove(k)                 
                            break

                # Remove any resources that the child is holding
                while destroy_process.resources != []:
                    for m in destroy_process.resources:
                        self.release_child_resource(destroy_process, m)

                # Remove the child from its parents list of children
                parent = destroy_process.parent
                # Find the parent within system
                for i in self.control_block.array:
                    if i != None and i.process == parent:
                        # Locate the child beint terminated in the child-list of parent
                        for j in i.children:
                            if j == destroy_process.process:
                                # Remove the child from the child-list of parent
                                i.children.remove(destroy_process.process)
                                break                    

                # Free the PCB[n] spot of child process
                count = 0
                for n in self.control_block.array:
                    if self.control_block.array[0] != n:
                        count += 1
                    if destroy_process.process == n.process:
                        self.control_block.array.pop(count)  
                        self.control_block.array.append(None) 
                        self.control_block.size -= 1
                        break

                # Return the parent of the child being terminated, as it is still the running process
                return self.control_block.currently_running_process.process
        
        # Process being terminated is not the currently running process, or a child of the currently running process, therefore causing an error
        return -1


    def release_child_resource(self, dest_proc, child_resource):
        """ A child process of the currently running process has been terminated, thereby releasing all its resources. By doing so, a check must be made to see if there is any processor on the waiting list of the newly available resource, and if so, allocate the resource to that processor (perhaps making it the running process within the system by doing so). """

        # Find the resource
        for i in self.resource_control_block.resources:
            if i.resource == int(child_resource):
                for j in self.control_block.array:
                    # Find process being currently terminated
                    if j != None and j.process == dest_proc.process:
                        # Remove the resource from the processor being terminated
                        dest_proc.resources.remove(child_resource)
                        # Remove the processor being terminated from the waiting list of the resource
                        i.waiting_list.remove(dest_proc.process)
                     
                        # If the waiting list thereby becomes empty, the resource state becomes 'free'
                        if i.waiting_list == []:
                            i.state = "free"
                            break
                        #... else, another process must be allocated the resource, thereby unblocking the process
                        else:
                            if i.waiting_list[0] == self.control_block.currently_running_process.process:
                                i.state = "allocated"
                                break
                            else:
                                res_new_proc = i.waiting_list[0]
                                for j in self.control_block.array:
                                    if j != None and j.process == res_new_proc and j.state == "blocked":
                                        j.state = "ready"
                                        # As the processor is currently no longer blocked, it can be put back on the appropriate ready list
                                        self.ready_list.add_to_RL(j, j.priority)
                                        break


    def request(self, resource):
        """ A process may requests and/or acquire about a resource. If the resource is currently unavailable, the requesting process becomes 'blocked'. """

        # if processor 0 requests a resource, it is prevented to do so, preventing deadlocks where no process is on the RL (ready list)
        if self.control_block.currently_running_process == self.control_block.array[0]:
            return -1

        # Check if resource requested is valid
        if int(resource) < 0 or int(resource) > 4:
            return -1

        # Check if the resource requested by the processor is already being held by it
        for proc_res in self.control_block.currently_running_process.resources:
            if proc_res == int(resource):
                return -1

        # Check if the resource requested is already 'allocated' - if so, processor becomes blocked on the waiting list of the requested resource, else assign resource to processor and mark resource as 'allocated'
        for res_block in self.resource_control_block.resources:
            if res_block.resource == int(resource):
                if res_block.state == "allocated":
                    # Put requesting processor on waiting list for resource... 
                    res_block.waiting_list.append(self.control_block.currently_running_process.process)
                    # ... , put resource in the resource list of processor
                    self.control_block.currently_running_process.resources.append(int(resource))
                    # ... and mark the state of the processor as 'blocked'
                    self.control_block.currently_running_process.state = "blocked"
                    # Find the next processor in line to become the running processor of the system
                    return self.scheduler("blocked")
                elif res_block.state == "free":
                    # If resource is free, mark the resource as 'allocated'...
                    res_block.state = "allocated"
                    # Put as the first item on the waiting list, as it is the running processor currently holding the resource
                    res_block.waiting_list.insert(0, self.control_block.currently_running_process.process)
                    # ... and put resource in the resource list of processor
                    self.control_block.currently_running_process.resources.append(int(resource))
                    return self.control_block.currently_running_process.process


    def release(self, resource):
        """ A processor, holding a resource, releases it and thereby makes the next processor in line (on the waiting list) change status from 'blocked' to 'ready', with the allocated resource in question. If no other process is on waiting list, the resource becomes 'free'. """

        # If the resource being released is not integer between 0 and 3, an error has occured
        if int(resource) < 0 or int(resource) > 4:
            return -1

        # Check if the resource being released is currently 'allocated'
        for res in self.resource_control_block.resources:
            if res.resource == int(resource):
                # If the resource state being released is already 'free', an error has occured
                if res.state != 'allocated':
                    return -1
                else:
                    # Check if the currently running processor is holding the resource being released...
                    for i in self.control_block.currently_running_process.resources:
                        if i == int(resource):
                            # If so, the resource can be removed from the processor resource list
                            self.control_block.currently_running_process.resources.remove(int(resource))
                            # ... and remove the terminated process from the waiting list of resource
                            res.waiting_list.remove(self.control_block.currently_running_process.process)
                            #... and if the resource waiting list is empty, the resource becomes 'free'
                            if res.waiting_list == []:
                                res.state = "free"
                                return self.control_block.currently_running_process.process
                            else:
                                #... else it must be re-allocated to the next process in the waiting list of the resource
                                res.state = "ready"
                                return self.scheduler("release")
        # Currently running process does not hold the resource being released, thereby causing an error
        return -1


    def timeout(self):
        """ Evoks time-sharing, changing the status of the currently running processor from 'running' to 'ready' (moving the processor to the end of the appropriate ready list), and next processor in line will become the new running processor of the system. """
        
        # Change status of the currently running processor from 'running' to 'ready'
        self.control_block.currently_running_process.state = "ready"

        # Move process i from head of RL (ready list) to end of RL
        if self.control_block.currently_running_process.priority == 1:
            timed_out_proc = self.ready_list.list1.pop(0)
            self.ready_list.list1.append(timed_out_proc)
        elif self.control_block.currently_running_process.priority == 2:
            timed_out_proc = self.ready_list.list2.pop(0)
            self.ready_list.list2.append(timed_out_proc)

        # New process now at the head of the 'ready list' becomes the running process
        return self.scheduler("timeout")


    def scheduler(self, func):
        """ The scheduler() performs contexts switch from the currently running process to a new process, and displays what process is currently running within the system. A context switch occurs when the currently running process becomes 'blocked', or a timeout occurs which results in the currently running process is added to the back of the ready list, and could occur if a priority process is created/destroyed. """
        
        # The scheduler() function is being called by the create() function, as a new process has been added to the system. By doing so, the system needs to check if the newly added processor has a higher priority than the currently running process within the system.
        if func == "create":
            # If currently running processor has priority equal to 0...
            if self.control_block.currently_running_process.priority == 0:
                # ... and ready list with priority 2 is not empty...
                if self.ready_list.list2 != [] or self.ready_list.list1 != []:
                    for i in self.ready_list.list2:
                        # ... change running process, to process with higher priority (if process state is 'ready')
                        if i.state == "ready":
                            old_running_process = self.control_block.currently_running_process
                            old_running_process.state = "ready"
                            self.control_block.currently_running_process = i
                            self.control_block.currently_running_process.state = "running"
                            if i != self.ready_list.list2[0]:
                                change_to_first = self.ready_list.list2.pop(i.process)
                                self.ready_list.list2.insert(0, change_to_first)
                            break
                    for j in self.ready_list.list1:
                        # ... change running process, to process with higher priority (if process state is 'ready')
                        if j.state == "ready":
                            old_running_process = self.control_block.currently_running_process
                            old_running_process.state = "ready"
                            self.control_block.currently_running_process = j
                            self.control_block.currently_running_process.state = "running"
                            if j != self.ready_list.list1[0]:
                                for i in self.ready_list.list2:
                                    if i == j.process:
                                        change_to_first = self.ready_list.list1.pop(j.processI)
                                        self.ready_list.list1.insert(0, change_to_first)
                            break
           # Or if currently running process has priority equal to 1...
            elif self.control_block.currently_running_process.priority == 1:
                # ... and ready list with priority 2 is not empty...
                if self.ready_list.list2 != []:
                    for k in self.ready_list.list2:
                        # ... change running process, to process with higher priority (if process state is 'ready')
                        if k.state == "ready":
                            old_running_process = self.control_block.currently_running_process
                            old_running_process.state = "ready"
                            self.control_block.currently_running_process = k
                            self.control_block.currently_running_process.state = "running"
                            if k != self.ready_list.list2[0]:
                                for i in self.ready_list.list2:
                                    if i == k.process:
                                        change_to_first = self.ready_list.list2.pop(i)
                                        self.ready_list.list2.insert(0, change_to_first)
                            break
            return self.control_block.currently_running_process.process

        # The scheduler() function has been called by the destroy() function, as a processor has been terminated within the system, so there needs to be checked if the terminated process was the currently running process in the system.
        elif func == "destroy":
            # If the destroyed processor was the currently running processor within the system...
            if self.control_block.currently_running_process == None:
                if self.ready_list.list2 != [] or self.ready_list.list1 != []:
                    # If process within ready list with priority 2 state is 'ready', make it the running process...
                    for item in self.ready_list.list2:
                        if item.state == "ready":
                            self.control_block.currently_running_process = item
                            self.control_block.currently_running_process.state = "running"
                            # ... and change its placeholder within the ready list to the first element within the list
                            if item != self.ready_list.list2[0]:
                                change_to_first = self.ready_list.list2.pop(item.process)
                                self.ready_list.list2.insert(0, change_to_first) 
                            return self.control_block.currently_running_process.process
                    # And if ready list 2 is empty (or no processor has the state 'ready'), and ready list 1 has processors, look up a processor with priority 1 to run within the system
                    for item in self.ready_list.list1:
                        if item.state == "ready":
                            self.control_block.currently_running_process = item
                            self.control_block.currently_running_process.state = "running"
                            # ... and change its placeholder within the ready list to the first element within the list
                            if item != self.ready_list.list1[0]:
                                change_to_first = self.ready_list.list1.pop(item.process)
                                self.ready_list.list1.insert(0, change_to_first) 
                            return self.control_block.currently_running_process.process
                else:
                    # Else, the processor running within the system becomes the processor originally created when the system was 'turned on' : Processor 0 with Priority 0
                    self.control_block.currently_running_process = self.ready_list.list0[0]
                    return self.control_block.currently_running_process.process

        # A processor within the system has released a resource it had allocated, making the resource 'free'. By doing so, another process is allocated the resource (if the waiting list of the resource is none empty) and may thereby become available to run (has higher priority than the currently running process)
        elif func == "release":
            # Check if a resource state is 'free' and if it has any processor on waiting list
            for res in self.resource_control_block.resources:
                # If a resource is found, it can be re-allocated a new process
                if res.state == "ready" and res.waiting_list != []:
                    # Assign the resource to the new processor
                    res.state = "allocated"
                    the_proc = res.waiting_list[0]
                    
                    # Find the new processor within the system, change its state
                    for proc in self.control_block.array:
                        if proc != None and proc.process == the_proc:
                            # Change state of processor from 'blocked' to 'ready'
                            proc.state = "ready"
                            
                            # Append to the appropriate ready list
                            if proc.priority == 2:
                                self.ready_list.list2.append(proc)
                            elif proc.priority == 1:
                                self.ready_list.list1.append(proc)

                            # Check if the currently running processor has priority lower than this one
                            if self.control_block.currently_running_process.priority == 1:
                                # And if so, make it the current running processor in the system
                                if proc.priority == 2:
                                    old_process = self.control_block.currently_running_process
                                    old_process.state = "ready"
                                    proc.state = "running"
                                    self.control_block.currently_running_process = proc
                        
            return self.control_block.currently_running_process.process
                                    
            
        # The user of the system has requested a time-out for the currently running processor, changing its state from 'running' to 'ready', thereby making the next available processor the currently running processor within the system
        elif func == "timeout":
            # If any processors on ready list with priority 2, check if state is 'ready' and if so, change to running processor            
            if self.ready_list.list2 != [] or self.ready_list.list1 != []:
                for i in self.ready_list.list2:
                    if i.state == "ready":
                        # Change the current running process
                        self.control_block.currently_running_process = i
                        i.state = "running"
                        return self.control_block.currently_running_process.process
                for j in self.ready_list.list1:
                    if j.state == "ready":
                        # Change the running process
                        self.control_block.currently_running_process = j
                        j.state = "running"
                        return self.control_block.currently_running_process.process
            # Else return the processor currently running within system, as there is no other processor to take over
            return self.control_block.currently_running_process.process
        
        # The currently running process of the system has become 'blocked' as the resource it requested is already allocated by another process. Therefore, a new running process must be found within the system.
        elif func == "blocked":
            # Remove old running process from the appropriate ready list
            old_running_process_priority = self.control_block.currently_running_process.priority
            if old_running_process_priority == 2:
                self.ready_list.list2.pop(0)
            elif old_running_process_priority == 1:
                self.ready_list.list1.pop(0)

            # Find a new processor to run within the system, according to its priority level
            if self.ready_list.list2 != [] or self.ready_list.list1 != []:
                for i in self.ready_list.list2:
                    if i.state == "ready":
                        # Change the running processor
                        self.control_block.currently_running_process = i
                        i.state = "running"
                        return self.control_block.currently_running_process.process
                for j in self.ready_list.list1:
                    if j.state == "ready":
                        # Change the running processor
                        self.control_block.currently_running_process = j
                        j.state = "running"
                        return self.control_block.currently_running_process.process
            else:
                self.control_block.currently_running_process = self.control_block.array[0]
                self.control_block.currently_running_process.state = "running"
                return self.control_block.currently_running_process.process

##############################################################################################################
##############################################################################################################

# Example C (replace the following for the first line in 'Example A/B'):
#     with open(sys.argv[1], 'r') as input_file, open(sys.argv[2], 'w') as output_file:

# Example A/B:
with open("input.txt", 'r') as input_file, open("output.txt", 'w') as output_file:
    command = Manager()
    while True:
        line = input_file.readline()
        if not line:
            break
        else:
            if line[0:2] == "cr":
                message = command.create(line[3])
                output_file.write(str(message) + " ")
            elif line[0:2] == "de":
                message = command.destroy(line[3])
                output_file.write(str(message) + " ")
            elif line[0:2] == "rq":
                message = command.request(line[3])
                output_file.write(str(message) + " ")
            elif line[0:2] == "rl":
                message = command.release(line[3])
                output_file.write(str(message) + " ")
            elif line[0:2] == "to":
                message = command.timeout()
                output_file.write(str(message) + " ")
            elif line[0:2] == "in":
                message = command.init()
                output_file.write(str(message) + " ")
            else:
                output_file.write(line)

##############################################################################################################
# To run the program manually, typing command within the terminal:

"""
def main():
    command = Manager()
    choice = None
    while choice != " ":
        choice = input("> ").lower()
        try:
            if choice[0:2] == "cr": 
                message = command.create(choice[3])
                print(str(message))
            elif choice[0:2] == "de": 
                message = command.destroy(choice[3])
                print(str(message))
            elif choice[0:2] == "rq":
                message = command.request(choice[3])
                print(str(message))
            elif choice[0:2] == "rl":
                message = command.release(choice[3])
                print(str(message))
            elif choice == "to":      
                message = command.timeout()
                print(str(message))
            elif choice == "in":      
                message = command.init()
                print(str(message))
            elif choice == "" or choice == " ":
                break
        except:
            print(str(-1))
            
main()
"""