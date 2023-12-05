import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day1Test {

    @Test
    public void test1() {
        assertEquals(22, Day1.testParseLine("two2"));
    }

    @Test
    public void test2() {
        assertEquals(78, Day1.testParseLine("7sevensixone3threeoneight"));
    }
}