
import java.util.ArrayList;
import java.util.List;

class Solution {
	private String str;

    public List<String> fizzBuzz(int n) {

		List<String> myList = new ArrayList<>();
        for(int i = 0; i < n; i++)
		{
			if(i % 3 == 0 && i % 5 == 0)
			{
				str = "FizzBuzz";
				myList.add(str);
			}
			else if(i % 3 == 0)
			{
				str = "Fizz";
				myList.add(str);
			}
			else if(i % 5 == 0)
			{
				str = "Buzz";
				myList.add(str);
			}
			else
			{
				str = String.valueOf(i);
				myList.add(str);
			}
		}
		return myList;
    }
}
