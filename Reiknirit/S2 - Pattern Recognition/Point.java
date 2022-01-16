package S2_PatternRecognition;
import java.util.Comparator;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Out;
import edu.princeton.cs.algs4.StdDraw;

/*************************************************************************
 * Compilation: javac Point.java Execution: Dependencies: StdDraw.java
 * Description: An immutable data type for points in the plane.
 *
 * @author Benjamín Aage Birgisson, email: benjamin18@ru.is
 *************************************************************************/

public class Point implements Comparable<Point> {
    public final int x, y;

    /** Comparing points by their slope. */
    public final Comparator<Point> SLOPE_ORDER = new Comparator<Point>()
    	{
    		public int compare(Point p0, Point p1) {
    			double s0 = slopeTo(p0);
    			double s1 = slopeTo(p1);
    			    			
    			if (s0 < s1) 
    				{ return -1; }
       			if (s0 > s1) 
    				{ return 1; }
    			return 0; }
    	};
    
    
    /** Create the point (x, y). */
    public Point(int x, int y) {
        this.x = x;
        this.y = y; }

    
    /** Plot this point to standard drawing. */
    public void draw() 
    	{ StdDraw.point(x, y); }

    
    /** Draw a line between this point and that point to standard drawing. */
    public void drawTo(Point that) 
    	{ StdDraw.line(this.x, this.y, that.x, that.y); }

    
    /**
     * Return the slope between the invoking point (this)
     * and the argument point (that) by calculating the following:
     * (y1 - y0) / (x1 - x0)
     * Slope of a horizontal line 				 == positive zero (+0.0)
     * Slope of a vertical line   				 == Double.POSITIVE_INFINITY
     * Slope of a degenerate line (self to self) == Double.NEGATIVE_INFINITY
     */
    public double slopeTo(Point that) {
    	if (y == that.y && x == that.x) 
    		{ return Double.NEGATIVE_INFINITY; }
    	
    	else if (x == that.x) 
    		{ return Double.POSITIVE_INFINITY; }
    	
    	else if (y == that.y)
    		{ return +0.0; }
    	
    	else 
    		{ return (double) (y - that.y) / (double) (x - that.x); }
    	}

    
    /**
     * Comparing two points by their y-coordinates, and if y-coordinates
     * are the same, compare their x-coordinates. 
     * Example: 
     * The point (x0,y0) is less than point (x1,y1) if either:
     *          y0 < y1      OR IF      y0 = y1 and x0 < x1. 		(return -1)
     * If points refer to themselves, return 0
     * else return 1.
     */
    public int compareTo(Point that) {
    	if (y < that.y || (y == that.y && x < that.x)) 
			{ return -1; }
	
    	else if (y == that.y && x == that.x) 
    		{ return 0; }
    
    	else 
    		{ return 1; }
    }

    
    /** Return string representation of this point. */
    public String toString() 
    	{ return "(" + x + ", " + y + ")"; }

    
    /**
     * Getting input from user to create an array of points (N in total).
     * Then doing tests (with print statements) of the methods created:
     * 		1. Slope between points (invoking point & argument point)
     * 		2. Comparing points from (x,y) coordinates
     * 		3. Comparing points by their slope 
     */
    public static void main(String[] args) {
        In in = new In();
        Out out = new Out();
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt(), y = in.readInt();
            points[i] = new Point(x, y);
        }
        out.printf("Testing slopeTo method...\n");
        for (int i = 1; i < points.length; i++) {
            out.println(points[i].slopeTo(points[i - 1]));
        }
        out.printf("Testing compareTo method...\n");
        for (int i = 1; i < points.length; i++) {
            out.println(points[i].compareTo(points[i - 1]));
        }
        out.printf("Testing SLOPE_ORDER comparator...\n");
        for (int i = 2; i < points.length; i++) {
            out.println(points[i].SLOPE_ORDER.compare(points[i - 1],
                    points[i - 2]));
        }
    }
}
