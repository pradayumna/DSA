/**
 * DSA Final Assessment Question 3 - Q3MaxHeapTest.java
 *
 * Name : 
 * ID   :
 *
 **/
 
public class Q3MaxHeapTest
{
	public static void main(String args[])
	{
		System.out.println("\n===== Question 3: Testing Heaps =====\n");
		
		Q3MaxHeap  testHeap = new Q3MaxHeap();
		
        System.out.println("Adding items...");
		for (int i=0; i<10; i++)
		{
			testHeap.add(i, "value-"+ Integer.toString(i));
            System.out.println("Added " + "value-"+Integer.toString(i)+" Priority: " + Integer.toString(i));
		}
		
        System.out.println();
        System.out.println("Removing items...");
		String temp;
		
		for (int i=0; i<10; i++)
		{
			temp = (String)testHeap.remove();
			System.out.println(temp);
		}
		System.out.println("\n===== Tests Complete =====\n");
	}
}