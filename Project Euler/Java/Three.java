import java.lang.Math;
import java.util.List;
import java.lang.Integer;

public class Three {
	public static void main(String[] args) {
		long target = 600851475143L;
		double sqrtTarget = Math.sqrt(600851475143L);
		int total = 1;
		for (int i = 3; i <= sqrtTarget; i++) {
			if (target % i == 0) {
				System.out.println(i);
				total *= i;
				if (total == target) {
					break;
				}
			}
		}
	}
}