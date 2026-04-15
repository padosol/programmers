import java.io.*;
import java.util.*;

public class Main {

    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String input = br.readLine();
            if (input == null || input.equals("")) {
                break;
            }
            N = Integer.parseInt(input);

            int count = (int) Math.pow(3, N);
            // ---------------------------
            String result = divide(1, count);

            System.out.println(result);
        }
    }

    public static String divide(int x, int size) {

        if (size == 1) {
            return "-";
        }

        int quarter = size / 3;
        String left = divide(x, quarter);
        String center = " ".repeat(quarter);

        return left + center + left;
    }

}
