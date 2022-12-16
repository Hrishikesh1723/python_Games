import java.io.File;

public class SomeProgram {
    public static void main(String[] args) {
        String current = "";
        File lastFile = null;
        for(String str : args){
            File newFile = new File((current + " " + str).trim());
            if(newFile.exists()){
                lastFile = newFile;
            }
        current += " " + str;
        }
        File yourFile = lastFile;
    }
}