import junit.framework.*;
import com.mockobjects.servlet.*;

public class testingWithMockObjects extends TestCase {

  public void test_bad_parameter() throws Exception {
    TestingLabConverterServlet s = new TestingLabConverterServlet();
    MockHttpServletRequest request = 
      new MockHttpServletRequest();
    MockHttpServletResponse response = 
      new MockHttpServletResponse();
    
    request.setupAddParameter("farenheitTemperature", "boo!");
    response.setExpectedContentType("text/html");
    s.doGet(request,response);
    response.verify();
    String res = "<html><head><title>Bad Temperature</title>"
          + "</head><body><h2>Need to enter a valid temperature!"
            + "Got a NumberFormatException on " 
          + "boo!" 
          + "</h2></body></html>" + "\n";
    assertEquals(res,
                 response.getOutputStreamContents());
  }
  
    public void test_empty_parameter() throws Exception {
    TestingLabConverterServlet s = new TestingLabConverterServlet();
    MockHttpServletRequest request = 
      new MockHttpServletRequest();
    MockHttpServletResponse response = 
      new MockHttpServletResponse();
    
    response.setExpectedContentType("text/html");
    s.doGet(request,response);
    response.verify();
    String res = "<html><head><title>No Temperature</title>"
          + "</head><body><h2>Need to enter a temperature!"
          + "</h2></body></html>" + "\n";
    assertEquals(res,
                 response.getOutputStreamContents());
  }


  public void test_boil() throws Exception {
    TestingLabConverterServlet s = new TestingLabConverterServlet();
    MockHttpServletRequest request = 
      new MockHttpServletRequest();
    MockHttpServletResponse response = 
      new MockHttpServletResponse();
    
    request.setupAddParameter("farenheitTemperature", "212");
    response.setExpectedContentType("text/html");
    s.doGet(request,response);
    response.verify();
    String austinTemperature = CityTemperatureServiceProvider.lookup("Austin");


    String res = "<html><head><title>Temperature Converter Result</title>" + "</head><body><h2>" + "212" + " Farenheit = " + "100" + " Celsius " + "</h2>" + "\n"+
    "<p><h3>The temperature in Austin is " + austinTemperature + " degrees Farenheit</h3>" + "\n" +
    "</body></html>" + "\n";

    assertEquals(res, response.getOutputStreamContents());
  }
  
}
