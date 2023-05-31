// 신규 아이디 추천
public class Solution {
    public String solution(String newId){
        // 1단계
        newId = newId.toLowerCase();
        // 2단계
        newId = newId.replaceAll("[^a-z0-9\\-_.]", "");
        // 3단계
        newId = newId.replaceAll("\\.+", ".");
        // 4단계
        newId = newId.replaceAll("^\\.+|\\.+$", "");
        // 5단계
        if (newId.isEmpty()) newId = "a";
        // 6단계
        if (newId.length() >= 16){
            newId = newId.substring(0, 15);
            newId = newId.replaceAll("\\.+$", "");
        }
        // 7단계
        while (newId.length() < 3){
            newId += newId.charAt(newId.length() - 1);
        }
        return newId;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "...!@BaT#*..y.abcdefghijklm";
        String result = answer.solution(input);

        System.out.print(result);
    }
}
