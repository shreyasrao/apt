import org.junit.rules.ExpectedException;

import junit.framework.TestCase;

public class RationalTest extends TestCase {
	
    protected Rational HALF;

    protected void setUp() {
      HALF = new Rational( 1, 2 );
    }

    // Create new test
    public RationalTest (String name) {
        super(name);
    }

    public void testEquality() {
        assertEquals(new Rational(1,3), new Rational(1,3));
        assertEquals(new Rational(1,3), new Rational(2,6));
        assertEquals(new Rational(3,3), new Rational(1,1));
    }

    // Test for nonequality
    public void testNonEquality() {
        assertFalse(new Rational(2,3).equals(
            new Rational(1,3)));
    }

    public void testAccessors() {
    	assertEquals(new Rational(2,3).numerator(), 2);
    	assertEquals(new Rational(2,3).denominator(), 3);
    }

    public void testRoot() {
        Rational s = new Rational( 1, 4 );
        Rational sRoot = null;
        try {
            sRoot = s.root();
        } catch (IllegalArgumentToSquareRootException e) {
            e.printStackTrace();
        }
        assertTrue( sRoot.isLessThan( HALF.plus( Rational.getTolerance() ) ) 
                        && HALF.minus( Rational.getTolerance() ).isLessThan( sRoot ) );
    }
    
    public void testAbs(){
    	Rational a = new Rational(-2,3);
    	Rational b = new Rational(2,3);
    	assertEquals(a.abs(), b);	
    }
    
    public void testLT(){
    	Rational a = new Rational(1,-3);
    	Rational b = new Rational(1,23);
    	assertTrue(a.isLessThan(b));
    }
    
    public void testPlus(){
    	Rational a = new Rational(2,3);
    	Rational c = new Rational(1,-3);
    	Rational b = new Rational(1,3);
    	assertEquals(c.plus(a),b);
    }
    
    public void testMinus(){
    	Rational a = new Rational(2,23);
    	Rational b = new Rational(2,-23);
    	Rational c = new Rational(-4,23);
    	
    	assertEquals(b.minus(a),c);
    }
    
    public void testTimes(){
    	Rational a = new Rational(-2,3);
    	Rational b = new Rational(2,3);
    	assertEquals(a.abs(), b.times(new Rational(-1,1).abs()));	
    }
    
    public void testDivides(){
    	Rational a = new Rational(2,3);
    	Rational b = new Rational(2,1);
    	Rational c = new Rational(1,3);
    	assertEquals(a.divides(b),c);
    }
    
    public void testToString(){
    	Rational a = new Rational(55,50);
    	Integer num = a.numerator();
    	Integer den = a.denominator();
    	String res = num.toString() + '/' + den.toString();
    	assertEquals(a.toString(),res);
    }
    
    public void testCopyConstructor(){
    	Rational a = new Rational(1,-3);
    	int num = a.numerator();
    	int den = a.denominator();
    	Rational b = new Rational(a);
    	assertEquals(num,b.numerator());
    	assertEquals(den,b.denominator());	
    }
    
    public void testTolerance(){
    	Rational a = new Rational(2,23);
    	a.setTolerance(a);
    	assertEquals(a, a.getTolerance());
    }

    public void testThrows(){
    	try{
    		Rational a = new Rational(2147483647*2,1);
    		a.root();
    		fail("Should not have gotten past root method");
    	} catch(Exception e){
    	}
    }
    
    public void testMain(){
    	String he[] = {"a","b"};
    	Rational.main(he);
    }
    
    public static void main(String args[]) {
        String[] testCaseName = 
            { RationalTest.class.getName() };
        // junit.swingui.TestRunner.main(testCaseName);
        junit.textui.TestRunner.main(testCaseName);
    }
}


