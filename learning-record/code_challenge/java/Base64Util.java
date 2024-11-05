import java.io.UnsupportedEncodingException;
import java.util.Base64;

public class Base64Util {
    public static void main(String[] args){
       System.out.println(Base64Util.setEncryptionBase64("123456"));
    }

    public static String setEncryptionBase64(String str) {
        byte[] b = null;
        String s = null;
        try {
            b = str.getBytes("utf-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        if (b != null) {
            Base64.Encoder encoder = Base64.getMimeEncoder();
            s = encoder.encodeToString(b);
        }
        return s;
    }
}