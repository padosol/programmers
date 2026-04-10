import java.io.*;
import java.util.*;

public class Main {

    static int N;

    static Deque<Integer> q;
    static Deque<Integer> line;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        line = new ArrayDeque<>();
        q = new ArrayDeque<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            line.add(Integer.parseInt(st.nextToken()));
        }

        int cur = 1;
        boolean possible = true;
        while (possible) {
            Integer lineNum = line.peekFirst();
            Integer qNum = q.peekLast();
            if (lineNum == null && qNum == null) {
                break;
            }

            if (lineNum != null && lineNum == cur) {
                line.removeFirst();
                cur += 1;
            } else if (qNum != null && qNum == cur) {
                q.removeLast();
                cur += 1;
            } else {
                if (qNum == null) {
                    q.addLast(lineNum);
                    line.removeFirst();
                } else if (lineNum == null) {
                    possible = false;
                } else {
                    if (lineNum > qNum) {
                        possible = false;
                    } else {
                        q.addLast(lineNum);
                        line.removeFirst();
                    }
                }
            }
        }

        if (possible) {
            System.out.println("Nice");
        } else {
            System.out.println("Sad");
        }
    }
}
