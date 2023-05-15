// 이상한 문자 만들기
public class Solution {

    public String solution(String s){
        // 입력 문자열의 모든 문자에 대해 반복
        StringBuilder builder = new StringBuilder();
        boolean toUpper = true;
        // c를 적절히 변환하여 builder에 추가
        for (char c : s.toCharArray()){
            // 문자가 공백 문자일 경우
            if (!Character.isAlphabetic(c)){
                // 공백 처리 (그대로 이어 붙이기)
                builder.append(c);
                toUpper = true;
            } else{
                // 알파벳 변환
                if (toUpper){
                    builder.append(Character.toUpperCase(c));
                } else {
                    builder.append(Character.toLowerCase(c));
                }
                toUpper = !toUpper;
            }
        }
        return builder.toString();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "try hello world";
        String result = answer.solution(input);

        System.out.print(result);
    }
}

