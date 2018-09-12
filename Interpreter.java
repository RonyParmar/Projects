import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;

public class hw2 {
	public static void hw2(String input, String output) throws IOException{
	
		PrintStream myconsole=new PrintStream(new File(output));
		System.setOut(myconsole);
		
		BufferedReader in = new BufferedReader(new FileReader(input));
		
		ArrayList stack = new ArrayList();
		String line = in.readLine();
		while(line!=null){
			
		
			if(Character.isLetter(line.charAt(0))){
				stack = parsePrimitive(line, stack, myconsole);
			}
			else if(line.charAt(0)==':'){
				stack = parseBooleanOrError(line, stack);
			}
			else if(line.charAt(0)) == "\""
			else{
				myconsole.println("Error command!");
			}
			
			line = in.readLine();
		
		}
		in.close();
		
		
	}
	
	public static ArrayList parseBooleanOrError(String line, ArrayList stack) {
		if (line.startsWith(":e")){
			stack.add(0, ":error:");
		}
		else if (line.startsWith(":t")){
			stack.add(0, ":true:");
		}
		else if (line.startsWith(":f")){
			stack.add(0, ":false:");
		}
		
		return stack;
	}

	public static ArrayList doMul(ArrayList stack) {
		if (stack.size()<2){
			stack.add(0, ":error:");
		}
		else if (((String) stack.get(0)).charAt(0) == ':' || ((String) stack.get(1)).charAt(0) == ':'){
			stack.add(0, ":error:");
		}
		else{
			int x = Integer.parseInt((String) stack.get(1));
			int y = Integer.parseInt((String) stack.get(0));
			stack.remove(0);
			stack.remove(0);
			Integer newTop = x*y;
			stack.add(0, newTop.toString());
		}
		return stack;
	}

	public static ArrayList doSub(ArrayList stack) {
		if (stack.size()<2){
			stack.add(0, ":error:");
		}
		else if (((String) stack.get(0)).charAt(0) == ':' || ((String) stack.get(1)).charAt(0) == ':'){
			stack.add(0, ":error:");
		}
		else{
			int x = Integer.parseInt((String) stack.get(1));
			int y = Integer.parseInt((String) stack.get(0));
			stack.remove(0);
			stack.remove(0);
			Integer newTop = x-y;
			stack.add(0, newTop.toString());
		}
		return stack;
	}

	public static ArrayList doAdd(ArrayList stack) {
		if (stack.size()<2){
			stack.add(0, ":error:");
		}
		else if (((String) stack.get(0)).charAt(0) == ':' || ((String) stack.get(1)).charAt(0) == ':'){
			stack.add(0, ":error:");
		}
		else{
			int x = Integer.parseInt((String) stack.get(1));
			int y = Integer.parseInt((String) stack.get(0));
			stack.remove(0);
			stack.remove(0);
			Integer newTop = x+y;
			stack.add(0, newTop.toString());
		}
		return stack;
	}

	public static ArrayList parsePrimitive(String line, ArrayList stack, PrintStream myconsole){
		if (line.startsWith("add")){
			stack = doAdd(stack);
		}
		else if (line.startsWith("sub")){
			stack = doSub(stack);
		}
		else if (line.startsWith("mul")){
			stack = doMul(stack);
		}
		else if (line.startsWith("div")){
			stack = doDiv(stack);
		}
		else if (line.startsWith("rem")){
			stack = doRem(stack);
		}
		else if (line.startsWith("pop")){
			stack = doPop(stack);
		}
		else if (line.startsWith("push")){
			stack = doPush(stack, line);
		}
		else if (line.startsWith("swap")){
			stack = doSwap(stack);
		}
		else if (line.startsWith("neg")){
			stack = doNeg(stack);
		}
		else if (line.startsWith("quit")){
			doQuit(stack, myconsole);
		}
		
		
		return stack;
	}

	public static void doQuit(ArrayList stack, PrintStream myconsole) {
		for (int i = 0; i < stack.size(); i++){
			myconsole.println(stack.get(i));
		}
		myconsole.close();
	}

	public static ArrayList doNeg(ArrayList stack) {
		if (stack.isEmpty()){
			stack.add(0, ":error:");
		}
		else if (((String) stack.get(0)).charAt(0) == ':'){
			stack.add(0, ":error:");
		}
		else{
			int x = Integer.parseInt((String) stack.get(0));
			Integer newTop = -1*x;
			stack.remove(0);
			stack.add(0, newTop.toString());
			}
		return stack;
	}

	private static ArrayList doSwap(ArrayList stack) {
		if (stack.size() < 2){
			stack.add(0, ":error:");
		}
		else{
			String x = (String) stack.get(1);
			String y = (String) stack.get(0);
			stack.remove(0);
			stack.remove(0);
			stack.add(0, y);
			stack.add(0, x);
		}
		return stack;
	}

	public static ArrayList doPush(ArrayList stack, String line) {
//		String[] lineList = line.split(" ");
//		String getNum = Arrays.asList(lineList).get(1);
//		stack.add(0, getNum);
		
		//stack.add(0, line.substring(5));
		String getNum = line.substring(5);
		if (getNum.charAt(0) == '-'){
			if (getNum.substring(1).equals("0")){
				stack.add("0");
			}
			else if (getNum.substring(1).matches("[0-9]+")){
				stack.add(0, getNum);
			}
			else{
				stack.add(0, ":error:");
			}
		}
		else if (getNum.matches("[0-9]+")){
			stack.add(0, getNum);
		}
		else{
			stack.add(0, ":error:");
		}
		return stack;
	}

	public static ArrayList doPop(ArrayList stack) {
		if (stack.size() < 1){
			stack.add(0, ":error:");
		}
		else{
			stack.remove(0);
		}
		return stack;
	}

	public static ArrayList doRem(ArrayList stack) {
		if (stack.size()<2){
			stack.add(0, ":error:");
		}
		else if (((String) stack.get(0)).charAt(0) == ':' || ((String) stack.get(1)).charAt(0) == ':'){
			stack.add(0, ":error:");
		}
		else{
			int x = Integer.parseInt((String) stack.get(1));
			int y = Integer.parseInt((String) stack.get(0));
			if (y == 0){
				stack.add(0, ":error:");
			}
			else{
				stack.remove(0);
				stack.remove(0);
				Integer newTop = x%y;
				stack.add(0, newTop.toString());
			}
		}
		return stack;
	}

	public static ArrayList doDiv(ArrayList stack) {
		if (stack.size()<2){
			stack.add(0, ":error:");
		}
		else if (((String) stack.get(0)).charAt(0) == ':' || ((String) stack.get(1)).charAt(0) == ':'){
			stack.add(0, ":error:");
		}
		else{
			int x = Integer.parseInt((String) stack.get(1));
			int y = Integer.parseInt((String) stack.get(0));
			if (y == 0){
				stack.add(0, ":error:");
			}
			else{
				stack.remove(0);
				stack.remove(0);
				Integer newTop = x/y;
				stack.add(0, newTop.toString());
			}
		}
		return stack;
	}
}
