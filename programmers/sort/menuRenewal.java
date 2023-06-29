import java.util.*;
import java.util.stream.Collectors;

// 메뉴 리뉴얼
public class Solution {
    // 코스 클래스 - 코스 구성과 주문 목록에서 등장한 횟수
    private static class Course{
        public final String course;
        public final int occurrences;

        public Course(String course, int occurrences){
            this.course = course;
            this.occurrences = occurrences;
        }
    }

    // 재귀 (다음 메뉴, 현재까지 선택한 메뉴, 주문 목록, 구한 코스)
    private void getCourses(char nextMenu, Set<String> selectedMenus, List<Set<String>> orderList, Map<Integer, List<Course>> courses){
        //  현재까지 조합한 메뉴들의 등장 횟수
        int occurrences = (int) orderList.stream()
                .filter(order -> order.containsAll(selectedMenus))
                .count();
        // 종료 조건
        if (occurrences < 2) return;

        // 포함된 메뉴 개수
        int size = selectedMenus.size();

        // 현재까지 찾은 코스를 CourseList에 넣기
        // 구해야 하는 코스 크기에 size가 포함되어있는지 검사 후, 포함되어 있다면 해당 리스트를 구함
        if (courses.containsKey(size)){
            List<Course> courseList = courses.get(size);
            // 코스 생성
            Course course = new Course(selectedMenus.stream()
                    .sorted()
                    .collect(Collectors.joining("")), occurrences);

            // 기존 코스 불러오기
            Course original  = courseList.get(0);

            // 기존 코스와 등장 횟수를 비교하여 대체하거나 추가
            if (original.occurrences < occurrences){
                courseList.clear();
                courseList.add(course);
            } else if (original.occurrences == occurrences){
                courseList.add(course);
            }
        }

        // 종료 조건
        if (size >= 10) return;

        // nextMenu와 그 이후의 메뉴를 검사
        for (char menuChar = nextMenu; menuChar <= 'Z'; menuChar++){
            String menu = String.valueOf(menuChar);
            selectedMenus.add(menu);
            getCourses((char) (menuChar + 1), selectedMenus, orderList, courses);
            selectedMenus.remove(menu);
        }
    }

    public String[] solution(String[] orders, int[] course) {
        // 주문 목록
        List<Set<String>> orderList = Arrays.stream(orders)
                .map(String::chars)
                .map(charStream -> charStream
                        .mapToObj(menu -> String.valueOf((char) menu))
                        .collect(Collectors.toSet()))
                .collect(Collectors.toList());
        // 생성된 코스
        Map<Integer, List<Course>> courses = new HashMap<>();
        for(int length : course){
            List<Course> list = new ArrayList<>();
            list.add(new Course("", 0));
            courses.put(length, list);
        }
        // 재귀 호출
        getCourses('A', new HashSet<>(), orderList, courses);

        // 정렬
        return courses.values().stream()
                .filter(list -> list.get(0).occurrences > 0)
                .flatMap(List::stream)
                .map(c -> c.course)
                .sorted()
                .toArray(String[]::new);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String[] input1 = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] input2 = {2,3,4};
        String[] result = answer.solution(input1, input2);

        System.out.print(Arrays.toString(result));
    }
}
