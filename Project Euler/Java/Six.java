import java.lang.Math;

public class Six {
	public static void main(String[] args) {
		int sum = 0;
		int squareSum = 0;
		for (int i = 1; i <= 100; i++) {
			sum += i;
			squareSum += i * i;
		}
		int difference = (int)Math.pow(sum, 2) - squareSum;
		System.out.println(difference);
	}
}