import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Map.Entry;

public class Day1 {
    public static void main(String[] args) throws Exception {
        int total = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader("Advent/src/puzzle"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                total += parseLine(line);
            }
        }

        System.out.println(total);
    }

    public static int testParseLine(String line) {
        return parseLine(line);
    }

    private static int parseLine(String line) {
        int firstDigit, lastDigit;
        Stack<Integer> numberStack = new Stack<Integer>();
        Pattern pattern = Pattern.compile("[1-9]");
        Matcher matcher;

        HashMap<String, Integer> wordNumbers = new HashMap<String, Integer>() {{
            put("one", 1);
            put("two", 2);
            put("three", 3);
            put("four", 4);
            put("five", 5);
            put("six", 6);
            put("seven", 7);
            put("eight", 8);
            put("nine", 9);
        }};

        // System.err.println(line);

        firstDigit = -1;
        lastDigit = -1;

        for (int i = 0; i < line.length(); i++) {
            int temp;

            try {
                temp = Integer.parseInt(line.substring(i, i + 1));

                numberStack.push(temp);
            } catch (NumberFormatException e) {
                int endIndex = i + 5 > line.length() ? line.length() : i + 5;
                String characters = line.substring(i, endIndex);

                for (Entry<String, Integer> set : wordNumbers.entrySet()) {
                    String key = set.getKey();
                    Integer value = set.getValue();

                    matcher = pattern.matcher(characters);
                    int regexIndex = Integer.MAX_VALUE;
                    if(matcher.find()){
                        regexIndex = matcher.start();
                    }

                    if (characters.indexOf(key) != -1 && characters.indexOf(key) < regexIndex) {
                        numberStack.push(value);

                        break;
                    }
                }
            }
        }

        lastDigit = numberStack.pop();

        while (!numberStack.empty()) {
            firstDigit = numberStack.pop();
        }

        if (firstDigit == -1) {
            firstDigit = lastDigit;
        }

        return Integer.parseInt(String.valueOf(firstDigit) + String.valueOf(lastDigit));
    }
}
