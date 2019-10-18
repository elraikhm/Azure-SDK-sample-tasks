public class EvHubStorageStudy {

	// Task 1 – Navigate to the Azure Portal and create Event Hubs Namespace ,create a new event hub with at least 5 partitions and 2
	// consumer groups and name it yourname_eventhub.
	// Create a storage account and  configure your events to be captured in the "lrstorage123" storage account
	// Write a code to programmatically retrieve the name and partition ids for the Event Hub you just created
	static void task1() {
		//add your code here
		System.out.println("end of task1-----------------------------------------------");
	}

	// Task 2 - Send an event with your name as body to the partition 1 in your
	// Event Hub, make sure that the retry mode is set to Fixed and allows up to 5
	// attempts to retry the send operation
	static void task2() {
		//add your code here
		System.out.println("end of task2-----------------------------------------------");
	}

	// Task 3 - Write code that receives asyncroniously the event you just sent and prints out its
	// body to the console
	static void task3() {
		//add your code here
		System.out.println("end of task3-----------------------------------------------");
	}

	// Task 4 – generate 10 samples of the random temperature values(random number from 0-100) and
	// send them all to the Event Hub, allocate 2 partitions that can store the temperature data
	static void task4() {
		System.out.println("end of task4-----------------------------------------------");
	}

	// Task 5 – Use EventProcessor class to print to the console all the events from
	// your event hub
	static void task5() {
		System.out.println("end of task5-----------------------------------------------");
	}

	// Task 5a – subscribe to receive only new temperature data events and print
	// event data to the console [to test, send a new batch of temperature data
	// to the event hub]
	static void task5a() {
		System.out.println("end of task5a-----------------------------------------------");
	}

	// Task 6 - Navigate to Azure portal , go to the storage account and find blobs
	// with event hub data , write code to print of all event blobs in the storage
	// account
	static void task6() {

		System.out.println("end of task6-----------------------------------------------");
	}

	// Task 7 - write code to create a new container in your storage
	// account, name it eventhubs container and copy file from this
	// "http://www.gutenberg.org/cache/epub/60084/pg60084.txt" link to the container
	static void task7() {
		System.out.println("end of task7-----------------------------------------------");
	}

	// Feel free to comment out functions after you are done with the task
	public static void main(String[] args) throws java.lang.Exception {
		task1();
		task2();
		task3();
		task4();
		task5();
		task5a();
		task6();
		task7();
	}
}
