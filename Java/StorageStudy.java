package java_storage_study;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;



public class StorageStudy {


	//-----------------------------------------------------------------------------------------------------------------
	//	Task 1 – Create new storage account at azure portal. Create container "books" and create a new blob step1.txt, add "Hello World" message, also upload couple of images to this container using the portal interface.
	//		create additional containers cont1, cont2 and cont3
	//      Using Azure SDK print the list of all the blobs available under the container “books” within your account. 
	static void task1() 
	{
		System.out.println("end of task1-----------------------------------------------");

	}
	//Copy the list of blobs you received  here:______________________________________________
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

		
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//	Task 2 – print the names of all containers in your storage account
	static void task2()
	{
		//add your code here
		System.out.println("end of task2-------------------------------------------------");
	}
	//Copy the list of blobs you received  here:______________________________________________
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

	
	
			
	//-----------------------------------------------------------------------------------------------------------------
	//	Task 3a – retrieve blob step1.txt from the container “books” and print it's content 
	static void task3a() 
	{
		System.out.println("end of task3a-------------------------------------------------");
	}
	//Copy the blob step1.txt content  here:______________________________________________
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

	
	
		
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//	Task 3b – print the size ( bytes ) of the  blob step1.txt from the container “books”
	static void task3b() 
	{
		System.out.println("end of task3b-------------------------------------------------");
	}
	//Add the size of the step2.txt blob  here:______________________________________________
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 


	
	
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//	Task 3c – retrieve last 2 bytes from blob step1.txt located in the container “books” and print them   
	static void task3c() 
	{
		System.out.println("end of task3c-------------------------------------------------");
	}
	//Copy retrieved content here:______________________________________________
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

	
	
	
	
	
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//	Task 4 – create a new container “mybooks” using the SDK
	static void task4() 
	{
		//add your code here
		System.out.println("end of task4---------------------------------------------------");
	}
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

	
	
	
	
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//	Task 5 –  upload a file from your  local disk  to newbook.txt blob in your new container “mybooks”.
	//Before you start, please comment out the task4 from the main function
	static void task5() 
	{
		//add your code here
		System.out.println("end of task5-------------------------------------------------------");
	}
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

	
	
	
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//Task 6 – The gutenberg project contains a large number of ebooks online
	// Write code that stores one of the large books in a new blob named newbook.txt in the mybooks container
	// This URL points to a sample book: "http://www.gutenberg.org/files/59466/59466-0.txt"
	static void task6()
	{
		//add your code here
		System.out.println(" end of task6------------------------------------------------");
	}
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 


	
	
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//	Task 7 - delete blob "newbook.txt" from "mybooks" container
	static void task7()
	{
		//add your code here
		System.out.println("end of task7---------------------------------------------------------");
	}
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

	
	
	
	
	//-----------------------------------------------------------------------------------------------------------------
	//  Task 8 - delete your container “mybooks”
	static void task8()
	{
		//add your code here
		System.out.println("end of task8-------------------------------------------------------------");
	}
	//How long this task took to implement(min): ____________________________________
	//How difficult ( very easy, easy, ok, hard, very hard)______________________   
	//How and what can we improve___________________________________________ 

	
	
	
	
    public static void main(String[] args) throws java.lang.Exception{
    	task1();
    	task2();
    	task3a();
    	task3b();
    	task3c();
    	task4();
    	task5();
    	task6();
    	task7();
	task8();
     }
}
