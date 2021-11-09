/**
 * DSA Final Assessment Question 2 - Q2BinarySearchTree.java
 *
 * Name : 
 * ID   :
 *
 **/

public class Q2BinarySearchTree {   
	// Inner class Q2TreeNode
	private class Q2TreeNode {
		public int value;
		public Q2TreeNode left;
		public Q2TreeNode right;
		
		public Q2TreeNode(int inVal)
		{
			value = inVal;
			left = null;
			right = null;
		}
	}
	// End Inner class
	// Class Q2BinarySearchTree
	private Q2TreeNode root;
	
	public Q2BinarySearchTree()
	{
		root = null;
	}
	
	public void insert(int val)
	{
		if (isEmpty())
		{
			root = new Q2TreeNode(val);
		}
		else
		{
			root = insertRec(val, root);
		}
	}

	public Boolean isEmpty()
	{
		return root == null;
	}

	private Q2TreeNode insertRec(int inVal, Q2TreeNode cur)
	{
		if (cur == null)
		{
			cur = new Q2TreeNode(inVal);
		}
		else
		{
			if (inVal < cur.value)
			{
				cur.left = insertRec(inVal, cur.left);
			}
			else	
			{
				cur.right = insertRec(inVal, cur.right);
			}
		}
		return cur;
	}
	
  
}
