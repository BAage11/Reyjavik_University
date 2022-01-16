/**********************************************************************
 *  Pattern Recognition readme.txt template
 **********************************************************************/

Name:  Benjamin Aage Birgisson
Login: benjamin18@ru.is
Hópur: N/A

Partner name:  N/A    
Partner login: N/A    
Partner hópur: N/A

Username of the student submitting to Mooshak: benjamin18@ru.is

Hours to complete assignment (optional):
Friday 08:30 - 11:30  &  12:15 - 16:00
Saturday 08:45 - 14:00
Sunday 09:00 - 13:00
Monday 12:00 - 18:00
Tuesday 15:00 - 20:00
Wednesday 12:00 - 17:00
Thursday 10:00 - 12:00  &  17:30 - 18:30
------------------------------------------
TOTAL :  35 hours (approximately)


/**********************************************************************
 *  Step 1.  Explain *briefly* how you implemented brute force.
 *           Describe how you implemented compareTo() and the
 *           slopeTo() methods in the Point data type.
 **********************************************************************/
brute force:
	- Get the input from user for the number of points (N) in array. Then create array with given (x,y) points given by user.
	- Using the compareTo() method, check if the y-coordinates are in descending order (from lowest to highest) in array.
	  This is done with a double for-loop, so every point in array is compared with every other point in array.
	  If y-coordinates are not in descending order (the method compareTo() sends back the integer value 1), swap places between the two points in array.
	- Then, for every four points in array (4 * for-loops), if they have the same slope between themselves ((p,q) && (q,r) and (q,r) && (r,s)) ,
	  print the sequence out. Else, continue to next points.
compareTo():
	- Followed guidance given in project description.
	  	- If y0-coordinate is less than y1-coordinates, or if they are equal and x0-coordinates is less than x1-coordinates,
	  	  return integer value -1. This means that the values are in a decreasing order.
	  	- If y0-coordinates are the same as y1-coordinates, and x0-coordinates are the same as x1-coordinates, 
	  	  then this is the same point in the array, and the integer value 0 is returned.
		- If none of the above fits the given points, return the integer value 1, meaning that the coordinates given are in an increasing order.
	  
slopeTo():
	- Guidance followed which where given in project description for return values.
		- Checked first if the point given (that.x, that.y) is equal to the invoking point (this.x, this.y).
		  If so, then this is the same point value and the return value given is negative infinity (goes from self to itself again).
		- Next checked if only the x-coordinates for the given point (that.x) is the same as the invoking point (this.x), but not the y-coordinates.
	 	  If that.x is equal to this.x, we have a vertical line and the return value given is positive infinity.
		- Last check made is only for the y-coordinates for the given point (that.y), to check if it is the same as the invoking point (this.y).
	  	  If that.y is equal to this.y, we have a horizontal line and the return value given is positive null (+0.0).
		- If none of the above is true, the following calculation is given for the slope between two points (a double value number):
			(this.y - that.y) / (this.x - that.x)


/**********************************************************************
 *  Step 2.  Explain *briefly* how you implemented the sorting solution.
 *           What steps did you do to avoid printing permutations
 *           and subsegments?
 **********************************************************************/
Brute.java:
I did so by using the compareTo() method, where two points are compared, giving the result of 1 if the points are in descending order.
If they are, the points would have to be swapped with each other (insertion sort), giving an ascending order of the two points.

Fast.java:
1) Make a counter for the number of points with the same slope between them.
2) For-loop over the array of points, making one point at a time as a base_point, which the array is then sorted by based on the given base point.
3) Get the slope of the two first points (base_point & base_point[i+1]), marking it as 'first_slope'.
4) Do a comparison of the slope between the base_point and the next point in array to check if it has the same slope as 'first_slope'.
   If so, increase the counter by one. If not, update the 'first_slope' calculation to be the slope between base_point and the next point in array.
5) Check before each comparison if the counter has reached 3 points, and if so, print out the sequence of points with the same slope between them.

* The code has the right points, with the same slope between them, but I have not been able to get them in the right order still. 



/**********************************************************************
 *  Empirical    Fill in the table below with actual running times in
 *  Analysis     seconds when reasonable (say 180 seconds or less).
 *               You can round to the nearest tenth of a second.
 *
 *  Estimate (using tilde notation) the running time (in seconds) of
 *  your two main functions as a function of the number of points N.
 *
 *  Explain how you derive any exponents.
 **********************************************************************/

      N       brute       sorting
 ---------------------------------
    150	      0,191	   0,048
    200	      0,573	   0,031
    300	      2,421	   0,082
    400	      7,507	   0,132
    800		*	   0,304
   1600		*	   0,691
   3200		*	   1,540
   6400		*	   4,504
  12800		*	  12,979

	* Time takes too long (program freezes)

Brute:    ~ 3N

Sorting:  ~ 3N




/**********************************************************************
 *  Theoretical   Give the order of growth of the worst-case running
 *                time of your programs as a function of N. Justify
 *                your answer briefly.
 **********************************************************************/

Brute: O(n^2)
On average, each insertion must traverse half the currently sorted array, while making a single comparison per step.
In the worst case, the array must be fully traversed. By algebra, this would be:  
1 + 2 + ..... + n - n * 0,5 = (n (n + 1) - n) / 2
Which is the same as:  O(n^2)

Sorting:  O(n log n)
Mergesort is O(log n) because the input is repeatedly halved.
And as the iteration of log(n) has to happen n times (for each item in the array), 
the time complexity as a whole will be:   O(n log n)


/**********************************************************************
 *  Known bugs / limitations. For example, if your program prints
 *  out different representations of the same line segment when there
 *  are 5 or more points on a line segment, indicate that here.
 **********************************************************************/
Have not been able to sort the points correctly in Fast.java, when printing out the points with the same slope between them.


/**********************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people (including course staff, lab TAs,
 *  classmates, and friends) and attribute them by name.
 **********************************************************************/
None.


/**********************************************************************
 *  Describe any serious problems you encountered.                    
 **********************************************************************/
Had difficulty figuring out how to sort the array by using the compareTo() method in Brute.java, as I knew that I had to compare every item of the array
with every other point in the array. The first thing I did was writing up the method on a piece of paper, trying to figure out what values to
enter into the compareTo() method - as my first try did not work (comparing points[i] to points[j]). 
After trying literally everything, I managed to figure out that I (of course) had to check every item with every item back and forth. 
So, an outer for-loop going through the whole array (one point at a time) and an inner for-loop going through every point in the array backwards (from last to first point) 
and comparing points[j] with points[j+1] was the solution! That is, using the sorting method of 'Insertion sort'!

Also had difficulty figuring out how to compare the slope between points in Fast.java, and to store the points to be able to print them out (if points where 4 or more).
Manage to implement this by making a variable called 'first_slope' where the slope between the base point and the next point in array, so that I could compare this slope
with other points in the array in regards to the given base point. Unfortunaly, I have not been able to get the sorting of the printed out points correct (in the right order).
I assume it is beacause I am using the original array of points, therefore mixing up the order for each iteration. But I have not been able to implement it in a satisfying way
either with a copy of the array, using the mix of these two arrays to get the right sorted output.


/**********************************************************************
 *  If you worked with a partner, assert below that you followed
 *  the protocol as described on the assignment page. Give one
 *  sentence explaining what each of you contributed.
 **********************************************************************/
No partner work was done.


/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 **********************************************************************/
I learned more about different sorting methods, for example the 'Insertion sort' method and the 'Merge sort' method.
