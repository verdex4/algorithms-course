import java.util.HashMap;
import java.util.Stack;

public class CorrectString {
    public static boolean run(String s) {
        if (s.length() % 2 != 0) {
            return false;
        }

        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> brackets = new HashMap<>();
        brackets.put('}', '{');
        brackets.put(']', '[');
        brackets.put(')', '(');

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            // если встретили закрывающую скобку, то ожидаем, что есть открывающая
            if (brackets.containsKey(c)) {
                // если стэк пуст или последний элемент не является открывающей скобкой
                if (stack.isEmpty() || stack.pop() != brackets.get(c)) {
                    return false;
                }
                continue;
            }
            // если встретили открывающую скобку, то добавляем в стэк
            stack.push(s.charAt(i));
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(run("()[]{}")); // true
        System.out.println(run("[(])")); // false
        System.out.println(run("([{}])")); // true
    }
}
