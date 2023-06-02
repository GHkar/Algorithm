import java.util.ArrayList;
import java.util.List;

// 모음 사전
public class Solution {
    // 사용할 수 있는 모든 문자
    private static final char[] CHARS = "AEIOU".toCharArray();
    // 재귀 method
    private void generate(String word, List<String> words){
        words.add(word);

        // 종료 조건
        if (word.length() == 5) return;

        // 점화식 구현
        for (char c : CHARS){
            generate(word + c, words);
        }
    }
    public int solution(String word){
        List<String> words = new ArrayList<>();
        generate("", words);
        return words.indexOf(word);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "AAAAE";
        int result = answer.solution(input);

        System.out.print(result);
    }
}
