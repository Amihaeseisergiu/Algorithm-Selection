package process;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static long factorial(int number) {
        long result = 1;

        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }

        return result;
    }

    public static void main(String[] args) {
        List<String> stringList = new ArrayList<>();

        for (int i = 0; i < 50; i++) {
            stringList.add("aaaaaaaaaa".repeat(Math.max(0, 10000)));
            factorial(100000000);
        }
    }
}