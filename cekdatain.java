public class cekdatain {
    public static void main(String[] args) {
        String data = "12345";
        if (data.matches("\\d+")) {
            System.out.println("Data valid: " + data);
        } else {
            System.out.println("Data tidak valid: " + data);
        }
    }
    
}
