package D1_Binary_Search_Experiments;

import java.util.Arrays;
import edu.princeton.cs.algs4.BinarySearch;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.Stopwatch;

public class BLTester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// Create array with random numbers
		int n = 320000;
		int[] a = new int[n];
		for (int i=0; i < n; i++) {
			a[i] = StdRandom.uniform(100000);
		}
		
		// Compatible array created to find random numbers
		int[] f = new int[n];
		for (int j=0; j < n; j++) {
			f[j] = StdRandom.uniform(100000);
		}
		
		// Original array sorted by values
		Arrays.sort(a);
				
		// Linear search
		Stopwatch stopwatch1 = new Stopwatch();
		int count1 = 0;
		for (int k=0; k < f.length; k++) 
			for (int c=0; c < a.length; c++) {
				if (f[k] == a[c]) count1++;
		}
		
		// Output - Linear
		StdOut.println("Count for linear search: "+count1);
		StdOut.println("Linear search time: "+stopwatch1.elapsedTime());
		StdOut.println();

		
		// Binary search
		Stopwatch stopwatch2 = new Stopwatch();
		int count2 = 0;
		for (int l=0; l < n; l++) {
			if (BinarySearch.indexOf(a, f[l]) != -1)
				count2++;
		}

		// Output - Binary
		StdOut.println("Count for binary search: "+count2);
		StdOut.println("Binary search time: "+stopwatch2.elapsedTime());
	}

}
