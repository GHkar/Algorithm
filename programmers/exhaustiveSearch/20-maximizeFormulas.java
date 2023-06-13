import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

// 수식 최대화
public class Solution {
    // 연산자의 우선순위
    private static final String[][] precedences = {
            "+-*".split(""),
            "+*-".split(""),
            "-+*".split(""),
            "-*+".split(""),
            "*+-".split(""),
            "*-+".split(""),
    };

    // 연산 결과 반환
    private long calculate(long lhs, long rhs, String op) {
        return switch (op){
            case "+" -> lhs + rhs;
            case "-" -> lhs - rhs;
            case "*" -> lhs * rhs;
            default -> 0;
        };
    }

    // 연산자 우선순위를 이용하여 계산
    private long calculate(List<String> tokens, String[] precedence){
        for (String op : precedence) {
            for (int i = 0; i < tokens.size(); i++){
                if (tokens.get(i).equals(op)) {
                    long lhs = Long.parseLong(tokens.get(i - 1));
                    long rhs = Long.parseLong(tokens.get(i + 1));
                    long result = calculate(lhs, rhs, op);

                    tokens.remove(i - 1);
                    tokens.remove(i - 1);
                    tokens.remove(i - 1);
                    tokens.add(i - 1, String.valueOf(result));
                    // 순회하는 인덱스 i를 앞당겨 옴
                    i -= 2;
                }
            }
        }
        return Long.parseLong(tokens.get(0));
    }

    public long solution(String expression){
        StringTokenizer tokenizer = new StringTokenizer(expression, "+-*", true);
        List<String> tokens = new ArrayList<>();
        while (tokenizer.hasMoreTokens()){
            tokens.add(tokenizer.nextToken());
        }

        long max = 0;
        for (String[] precedence : precedences){
            long value = Math.abs(calculate(new ArrayList<>(tokens), precedence));
            if (value > max){
                max = value;
            }
        }
        return max;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "100-200*300-500+20";
        long result = answer.solution(input);

        System.out.print(result);
    }
}
