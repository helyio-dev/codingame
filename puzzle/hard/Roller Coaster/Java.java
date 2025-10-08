import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

	public static void main(String args[]) {
	    long startTime = System.nanoTime();
		Scanner in = new Scanner(System.in);
		long nbPlaces = in.nextLong();
		long nbTours = in.nextLong();
		int nbGroupes = in.nextInt();
		int[] groupes = new int[nbGroupes];
		for (int i = 0; i < nbGroupes; i++) {
			groupes[i] = in.nextInt();
		}
		
		int[] gains = new int[nbGroupes];
		int[] groupeSuivant = new int[nbGroupes];
		
		for (int i = 0; i < nbGroupes; i++) {
		    int currentIndex = i;
		    gains[i] = 0;
		    while (true) {
		        int nextGp = groupes[currentIndex];
		        if (gains[i] + nextGp > nbPlaces) {
		            break;
		        }
		        gains[i] += nextGp;
		        
		        currentIndex++;
		        if (currentIndex == nbGroupes) {
		            currentIndex = 0;
		        }
		        
		        if (currentIndex == i) {
		            break;
		        }
		    }
		    groupeSuivant[i] = currentIndex;
		}
		
		long total = 0;
		int currentIndex = 0;
		
		for (int i = 0; i < nbTours; i++) {
		    total += gains[currentIndex];
		    currentIndex = groupeSuivant[currentIndex];
		}
		
		long elapsedTime = System.nanoTime() - startTime;
		System.err.println("Time : " + elapsedTime);
		
		System.out.println(total);
	}
}