package Practice;
import java.util.Arrays;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Out;
import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;

public class KdTree {

    private static class KdNode {
        private KdNode left;
        private KdNode right;
        private final boolean vertical;
        private final double x;
        private final double y;

        public KdNode(final double x, final double y, final KdNode l, final KdNode r, final boolean v) {
            this.x = x;
            this.y = y;
            left = l;
            right = r;
            vertical = v; }
    }


    private static final RectHV CONTAINER = new RectHV(0, 0, 1, 1);
    private KdNode root;
    private int size;

    
    public KdTree() {
        size = 0;
        root = null; }

    
    public boolean contains(final Point2D p) 
    	{ return contains(root, p.x(), p.y()); }


    private boolean contains(KdNode node, double x, double y) {
        if (node == null) 
        	return false;

        if (node.x == x && node.y == y) 
        	return true;

        if (node.vertical && x < node.x || !node.vertical && y < node.y)
            return contains(node.left, x, y);

        else
            return contains(node.right, x, y); 
    }


    public void draw() {
        StdDraw.setScale(0, 1);
        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.setPenRadius();
        CONTAINER.draw();
        draw(root, CONTAINER);
    }


    private void draw(final KdNode node, final RectHV rect) {
        if (node == null) 
        	return;

        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.setPenRadius(0.01);
        new Point2D(node.x, node.y).draw();
        Point2D min, max;

        if (node.vertical) {
            StdDraw.setPenColor(StdDraw.RED);
            min = new Point2D(node.x, rect.ymin());
            max = new Point2D(node.x, rect.ymax());
        } 
        
        else {
            StdDraw.setPenColor(StdDraw.BLUE);
            min = new Point2D(rect.xmin(), node.y);
            max = new Point2D(rect.xmax(), node.y);
        }

        StdDraw.setPenRadius();
        min.drawTo(max);

        draw(node.left, leftRect(rect, node));
        draw(node.right, rightRect(rect, node));
    }


    private KdNode insert(final KdNode node, final Point2D p, final boolean vertical) {
        if (node == null) {
            size++;
            return new KdNode(p.x(), p.y(), null, null, vertical);
        }

        if (node.x == p.x() && node.y == p.y()) 
        	return node;

        if (node.vertical && p.x() < node.x || !node.vertical && p.y() < node.y)
            node.left = insert(node.left, p, !node.vertical);

        else
            node.right = insert(node.right, p, !node.vertical);

        return node;
    }


    public void insert(final Point2D p)
    	{ root = insert(root, p, true); }


    public boolean isEmpty()
    	{ return size == 0; }


    private RectHV leftRect(final RectHV rect, final KdNode node) {
        if (node.vertical)
            return new RectHV(rect.xmin(), rect.ymin(), node.x, rect.ymax());
        else
            return new RectHV(rect.xmin(), rect.ymin(), rect.xmax(), node.y);
    }



    private Point2D nearest(final KdNode node, final RectHV rect, final double x, final double y, final Point2D candidate) {
        if (node == null) 
        	return candidate;

        double dqn = 0.0;
        double drq = 0.0;
        RectHV left = null;
        RectHV rigt = null;
        final Point2D query = new Point2D(x, y);
        Point2D nearest = candidate;

        if (nearest != null) {
            dqn = query.distanceSquaredTo(nearest);
            drq = rect.distanceSquaredTo(query);
        }

        if (nearest == null || dqn > drq) {
            final Point2D point = new Point2D(node.x, node.y);

            if (nearest == null || dqn > query.distanceSquaredTo(point))
                nearest = point;

            if (node.vertical) {
                left = new RectHV(rect.xmin(), rect.ymin(), node.x, rect.ymax());
                rigt = new RectHV(node.x, rect.ymin(), rect.xmax(), rect.ymax());

                if (x < node.x) {
                    nearest = nearest(node.left, left, x, y, nearest);
                    nearest = nearest(node.right, rigt, x, y, nearest);
                } 
                
                else {
                    nearest = nearest(node.right, rigt, x, y, nearest);
                    nearest = nearest(node.left, left, x, y, nearest);
                }
            } 
            
            else {
                left = new RectHV(rect.xmin(), rect.ymin(), rect.xmax(), node.y);
                rigt = new RectHV(rect.xmin(), node.y, rect.xmax(), rect.ymax());

                if (y < node.y) {
                    nearest = nearest(node.left, left, x, y, nearest);
                    nearest = nearest(node.right, rigt, x, y, nearest);
                } 
                
                else {
                    nearest = nearest(node.right, rigt, x, y, nearest);
                    nearest = nearest(node.left, left, x, y, nearest);
                }
            }
        }

        return nearest;
    }


    public Point2D nearest(final Point2D p)
    	{ return nearest(root, CONTAINER, p.x(), p.y(), null); }


    private void range(final KdNode node, final RectHV nrect, final RectHV rect, final Queue<Point2D> queue) {
        if (node == null) 
        	return;

        if (rect.intersects(nrect)) {
            final Point2D p = new Point2D(node.x, node.y);

            if (rect.contains(p)) 
            	queue.enqueue(p);

            range(node.left, leftRect(nrect, node), rect, queue);
            range(node.right, rightRect(nrect, node), rect, queue);
        }
    }


    public Iterable<Point2D> range(final RectHV rect) {
        final Queue<Point2D> queue = new Queue<Point2D>();
        range(root, CONTAINER, rect, queue);
        return queue;
    }


    private RectHV rightRect(final RectHV rect, final KdNode node) {
        if (node.vertical)
            return new RectHV(node.x, rect.ymin(), rect.xmax(), rect.ymax());

        else
            return new RectHV(rect.xmin(), node.y, rect.xmax(), rect.ymax());
    }


    public int size()
    	{ return size; }


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