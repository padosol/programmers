import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static Deque<Integer> nums;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        nums = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                nums.removeLast();
            } else {
                nums.add(num);
            }
        }

        if (nums.size() == 0) {
            System.out.println(0);
        } else {
            System.out.println(nums.stream().mapToInt(Integer::intValue).sum());
        }
    }
}
