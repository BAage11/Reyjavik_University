package S3_Kd_trees;
import java.util.Arrays;
import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Out;


public class KdTree {
	
	private Node root;
	private int size;
		
	// Placeholder of each node (point), its children, and the node rectangle surrounding */
	private static class Node {
    	private Point2D p;
    	private RectHV rect;
    	private Node left;
    	private Node right;
    	
    	public Node(Point2D p, RectHV rect) {
    		this.p = p;
    		this.rect = rect; }
    }
    
	
	// Constructing an empty set of points
    public KdTree() { 
    	root = null; 
    	size = 0; }
    

    // Check to see if the set is empty, or not
    public boolean isEmpty() 
    	{ return size == 0; }

    
    // Return the size of the set (number of points)
    public int size() 
    	{ return size; }

// ################################################################################################
    // add the point p to the set (if it is not already in the set)
    public void insert(Point2D p) {
    	root = insert(root, p);
    }
    
    
    private Node insert(Node node, Point2D p) {
    	if (node == null) {
    		size++;
    		return new Node(p.x(), p.y());
    	}
    } 

    // does the set contain the point p?
    public boolean contains(Point2D p) {
    	if (p == null) 
    		{ return false; }
    	
    	
    	return true; }

    // draw all of the points to standard draw
    public void draw() 
    	{ }

    // all points in the set that are inside the rectangle
    public Iterable<Point2D> range(RectHV rect) 
    	{ return null; }

    // a nearest neighbour in the set to p; null if set is empty
    public Point2D nearest(Point2D p) 
    	{ return p; }
    // ################################################################################################
    
    
    /*******************************************************************************
     * Test client
     ******************************************************************************/
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
        
        KdTree set = new KdTree();
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
