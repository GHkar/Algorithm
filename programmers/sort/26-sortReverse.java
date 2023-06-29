
// 문자열 내림차순으로 배치하기
public class Solution {
    public String solution(String s) {
        return s.chars()
                .boxed()
                .sorted((v1, v2) -> v2 - v1)
                .collect(StringBuilder::new,
                        StringBuilder::appendCodePoint,
                        StringBuilder::append)
                .toString();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "Zbcdefg";
        String result = answer.solution(input);

        System.out.print(result);
    }
}
