package S1_Percolation;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.Stopwatch;


/** A series of computational experiments.
 *  The function performs T independent computational experiments on an N-by-N grid.
 *  With the data given, calculations are made for the mean, the standard deviation, 
 *  and the 95% confidence interval for the percolation threshold. */
public class PercolationStats {
	
	private int T;
	private double[] results;
		
	/** Performing T independent experiments on an N-by-N grid. */
	public PercolationStats(int N, int T) {    
		if (T <= 0 || N <= 0) { 
			throw new java.lang.IllegalArgumentException("T and N must both be larger than 0."); }
		
		this.T = T;
		this.results = new double[T];
		
		for (int i = 0; i < T; i++) {
			Percolation percolation = new Percolation(N);
			while (!percolation.percolates()) {
				// StdOut.print("Row: ");
				int row = StdRandom.uniform(0, N);  // StdIn.readInt();
				
				// StdOut.print("Column: ");
				int col = StdRandom.uniform(0, N); // StdIn.readInt();
				
				// StdOut.println("Row: " + row + ", Column: " + col);
				percolation.open(row, col);	}
			
			int number = percolation.numberOfOpenSites();
			results[i] = number / Math.pow(N, 2); }		
		
		// StdOut.print("\nMean: ");
		// StdOut.println(mean());
		
		// StdOut.print("Standard deviation: ");
		// StdOut.println(stddev());
		
		// StdOut.print("Confidence Low: ");
		// StdOut.println(confidenceLow());
		
		// StdOut.print("Confidence High: ");
		// StdOut.println(confidenceHigh());
	}
		
	
	/** Sample mean of percolation threshold. */
	public double mean() { 
		return StdStats.mean(results); }
	
	
	/** Sample standard deviation of percolation threshold. */
	public double stddev() { 
		return StdStats.stddev(results); }
	
	
	/** Low endpoint of 95% confidence interval. */
	public double confidenceLow() { 
		// mean - ((1,96 * stdev) / sqrt(T)) according to assignment
		double low = StdStats.mean(results) - ((1.96 * StdStats.stddev(results)) / Math.sqrt(T));
		return low; }
	
	
	/** High endpoint of 95% confidence interval. */
	public double confidenceHigh() { 
		// mean + ((1,96 * stdev) / sqrt(T)) according to assignment
		double high = StdStats.mean(results) + ((1.96 * StdStats.stddev(results)) / Math.sqrt(T));
		return high; }

	
	
	public static void main(String[] args) {
		int N = StdRandom.uniform(1,100);
		int T = StdRandom.uniform(1,50);
		
		Stopwatch timer = new Stopwatch();
		PercolationStats test = new PercolationStats(N,T); 
		double time = timer.elapsedTime();
		StdOut.println("\nTimer: " + time); 
	}
}
