import java.util.Scanner;

public class Main {

   public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        long num = s.nextInt(), b=s.nextInt();
        long temp=1, n;
        String answer = "";

        for(;;) {
            if(num>=temp) {
                temp*=b;
            }
            else {
                temp/=b;
                break;
            }
        }
        while(true) {
            if(temp!=0) {
                n = num/temp;
                num %= temp;
                if(n>9) {
                    n+=55;
                    answer+=(char)n;
//                    System.out.print((char)n);
                }
                else
                    answer+=n;
//                    System.out.print(n);
            }
            else
                break;
            temp /= b;

        }
        System.out.println(answer);
        s.close();
            
   }
}
