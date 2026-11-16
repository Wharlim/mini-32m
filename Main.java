public class Main {

public static int countVowels(String string){
    int count = 0;
    String lowerText = string.toLowerCase();
    for (int i = 0; i < lowerText.length(); i++){
        char c = lowerText.charAt(i);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
            count++;
        }
    }
    return count;
}
public static int sumEvens(int[] arr) {
    int sum = 0;
    for (int num:arr){
        if (num % 2 == 0){
            sum += num;
        }
    }
    return sum;
}
public static void main(String[] args) {
    int sample = sumEvens(new int[]{1,2,3,4,5,6});
    String thing = "Something";
    System.out.println(sample);
    System.out.println(countVowels(thing));
}
}