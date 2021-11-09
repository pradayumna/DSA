/**
 * DSA Final Assessment Question 4 - Q4MaxHeapTest.java
 *
 * Name : 
 * ID   :
 *
 **/
 
public class Q4MaxHeapTest
{
	public static void main(String args[])
	{
		System.out.println("\n===== Question 4: Testing Heaps =====\n");
		
		Q4MaxHeap  testHeap = new Q4MaxHeap();
		
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