package S2_PatternRecognition;
import java.util.Arrays;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Stopwatch;

public class Fast {

	/**
	 * Select a point from the given array, and have as a base point.
	 * Sort the points according to the slope made with base point.
	 *
	 * For each other point in array, check the slope they make with the current base point.
	 * 
	 * Check if any three (or more) points in the sorted array have equal slope in 
	 * regards to the chosen base point. If they do, invoke the print-out-method.
	 */
	public static void findMatchingPoints(Point[] points) {		
		Arrays.sort(points, 0, points.length);
		
		Point[] copy_points = new Point[points.length];
		for (int j = 0; j < points.length; j++) 
			{ copy_points[j] = points[j]; } 
		
		int current_slope_points = 1;
		for (int i = 0; i < points.length - 1; i++) {
			Point base_point = points[i];
			Arrays.sort(points, i + 1, points.length, base_point.SLOPE_ORDER);
			double first_slope = points[i].slopeTo(points[i+1]);	
			for (int j = i + 2; j < points.length; j++) {
				if (points[i].slopeTo(points[j]) == first_slope) 
					{ current_slope_points++; }
				
				else {
					first_slope = points[i].slopeTo(points[j]);
					current_slope_points = 1; }

				if (current_slope_points == 3) { 
					printPointSequences(points, i, j); 
					current_slope_points = 1; }
			}
		}
	}
	
	
	/**
	 * If three or more points have equal slope to the given base point,
	 * these points (plus base points) are collinear and are printed out.
	 */
	public static void printPointSequences(Point[] points, int base_point, int high) {
		StdOut.print(points[base_point] + " -> ");
		for (int i = high-2; i <= high; i++) {
			if (i == high) 
				{ StdOut.println(points[i]); }
			else 
				{ StdOut.print(points[i] + " -> "); }
		}
	}
	
	
	/**
	 *  Created an array of points from the input of user, and
	 *  check for matches within points in array (using findMatchingPoints() method). 
	 * */ 
	public static void main(String[] args) {
		In in = new In();
		int N = in.readInt();
        Point[] points = new Point[N];
        
        for (int i = 0; i < N; i++) {
            int x = in.readInt(), y = in.readInt();
            points[i] = new Point(x, y); }
        
		/*Stopwatch timer = new Stopwatch();*/
        findMatchingPoints(points); 
		/*double time = timer.elapsedTime();
		StdOut.println("\nTimer: " + time); */
		}
}
