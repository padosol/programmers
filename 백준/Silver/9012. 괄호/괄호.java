import java.io.*;
import java.util.*;

public class Main {

    static int N;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int j = 0; j < N; j++) {
            String s = br.readLine();

            int count = 0;
            for (int i = 0; i < s.length(); i++) {
                String ss = String.valueOf(s.charAt(i));
                if (ss.equals("(")) {
                    count++;
                } else {
                    count--;
                }

                if (count < 0) {
                    break;
                }
            }

            if (count == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        }

    }
}
