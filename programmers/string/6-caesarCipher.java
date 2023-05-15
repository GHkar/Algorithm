// 시저 암호
public class Solution {

    // c를 n만큼 밀어 반환
    private char push(char c, int n){
        // 알파벳이 아닌 경우 문자를 그대로 이어 붙이기
        if (!Character.isAlphabetic(c)) return c;

        int offset = Character.isUpperCase(c) ? 'A' : 'a';
        int position = c - offset;
        position = (position + n) % ('Z' - 'A' + 1);

        return (char) (offset + position);
    }

    public String solution(String s, int n){
        // 입력 문자열의 모든 문자에 대해 반복
        StringBuilder builder = new StringBuilder();
        for (char c : s.toCharArray()){
            // c를 n만큼 민 문자를 builder에 이어 붙이기
            builder.append(push(c, n));
        }
        return builder.toString();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input1 = "AB";
        int input2 = 1;
        String result = answer.solution(input1, input2);

        System.out.print(result);
    }
}

