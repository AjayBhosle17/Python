abstract class Parent{
	int x=10;
	abstract void property();
}
class child extends Parent{

	void property(){

		System.out.println("gold,money");
	
	}

	public static void main(String[]args){
	
		child c=new child();
		c.property();
	}
}



