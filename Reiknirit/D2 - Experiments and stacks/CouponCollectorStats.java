package D2_Experiments_Stacks;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

/** Coupon Collector Stats 
 * Runs the program 'couponCollectorTest' T times, with N set of cards to collect.
 * Also generated are calculations for the mean of the tests run, and the standard deviation of the tests run.
 * 
 * @author Benjamín Aage Birgisson
 * @version 1.0 August 28, 2019
 *
 */

public class CouponCollectorStats extends CouponCollector {
	public static void couponCollectorStats(int N, int T) {
		/**
		 * Run tests T times for N number of cards to collect.
		 * Gives the number of times it took to collect all cards (N), for each tests run (T).
		 * ALso calculates the mean and standard deviation of the total tests run.
		 */
		
		int count = 0;
		int[] results = new int[T];
		
		// Test(s) with N number of cards, T times
		while (count < T) {
			count++;
			StdOut.println("\nTest number " + count);
			int result = couponCollectorTest(N);
			StdOut.println("Total numbers generated in the process: " + result);
			results[count-1] = result;
		}
		
		// Calculation for the mean of tests
		int mean_total = 0;
		for (int i = 0; i < results.length; i++) {
			mean_total += results[i];
		}
		double mean = mean_total / T;
		StdOut.println("\nMean: " + mean);

		
		// Calculation for the standard deviation of tests
		double[] stdev_array = new double[T];
		for (int j = 0; j < results.length; j++) {
			double result_squared = (results[j] - mean);
			stdev_array[j] = Math.pow(result_squared, 2);
		}
		double stdev_sum = 0;
		for (int k = 0; k < stdev_array.length; k++) {
			stdev_sum += stdev_array[k];
		}
		double stdev = Math.sqrt(stdev_sum / stdev_array.length);
		StdOut.println("Standard deviation: " + stdev);
	}
			
		
	
	public static void main(String[] args) {
		/**
		 * Lets the user decide how many cards have to be collected (N), and how many times the test should be run (T).
		 * Afterwards, the class of 'couponCollectorStats' is run, with the given parameters of T and N.
		 */
		
		StdOut.print("How many cards in collection? ");
		int N = StdIn.readInt(); 
		
		StdOut.print("How many times to run experiment? ");
		int T = StdIn.readInt();
		
		couponCollectorStats(N, T);

	}


}
