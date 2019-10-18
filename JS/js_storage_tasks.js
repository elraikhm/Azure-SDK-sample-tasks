/*Create new storage account , create 3 containers in the account : "containerjs-01",containerjs-02 and containerjs-03, upload a file (amy image) to containerjs-01 using azure portal 
  and capture this file name in the scorageHandler method below under "blobname" variable
  copy your account credentials below*/
const account = "";
const accountKey = "";

//Use the account and accountKey constants to create an object that allows you to connect to the storage account below
//

/*  Task 1 - In this Task you will create a container, create a blob, list all containers, 
    list all blobs in containers, and list all containers by page. 
*/
async function createContainer(containerName) {
    //TODO: Write code that creates a container with a given name

    try {
    }
    catch (errr) {
    }
    
}

async function createBlob(containerName, content, blobName) {
    //TODO: Write code that creates a blob with the given name and content in a container with specified name    
}

async function listAllContainers() {
    //TODO: Lists all the names of the containers in storage account 
}

async function countContainers() {
    //TODO: Complete following code that counts the number of containers in storage account 1
}

async function listAllBlobInContainer(containerName) {
    //TODO: Complete following code that lists all the blobs in the given container
}

/*  Task 2 - In this Task you will update a blob, download a blob, get length of blob, check if the container is empty, 
    delete the blob, and delete the container.
*/
async function updateBlob(containerName, content, blobName) {
    //TODO: Write code that updates the given blob with the new given content in a container with specified name
}

async function downloadBlob(fromContainer, blobName, downloadFolderPath) {
    //TODO: Write code that downloads a blob with given name from a container with specified name in the given downloadFilePath
}

async function getLengthOfBlob(containerName, blobName) {
    //TODO: Write code that gets the content length of a blob with given name in a container with specified name
    
}
async function isEmpty(containerName) {
    //TODO: Write code that checks to see if a container with a given name is empty (has zero containers) or not
    
}

async function deleteBlob(containerName, blobName) {
    //TODO: Write code that deletes a blob with the given name in a container with specified name
    
}

async function deleteContainer(containerName) {
    //TODO: Write code that deletes a container with a given name

}

async function storageHandler() {
    /*
     * TODO: In this function which is the main function of the program replace names written in capital letters accordingly
     */
    // print containers in storage account
    const containerName = "containerjs-01";
    const newContainerName = "containerjs-04";
    const blobName = "";
    const newblob = "newblob"
    await listAllContainers();

    //Count containers in storage account
    await countContainers();
    
    //print blobs in a container
    await listAllBlobInContainer(containerName);
    // create a container
    //await createContainer(newContainerName);
    // create a blob
    await createBlob(newContainerName, "Hello world", newblob);
    // get length of a blob
    await getLengthOfBlob(containerName, blobName);
    //update a blob
    await updateBlob(containerName, "Hello world from UX lab", newblob);
    // download a blob
    await downloadBlob(containerName, newblob, "C:\\StorageJS\\TestProject\\");
    // delete a blob
    await deleteBlob(containerName, newblob);
    // check to see if empty
    await isEmpty(containerName);
    // delete a container
    await deleteContainer(containerName);

}

storageHandler()
    .then(() => {
        console.log("Application run success");
    })
    .catch((err) => {
        console.log(err.message);
    });

/* Task 3. In this task, you will create a signed access signature 
*/ 
async function setReadOnlySASPermissions(containerName, blobToSetPermsOnName) {
    //TODO: Write code that creates a signed access signature that gives read permission to the blob for the next 6 hours
    //A shared access signature is a token that somebody can use to request access to a resource without needing to know the
    //credentials to access the storage account
    const now = new Date();
    const sixHoursFromNow = new Date(now.getTime() + 6 * 60 * 60 * 1000);

}

async function setContainerReadOnlySASPermissions(containerName) {
    //TODO: Write code that creates a signed access signature that gives read permission to the container for the next 6 hours
    //A shared access signature is a token that somebody can use to request access to a resource without needing to know the
    //credentials to access the storage account
}