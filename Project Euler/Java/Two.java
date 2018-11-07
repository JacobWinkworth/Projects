import java.lang.Math;

public class Two {
	public static void main(String[] args) {
		float fibNum = 1;
		int total = 0;
		while(fibNum < 4000000) {
			fibNum = Math.round(fibNum * ((1 + Math.sqrt(5)) / 2));
			if(fibNum % 2 == 0) {
				total += fibNum;
			}
		}
		System.out.println(total);
	}
}