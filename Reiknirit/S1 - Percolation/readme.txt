/******************************************************************************
 *  Name: Benjamín Aage Birgisson
 *  Kt:	020883-5539
 *  Hópur: N/A
 *
 *  Partner Name:    N/A
 *  Partner Kt:      N/A
 *  Partner Hópur: N/A
 * 
 *  Operating system:  Windows 10
 *  Compiler:  Java
 *  Text editor / IDE:  Eclipse
 *
 *  Have you taken (part of) this course before: No
 *
 *  Hours to complete assignment (optional):  
 *  Thursday (6pm-7pm), Saturday (10am-7pm), Sunday (10am-3pm), Tuesday (09am-15pm), 
 *  Wednesday (08:30am-10am  &  14pm-17pm), Thursday (10am-11:30am  &  18pm-19pm), Friday (12:30pm-15:00pm)
 *  TOTAL :  30 hours (approximately)
 *
 ******************************************************************************/


/******************************************************************************
 *  Describe how you implemented Percolation.java. How did you check
 *  whether the system percolates?
 *****************************************************************************/
1. Get an input for the size of grid (NxN) from user.
2. Check if the input from user was larger than zero. If so, continue with program. 
   Else, give user a message that the input is invalid.
3. Create grid with NxN sites with values ranging from 0 to N-1 (with N being the input given from the user). 
   Also, created another grid for the same size where values stored are either 'true' or 'false, depending if the site is open or not. All sites initially put as 'false'.
4. Created an index number to identify sites located on the top row of grid, as well as an index for the sites located on the bottom row of the grid.
   This was though of as a check to see if the grid is percolating, or not. 
   That is, if there is a connection between the top row and the bottom row, the grid is percolating.
5. Sites created (p,q) at random to open in the grid, and then check if the site just opened has any possible connections to other sites around.
   This was done to keep a record on which sites in the grid where connected, and to check to see if the grid is percolating or not (top and bottom row connected).
   If site has already been opened, the program continues without interference.
6. By checking to see if grids where connected or not, it is be possible to check if the bottom row of the grid is connected to the top row of the grid.
   If so, then the grid is percolating.
7. Finally, a method was created to count how many sites where opened in the total amount of sites in the grid.

Check whether the system perculates is described in step number 5-6 here above.


/******************************************************************************
 *  Using Percolation with QuickFindUF.java,  fill in the table below such that 
 *  the N values are multiples of each other.

 *  Give a formula (using tilde notation) for the running time (in seconds) of 
 *  PercolationStats.java as a function of both N and T. Be sure to give both 
 *  the coefficient and exponent of the leading term. Your coefficients should 
 *  be based on empirical data and rounded to two significant digits, such as 
 *  5.3*10^-8 * N^5.0 T^1.5.
 *****************************************************************************/

(keep T constant)	-->	T = 100

 N          time (seconds)
------------------------------
50		0,020
100		0,622
200		6,773
400		3,195
800		1,157



(keep N constant)	-->	N = 100

 T          time (seconds)
------------------------------
50		0,460
100		0,060
200		0,168
400		1,353
800		0,270


running time as a function of N and T:  
	     T = a * N^3
	=>   1,157 = a (800)^2
	=>   a = 1,157 / 800^2
	=>   a = 1,81 * 10^-6
	
	=>   ~ 1,81 * 10^-6 * N^2
	=>   N^2

/******************************************************************************
 *  Repeat the previous question, but use WeightedQuickUnionUF.java.
 *****************************************************************************/

(keep T constant)	-->	T = 100

 N          time (seconds)
------------------------------
50		0,466
100		0,682
200		2,448
400		11,487
800		37,117


(keep N constant)	-->	N = 100

 T          time (seconds)
------------------------------
50		0,142
100		0,543
200		1,316
400		2,956
800		3,704


running time as a function of N and T:  
	T = a * N^3
	=>   37,117 = a (800)^2
	=>   a = 37,117 / 800^2
	=>   a = 5,80 * 10^-5
	
	=>   ~ 5,80 * 10^-5 * N^2 
	=>   N^2


/**********************************************************************
 *  How much memory (in bytes) does a Percolation object use to store
 *  an N-by-N grid? Use the 64-bit memory cost model from Section 1.4
 *  of the textbook and use tilde notation to simplify your answer.
 *  Briefly justify your answers.
 *
 *  Include the memory for all referenced objects (deep memory).
 **********************************************************************/
Percolation object - Memory:
	Object overhead = 16 bytes
	Reference = ~ 4mn
	Padding = 8 bytes

So, if N=2 the memory (in bytes) would be to store an N-by-N grid is:
	16 + (4 x 2 x 2) + 8 = 16 + 16 + 8 = 40 bytes


Array access is n, and as we have a two dimensional array here, the array access would be n^2 (or n times n).
So the tilde notation would therefore be:   
					~2n array access


/******************************************************************************
 *  After reading the course collaboration policy, answer the
 *  following short quiz. This counts for a portion of your grade.
 *  Write down the answers in the space below.
 *****************************************************************************/
1. (c) You can help a student by discussing ideas, selecting data
    structures, and debugging their code.
2. (c) You and your partner must both be present while writing code,
    during the analysis, and while submitting the code and the
    readme. Failure to do so is a violation of the course
    collaboration policy.


1. How much help can you give a fellow student taking REIR
(a) None. Only the TAs can help.
(b) You can discuss ideas and concepts but students can get help
    debugging their code only from a TA, or
    student who has already passed REIR.
(c) You can help a student by discussing ideas, selecting data
    structures, and debugging their code.
(d) You can help a student by emailing him/her your code.

2. What are the rules when partnering?
 (a) You and your partner must both be present while writing code.
     But after that only one person needs to do the analysis.
 (b) You and your partner must both be present while writing code
     and during the analysis, but, after that, only one person
     needs to be present while submitting the code and the
     readme.
 (c) You and your partner must both be present while writing code,
     during the analysis, and while submitting the code and the
     readme. Failure to do so is a violation of the course
     collaboration policy.
 
/******************************************************************************
 *  Known bugs / limitations.
 *****************************************************************************/
Did (most likely) not cover the coding for preventing possible 'backwash' - at least did not verify it thoroughly enough.
Was not sure about the meaning of 1D and 2D coordinates, described in the 'Checklist' document for the project - so may be a possible bug.


/******************************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and classes, but do
 *  include any help from people (including course staff, lab TAs,
 *  classmates, and friends) and attribute them by name.
 *****************************************************************************/
Got help from a TA (Tómas Hrafn Jóhannesson) on Piazza explaining how you can use the constructor to access global variables, without calling the method with the variable itself.
He recommended reading the following in this regards:  https://www.javacoffeebreak.com/faq/faq0002.html

Got help from TA in 'dæmatími' to implement the file 'InteractivePercolationVisualizer'.


/******************************************************************************
 *  Describe any serious problems you encountered.                    
 *****************************************************************************/
My biggest problem was debugging everything, which was very time consuming, to find different problems.
For example error checks that was put into the code (that N and (p,q) where within particular parameters, that symbols like "<" and ">" 
where put the right way (at the right times in the code), that using row+1/row-1 and (or) col+1/col-1 in the right places etc.)

Also, to implement the connection between the top_row of the grid with the bottom_row of the grid and 
check if there where any connections between them two was highly complicated to implement 
(ended up being a bug in the main method, instead of the percolate method).



/******************************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 *****************************************************************************/
I enjoyed many parts of the assignment, but would have liked to see some simple code implemented in classroom for 
QuickFindUF and WeightedQuickUnionUF just to get a bit of a feel on how to implement these things when checking for percolation in a grid.

