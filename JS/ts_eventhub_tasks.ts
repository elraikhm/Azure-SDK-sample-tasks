// Task 1 – Navigate to the Azure Portal and create new Event Hubs Namespace n
// At Azure Portal create a new event hub with at least 5 partitions and add 2 consumer groups .
// Write a code to retrieve the eventhub name and the partition ids for the Event Hub you
// just created
async function getRunTimeInfo(): Promise<void> {
//add your code here
    var hubBot = new EventHubClient('sb://lreventhubns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=42yoBR0Fid8kKBu8NNPq4FLYExG1tBKnRZDNsTEAo50=');

}


// Task 2 - Send an event with "Hello world" body to the partition 1 in your
// Event Hub, make sure that the retry mode is set to Fixed and allows up to 5
// attempts to retry the send operation
async function sendEvent(): Promise<void> {
// add your code here
}

// Task 3 - Write code that receives the event you just sent and prints out its
// body to the console. While receiving, set ownership level of partition "1" to 500. 
async function receiveEvent(): Promise<void> {

}

// Task 4 – generate 10 samples of temperature values (random number 0-100)  and send them all together to the Event Hub
async function sendBatch(): Promise<void> { 
//const temp = Math.floor(Math.random() * 120) + 1 ;
// add your code here
}

// Task 5 – receive all new events from the event hub and print out to the console. 
async function receiveAll(): Promise<void> { 

}

// Task 6 – EvenProcessor is an intelligent consumer agent that simplifies the management of checkpointing, leasing, and parallel event readers.
//          User will need to implement the actual event processing logic , but other aspects will be handled by the library.
//          Use EventProcessor class to print to the console all the events from your event hub. Expect it to be a larger task.
async function eventProcessing() {

}

// Task 7 – Receive all events from the partition 1  and ensure that current reader has an exclusive ownership on this partition.
// Sometimes consumer is intended to be the exclusive receiver of events for the requested partition and the associated consumer group, 
// in this case other receivers will receive an error when trying to receive events from this partition.
async function receiveEventsExclusive() {

}

async function main()
{
    await getRunTimeInfo();
    console.log(`getRunTimeInfo is complete`);
    await sendEvent();
    console.log(`sendEvent is complete`);
    await receiveEvent();
    console.log(`receiveEvent is complete`);
    await sendBatch();
    console.log(`sendBatch is complete`);
    await receiveAll();
    console.log(`receiveAll is complete`);
    await eventProcessing();
    console.log(`eventPorcessing is complete`);
    await receiveEventsExclusive();
    console.log(`receiveEventsExclusive is complete`);
}

main().catch(err => {
    console.log("Error occurred: ", err);
});