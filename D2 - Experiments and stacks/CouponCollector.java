package D2_Experiments_Stacks;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class CouponCollector {
	public static int couponCollectorTest(int N) {
		int[] cards = new int[N];						// Create an array for N number of cards to be collected
		int count = 0;									// Counter for how many cards have been collected in total (incl.duplicates)
		int cards_collected = 0;						// Number of cards that have been collected (without duplications)

		while (cards_collected < N) {					// Continue until all cards have been collected
			int new_card = StdRandom.uniform(N);		// Create a random card (index)
			count++;
	
			if (cards[new_card] == 0) {					// Check to see if card in array has not yet been 'collected'....
				cards[new_card] = 1;					// ... and if not collected, mark as 'collected'
				cards_collected++;
			}
		}
	
		return count;
	}
	

	public static void main(String[] args) {
		StdOut.print("How many cards in collection? ");
		int N = StdIn.readInt(); 
		
		int result = couponCollectorTest(N);
		StdOut.println("Total numbers generated in the process: " + result);
		}
}
