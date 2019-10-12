import java.awt.Point;
import java.util.Arrays;
import java.util.Comparator;
import java.util.TreeSet;

/**
 * Modified from https://baptiste-wicht.com/posts/2010/04/closest-pair-of-point-plane-sweep-algorithm.html
 * It's the same algorithm for closest pair of point.
 * The only difference is the way to calculate the distance.
 *
 */
public class Codility2018Rubidium {

	public int solution(int[] X, int[] Y) {
		Point[] sorted = new Point[X.length];
		for(int i=0; i<X.length; i++)
		{
			sorted[i] = new Point(X[i],Y[i]);
		}

		//When we start the min distance is the infinity
		int crtMinDist = 200000;

		//Get the points and sort them
		Arrays.sort(sorted, HORIZONTAL_COMPARATOR);

		//When we start the left most candidate is the first one
		int leftMostCandidateIndex = 0;

		//Vertically sorted set of candidates
		TreeSet<Point> candidates = new TreeSet<Point>(VERTICAL_COMPARATOR);

		//For each point from left to right
		for (Point current : sorted) {
			//Shrink the candidates
			while (current.x - sorted[leftMostCandidateIndex].x > crtMinDist) {
				candidates.remove(sorted[leftMostCandidateIndex]);
				leftMostCandidateIndex++;
			}

			//Compute the y head and the y tail of the candidates set
			Point head = new Point(current.x, current.y - crtMinDist);
			Point tail = new Point(current.x, current.y + crtMinDist);

			//We take only the interesting candidates in the y axis
			for (Point point : candidates.subSet(head, tail)) {
				int distance = distance(current, point);

				//Simple min computation
				if (distance < crtMinDist) {
					crtMinDist = distance;
				}
			}

			//The current point is now a candidate
			candidates.add(current);
		}

		return crtMinDist/2;
	}

	private static int distance(Point a, Point b)
	{
		return Math.max(Math.abs(a.x-b.x), Math.abs(a.y-b.y));
	}

	private static final Comparator<Point> VERTICAL_COMPARATOR = new Comparator<Point>() {
		@Override
		public int compare(Point a, Point b) {
			if (a.y < b.y) {
				return -1;
			}
			if (a.y > b.y) {
				return 1;
			}
			if (a.x < b.x) {
				return -1;
			}
			if (a.x > b.x) {
				return 1;
			}
			return 0;
		}
	};

	private static final Comparator<Point> HORIZONTAL_COMPARATOR = new Comparator<Point>() {
		@Override
		public int compare(Point a, Point b) {
			if (a.x < b.x) {
				return -1;
			}
			if (a.x > b.x) {
				return 1;
			}
			if (a.y < b.y) {
				return -1;
			}
			if (a.y > b.y) {
				return 1;
			}
			return 0;
		}
	};

	public static void main(String[] args) {
		var p = new Codility2018Rubidium();
		System.out.println(p.solution(new int[] {0,0,10,10}, 
				new int[] {0,10,0,10})); //5
		System.out.println(p.solution(new int[] {1,1,8}, 
				new int[] {1,6,0})); //2
	}

}
