package java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * This code challenge is from https://developers.turing.com/dashboard/coding_challenge
 * Given a string morsecode that contains a list of '.’and '-' . You are allowed to make one move and replace two consecutive ".." with "--"
 * Return all possible morse codes you can get after a single move you do to the string morsecode
 * If you cannot do any moves, just return an empty array.
 * <p>
 * Example 1:
 * Input: morsecode = "...."  Output: ["--..",".--.","..--"]
 * <p>
 * Constraints:. 1 <= morsecode.length <= 58e· morsecode[i] is either '.' or '-".
 */
public class MorseCode {
    public static void main(String[] args)
            throws IOException {
        // Enter data using BufferReader
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(System.in));
        // Reading data using readLine
        String morseCode = reader.readLine();
        System.out.println(replaceAll(morseCode));
    }

    public static List<String> replaceAll(String morseCode) {
        List<String> ans = new ArrayList<>();
        String morseCodeArray[] = morseCode.split("");
        if (morseCode.length() >= 1 && morseCode.length() <= 500) {
            for (int i = 0; i < morseCodeArray.length - 1; i++) {
                if (!morseCodeArray[i].equals(".") && !morseCodeArray[i].equals("-")) {
                    return ans;
                }
                if ("..".equals(morseCodeArray[i] + morseCodeArray[i + 1])) {
                    morseCodeArray[i] = "-";
                    morseCodeArray[i + 1] = "-";
                    StringBuilder sb = new StringBuilder();
                    for (String s : morseCodeArray) {
                        sb.append(s);
                    }
                    ans.add(sb.toString());
                    morseCodeArray = morseCode.split("");
                }
            }
        }
        return ans;
    }
}