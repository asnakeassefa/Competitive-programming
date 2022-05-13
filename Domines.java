import java.util.Scanner;
 
public class Dominoes {
	public static int noOfDomines(int M, int N)
	{
		return (M*N)/2;
	}
 
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
 
		int M,N;
		M = input.nextInt();
		N = input.nextInt();
 
		System.out.println(noOfDomines(M,N));
	}
}
