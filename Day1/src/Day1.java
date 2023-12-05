import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Stack;

public class Day1 {
    public static void main(String[] args) throws Exception {
        int total = 0;
        int firstDigit, lastDigit;
        Stack<Integer> numberStack = new Stack<Integer>();

        try (BufferedReader reader = new BufferedReader(new FileReader("Day1/src/puzzle"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                firstDigit = -1;
                lastDigit = -1;

                for (int i = 0; i < line.length(); i++) {
                    int temp;

                    try {
                        temp = Integer.parseInt(line.substring(i, i + 1));

                        numberStack.push(temp);
                    } catch (NumberFormatException e) { }
                }

                lastDigit = numberStack.pop();

                while (!numberStack.empty()) {
                    firstDigit = numberStack.pop();
                }

                if (firstDigit == -1) {
                    firstDigit = lastDigit;
                }

                total += Integer.parseInt(String.valueOf(firstDigit) + String.valueOf(lastDigit));
            }
        }

        System.out.println(total);
    }
}
