//package org.openqa.selenium.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;

public class example  {
	
	public static String getTempFromSource(String res){
        int begining = res.indexOf("<h2>");
        int end = res.indexOf("</h2>");
        String convertRes = res.substring(begining, end);
        int b = convertRes.indexOf("=");
        if(b!=-1){
        	int e = convertRes.indexOf("Celsius")-1;
            String value = convertRes.substring(b+2, e);
            return value;
        }
        else{
        	return res.substring(begining + 2, end);
        }
        
	}
	
	public static String convertTemp(Double temp){
        WebElement box = driver.findElement(By.name("farenheitTemperature"));
        box.clear();
        box.sendKeys(temp.toString());
        box.submit();
        
        String res = driver.getPageSource();
        int begining = res.indexOf("<h2>");
        int end = res.indexOf("</h2>");
        String convertRes = res.substring(begining, end);
        int b = convertRes.indexOf("=") + 2;
        int e = convertRes.indexOf("Celsius")-1;
        String value = convertRes.substring(b, e);
        //Double dValue = Double.parseDouble(value);
        //System.out.println(dValue);
        return value;

	}
	
	private static WebDriver driver;
	
	public static void login(){
		driver = new HtmlUnitDriver();
		
		driver.get("http://apt-public.appspot.com/testing-lab-login.html");

        WebElement element = driver.findElement(By.name("userId"));

        element.clear();
        element.sendKeys("andy");
        
        WebElement password = driver.findElement(By.name("userPassword"));
        
        password.clear();
        password.sendKeys("apple");
        
        password.submit();
        
        return;
	}
	
	public static Integer decimals(String s){
		int last = s.length()-1;
		int d = s.indexOf(".");
		return last - d;
	}
	
	public static void inputTemp(double F){
		String a = convertTemp(F);
		System.out.println("Converting " + F + " into celsius: " + a);
		Integer b = decimals(a);
		if((F>=0) && (F<=212)){
			if(b!=2){
				System.out.println("Conversion should have resulted in 2 places of percision. Got " + b);
			}
		}
		else{
			if(b!=1){
				System.out.println("Conversion should have resulted in 1 place of percision. Got " + b);
			}
		}
	}
	
	public static void testConverter(){
		inputTemp(-10.000);
	}
	
	public static void testURL(){
		String s = driver.getCurrentUrl();
		
		System.out.println("Testing converting from URL lowercase");
		driver.get(s + "?farenheittemperature=212");
		System.out.println("result is " + driver.getPageSource());
		
		System.out.println("Testing converting from URL");
		driver.get(s + "?farenheitTemperature=212");
		System.out.println("result is " + getTempFromSource(driver.getPageSource()));
		
		System.out.println("Testing converting from URL");
		driver.get(s + "?farenheitTemperature=9.73E2");
		System.out.println("result is " + getTempFromSource(driver.getPageSource()));
		
		
	}
	
	public static void testMultiple(){
		WebDriver Driver;
		
		Driver = new HtmlUnitDriver();
		
		Driver.get("http://apt-public.appspot.com/testing-lab-login.html");

        WebElement element = Driver.findElement(By.name("userId"));

        element.clear();
        element.sendKeys("andy");
        
        WebElement password = Driver.findElement(By.name("userPassword"));
        
        password.clear();
        password.sendKeys("apple");
        
        password.submit();
        WebElement box = driver.findElement(By.name("farenheitTemperature"));
        System.out.println("Success");
        
        Driver.quit();
        
        System.out.println("Login with leading and trailing white space and upper case letters in uname");
        
        Driver = new HtmlUnitDriver();
		
		Driver.get("http://apt-public.appspot.com/testing-lab-login.html");

        WebElement element1 = Driver.findElement(By.name("userId"));

        element.clear();
        element.sendKeys("   bOb   ");
        
        WebElement password1 = Driver.findElement(By.name("userPassword"));
        
        password.clear();
        password.sendKeys("bathtub");
        
        password.submit();
        WebElement box1 = driver.findElement(By.name("farenheitTemperature"));
        System.out.println("Success");
        
        Driver.quit();

        System.out.println("Login with leading and trailing white space and upper case letters in password");
        
        Driver = new HtmlUnitDriver();
		
		Driver.get("http://apt-public.appspot.com/testing-lab-login.html");

        WebElement element2 = Driver.findElement(By.name("userId"));

        element.clear();
        element.sendKeys("   chaRlie   ");
        
        WebElement password2 = Driver.findElement(By.name("userPassword"));
        
        password.clear();
        password.sendKeys("China");
        
        password.submit();
        //WebElement box2 = driver.findElement(By.name("farenheitTemperature"));
        System.out.println("Sucess");
        
        Driver.quit();
        
	}
	
	
	public void testLogin(){
		WebDriver driver = new HtmlUnitDriver();

        // And now use this to visit Google
        //driver.get("http://www.google.com");
        driver.get("http://apt-public.appspot.com/testing-lab-login.html");

        // Find the text input element by its name
        //WebElement element = driver.findElement(By.name("q"));
        WebElement element = driver.findElement(By.name("userId"));

        // Enter something to search for
        element.clear();
        element.sendKeys("andy");
        //element.submit();

        WebElement password = driver.findElement(By.name("userPassword"));
        
        password.clear();
        password.sendKeys("apple");
        
        password.submit();
        
        
        // Now submit the form. WebDriver will find the form for us from the element
        //element.submit();

        // Check the title of the page
        System.out.println("Page title is: " + driver.getTitle());

        driver.quit();
	}
	
    public static void main(String[] args) {
        login();
    	testConverter();
    	testURL();
    	
    	driver.quit();
    	
    	testMultiple();
        
        
    }
}