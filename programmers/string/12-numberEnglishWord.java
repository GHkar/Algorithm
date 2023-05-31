// 숫자 문자열과 영단어
public class Solution {

    // 영단어 문자열
    private static final String[] words = {
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    };


    public int solution(String s){
        // 영단어 배열을 순회하며 입력 문자열에 등장하는 모든 영어단어를 치환한 문자열 생성
        for (int i = 0; i < words.length; i++){
            s = s.replace(words[i], Integer.toString(i));
        }
        return Integer.parseInt(s);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "one4seveneight";
        int result = answer.solution(input);

        System.out.print(result);
    }
}
