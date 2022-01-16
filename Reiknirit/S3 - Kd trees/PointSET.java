package S3_Kd_trees;
import java.util.Arrays;
import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.SET;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Out;

/**
 * A mutable data type PointSET that represents a set of points in a unit square.
 * All points have x- and y-coordinates between 0 and 1.
 * Using a red-black BST, supporting efficient range search (finding all the points within a rectangle)
 * and supporting efficient nearest neighbour search (find closest point to a query point).
 * @author Benjamin Aage
 */
public class PointSET {	
	
	private SET<Point2D> set;
	
    // Implementing an empty set of points
    public PointSET() 
    	{ set = new SET<Point2D>(); }

    
    // Check to see if the set of points is empty (or not)
    public boolean isEmpty() 
    	{ return set.isEmpty(); }
    

    // Returning the number of points within the set
    public int size() 
    	{ return set.size(); }

    
    // Adding a new point (p) to the set
    public void insert(Point2D p) 
    	{ set.add(p); }

    
    // Check to see if a given point (p) is in the set
    public boolean contains(Point2D p) 
    	{ return set.contains(p); }

    
    // Draw all of the points within set
    public void draw() { 
    	for (Point2D p : set) 
    		{ p.draw(); }
    }

    
    // Check for all points in set, if they are within the rectangle and if so, return these points
    public Iterable<Point2D> range(RectHV rect) { 
    	SET<Point2D> within_range = new SET<Point2D>();
  	
    	for (Point2D curr_point : set) {
    		if (rect.contains(curr_point)) 
    			{ within_range.add(curr_point); }
    	}    	

    	return within_range; }

    
    // Returns the nearest point to the query point (p), null if the set is empty
    public Point2D nearest(Point2D p) { 
    	if (set.size() == 0)
    		{ return null; };
		
    	Point2D nearest_point = new Point2D(-1, -1);
    	for (Point2D point : set) {
    		if (point.distanceSquaredTo(p) < nearest_point.distanceSquaredTo(p))
    			{ nearest_point = point; }
    	}
    	
    	return nearest_point; }

    
    public static void main(String[] args) {
        In in = new In();
        Out out = new Out();
        int nrOfRecangles = in.readInt();
        int nrOfPointsCont = in.readInt();
        int nrOfPointsNear = in.readInt();
        RectHV[] rectangles = new RectHV[nrOfRecangles];
        Point2D[] pointsCont = new Point2D[nrOfPointsCont];
        Point2D[] pointsNear = new Point2D[nrOfPointsNear];
        
        for (int i = 0; i < nrOfRecangles; i++) {
            rectangles[i] = new RectHV(in.readDouble(), in.readDouble(),
                    in.readDouble(), in.readDouble()); }
        
        for (int i = 0; i < nrOfPointsCont; i++) 
        	{ pointsCont[i] = new Point2D(in.readDouble(), in.readDouble()); }
        
        for (int i = 0; i < nrOfPointsNear; i++) 
        	{ pointsNear[i] = new Point2D(in.readDouble(), in.readDouble()); }
        
        PointSET set = new PointSET();
        for (int i = 0; !in.isEmpty(); i++) {
            double x = in.readDouble(), y = in.readDouble();
            set.insert(new Point2D(x, y)); }
        
        for (int i = 0; i < nrOfRecangles; i++) {
            // Query on rectangle i, sort the result, and print
            Iterable<Point2D> ptset = set.range(rectangles[i]);
            int ptcount = 0;
            
            for (Point2D p : ptset)
                ptcount++;
            
            Point2D[] ptarr = new Point2D[ptcount];
            int j = 0;
            for (Point2D p : ptset) {
                ptarr[j] = p;
                j++; }
            
            Arrays.sort(ptarr);
            out.println("Inside rectangle " + (i + 1) + ":");
            for (j = 0; j < ptcount; j++)
                out.println(ptarr[j]);
        }
        
        out.println("Contain test:");
        for (int i = 0; i < nrOfPointsCont; i++) 
        	{ out.println((i + 1) + ": " + set.contains(pointsCont[i])); }

        out.println("Nearest test:");
        for (int i = 0; i < nrOfPointsNear; i++) 
        	{ out.println((i + 1) + ": " + set.nearest(pointsNear[i])); }

        out.println();
    }
}
