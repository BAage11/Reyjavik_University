package D1_Binary_Search_Experiments;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class H_Longest_Run {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// Make array in accordance to user preferences
		int n = StdIn.readInt();
		int[] a = new int[n];
		
		for (int i=0; i < n; i++) {
			a[i] = StdIn.readInt();
		}
		
		// Find the maximum sequence of increasing numbers in array
		int count = 1;
		int max = 0;
		for (int j=1; j < n; j++) {
			if (a[j] >= a[j-1]) count++; 

			else if (a[j] < a[j-1]) { 
				if (count > max) {
						max = count;
						count = 1;
				}
			}
		}
		
		// Output - Biggest sequence of increasing numbers in array
		StdOut.println(max);
		
	}

}
