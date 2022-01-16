package S2_PatternRecognition;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Out;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Stopwatch;

public class Brute {

	/**
	 * First, get number of points (N) in graph from user.
	 * Then, from 1 to N get an input of coordinates (x,y) from user.
	 * 
	 * To sort the order of points, the method Point.compareTo() is used, 
	 * using values based on the concept of Insertion sort.
	 * If value from compareTo() is equal to 1, then the points have to be swapped in the array,
	 * else the point (x0,y0) would be higher than point (x1, y1) in array. We want a slope of -1 for each.
	 * 
	 * At last, a check is made whether the slope of four consecutive point have equal slope between each other: 
	 * 			(p,q) && (q,r)   and   (q,r) && (r,s)
	 * If the same slope is between all of these points, print them out.
	 */
	public static void main(String[] args) {
		In in = new In();
		Out out = new Out();
		int z = in.readInt();
        Point[] points = new Point[z];
        
        for (int i = 0; i < z; i++) {
            int x = in.readInt(), y = in.readInt();
            points[i] = new Point(x, y); 
        }
        
        /*Stopwatch timer = new Stopwatch();*/
        
        // Arrays.sort(points);			Necessary?
        for (int j = 0; j < points.length; j++) {
			for (int k = 0; k < points.length - j - 1; k++) {
				if (points[k].compareTo(points[k+1]) == 1) {
					Point swapping_point = points[k];
					points[k] = points[k+1];
					points[k+1] = swapping_point;
				}
			}
		}

        
		for (int l = 0; l < points.length; l++) {
			for (int m = l + 1; m < points.length; m++) {
				for (int n = m + 1; n < points.length; n++) {
					for (int o = n + 1; o < points.length; o++) {
						if (points[l].slopeTo(points[m]) == points[m].slopeTo(points[n])) {
							if (points[m].slopeTo(points[n]) == points[n].slopeTo(points[o])) {
								out.println(points[l].toString() + " -> " + points[m].toString() + " -> " +
											 points[n].toString() + " -> " + points[o].toString());
							}
						}
					}
				}
			}
		}
		/*double time = timer.elapsedTime();
		StdOut.println("\nTimer: " + time);*/
		
	}

}
