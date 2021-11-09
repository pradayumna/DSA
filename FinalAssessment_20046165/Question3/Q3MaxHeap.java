/**
 * DSA Final Assessment Question 3 - Q3MaxHeap.java
 *
 * Name : 
 * ID   :
 *
 **/
 
public class Q3MaxHeap
{

	public class HeapEntry
	{
	private int priority;
	private Object value;

	public HeapEntry(int priority, Object value)
	{
		this.priority = priority;
		this.value = value;
	}

	public int getPriority()
	{
		return priority;
	}

	public Object getValue()
	{
		return value;
	}

	}

	private HeapEntry[] heap;
	private int count;
	private int MAXSIZE = 10;
	
	
	public Q3MaxHeap()
	{
		heap = new HeapEntry[MAXSIZE];
		count = 0;	
	}


	public void add(int priority, Object value)
	{
		HeapEntry entry = new HeapEntry(priority, value);
		heap[count] = entry;
		count++;
		trickleUp(count-1);
	}

	public Object remove() 
	{
		Object retValue;
		HeapEntry entry = heap[0];
		retValue = entry.getValue();
		heap[0] = heap[count-1];
		heap[count-1] = null;
		count--;
		trickleDown(0);
		return retValue;
	}

	private void trickleDown(int index)
	{
	   int leftIdx = index * 2 + 1;
	   int rightIdx = leftIdx + 1;
	   int largeIdx;
	   HeapEntry temp;

	   if (leftIdx < count)
		{
		largeIdx = leftIdx;			
		if (rightIdx < count)
		{
		   if (heap[leftIdx].getPriority() < heap[rightIdx].getPriority())
			{
				largeIdx = rightIdx;
			}
		}
		if (heap[largeIdx].getPriority() > heap[index].getPriority())
		{
              	temp = heap[largeIdx];
              	heap[largeIdx] = heap[index];
              	heap[index] = temp;
			trickleDown(largeIdx);
		}	
	   }
	}
	
	private void trickleUp(int index)
	{
		int parentIndex;
		HeapEntry temp;

		parentIndex = (index-1)/2;

		if (index > 0 )
		{
			if (heap[index].getPriority() > heap[parentIndex].getPriority())
			{
				temp = heap[parentIndex];
				heap[parentIndex] = heap[index];
				heap[index] = temp;
				trickleUp(parentIndex);
			}
		}
		
	}
}