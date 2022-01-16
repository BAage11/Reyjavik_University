package S1_Percolation;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;
// import edu.princeton.cs.algs4.QuickUnionUF;


/** Create an NxN grid, where every site is blocked in the beginning. 
 *  Then, one site at a time, open the site/cell picked and 
 *  check if the grid percolates (any cell in top row is connected 
 *  to any cell in the bottom row of the grid). */
public class Percolation 
{
	private int N;
	private int top_row;
	private int bottom_row;
	private int[][] Grid;
	private boolean[][] CheckOpenGrid;
	private WeightedQuickUnionUF weightedQuickUnionUF;
	// private QuickUnionUF quickUnionUF;
	
	
	/** Create a grid with dimensions being N-by-N, and all sites of the grid being initially blocked. */
	public Percolation(int N) { 
    	checkInput(N);
    		
    	this.N = N;											// Set the input (N) to the private value N in constructor
    	top_row = N * N;									// Top row indexed as unique number
    	bottom_row = N * N + 1;								// Bottom row indexed as unique number
    	Grid = new int[N][N];								// All values initiated to 0
    	CheckOpenGrid = new boolean[N][N];					// All values initiated to 'false', all sites are blocked
    	weightedQuickUnionUF = new WeightedQuickUnionUF(N * N+2);		// Create a new instance of WQU-UF
    	
    	int counter = 0;
    	for (int row = 0; row < N; row++) {					// Changing values of Grid from 0 to N-1
    		for (int col = 0; col < N; col++) {
    			Grid[row][col] = counter;	
    			counter++; }    	
    	}
	}
	
	private void checkInput(int N) {
		if (N <= 0) {
    		throw new java.lang.IllegalArgumentException("The number of sites in grid must be larger than 0.");	}
		}
	
	
	/** Check if row and column index is within given grid. */
	private void checkIndex(int row, int col) {
		if (row < 0 || row >= N) {
			throw new java.lang.IndexOutOfBoundsException("Row value must be higher or equal to 0 and lower than N."); } 
		
		if (col < 0 || col >= N) {
			throw new IndexOutOfBoundsException("Column value must be higher or equal to 0 and lower than N."); } 
	}
		
	
	/** Open the site (row, column) if it is not open already.
	 *  Then check if the site opened can be connected with any other site around it. */
    public void open(int row, int col) { 
    	checkIndex(row, col);					// Check to see if the index given is within given grid.
    	
    	if (!isOpen(row, col)) {
    		CheckOpenGrid[row][col] = true;
       		int index = Grid[row][col];
       		
       		if (row == 0) 			// If index of row is equal to 1, then it is part of top row in grid
       		{ weightedQuickUnionUF.union(index, top_row); }
       		
       		if (row == N-1) 		// If index of row is equal to N-1, then it is part of bottom row in grid
       		{ weightedQuickUnionUF.union(index, bottom_row); }
       		
       		if (row-1 >= 0 && isOpen(row-1, col))		// Check if row-1 is open, then union row&column to row-1&column
       		{ weightedQuickUnionUF.union(index, Grid[row-1][col]); }
       		
       		if (row+1 < N && isOpen(row+1, col))		// Check if row+1 is open, iff then union row&column to row+1&column
       		{ weightedQuickUnionUF.union(index, Grid[row+1][col]); }
       		
       		if (col-1 >= 0 && isOpen(row, col-1))		// Check if column-1 is open, then union row&column to row&column-1
       		{ weightedQuickUnionUF.union(index, Grid[row][col-1]); }

       		if (col+1 < N && isOpen(row, col+1))		// Check if column+1 is open, iff then union row&column to row&column+1
       		{ weightedQuickUnionUF.union(index, Grid[row][col+1]); }
       	}
    	else return;
    }
    
    
    /** Is the site (row, column) open? 
     *  Returns the value in grid, either 'false' or 'true'. */
    public boolean isOpen(int row, int col) {     	
    	checkIndex(row, col);;					// Check to see if the index given is within given grid.
    	return CheckOpenGrid[row][col];	
    }
    
    
    /** Is the site (row, column) full? */
    public boolean isFull(int row, int col) {     	
    	checkIndex(row, col);					// Check to see if the index given is within given grid.
    	
    	if (!isOpen(row, col)) {
        	return false; }
    	else {
    		return weightedQuickUnionUF.connected(Grid[row][col], top_row);
        }
    }
    
    
    /** Number of open sites.
     * Check each site in grid to see if it is marked as 'true' (open) in CheckOpenGrid. */
    public int numberOfOpenSites() {   	
    	int count = 0;
    	for (int i = 0; i < N; i++) { 
    		for (int j = 0; j < N; j++ ) {
    			if (isOpen(i,j)) 
    				{ count++; }
    		}
    	}  
    	return count;
    }
    
    
    /** Does the system percolate? 
     * Check to see if top and bottom row are connected. */
    public boolean percolates() { 
		// StdOut.println("Top: " + top_row + ", Bottom: " + bottom_row + "\n");
    	return weightedQuickUnionUF.connected(bottom_row, top_row); 
    }
    
    
	public static void main(String[] args) {
		StdOut.print("Grid size (N): ");
		int N = StdIn.readInt();		
	
		Percolation percolation = new Percolation(N);		// Create grid
		while (!percolation.percolates()) {					// While not percolating, open site in grid (p,q) randomly	
			// StdOut.print("Row: ");
			int row = StdRandom.uniform(0, (N));  // StdIn.readInt();
			
			// StdOut.print("Column: ");
			int col = StdRandom.uniform(0, (N)); // StdIn.readInt();
			
			StdOut.println("Row: " + row + ", Column: " + col);
			percolation.open(row, col);
		}		
				
		StdOut.print("\nNumber of sites in grid: ");
		StdOut.println(N*N);
		
		StdOut.print("Number of open sites: ");
		StdOut.println(percolation.numberOfOpenSites());

		StdOut.print("Percentage: ");
		StdOut.println((double) percolation.numberOfOpenSites() / (N*N));
	}
}
