using System;

namespace KeyVaultTest
{
    class Program
    {
        //Create new key vault at azure portal. Use Azure Portal to generate several Keys and several Certificates(set expiration dates and disable at least 2 keys)
	//Usingf the SDK , create a new software RSA key "myRSAKey" that will expire in 5 days from today
        public static async Task task1()
        {
              System.Console.WriteLine("--------------task1 is complete-----------------------------------------");
        }

        // Print the name , type and the expiration time of each key stored in your Key Vault
        public static async Task task2()
        {
            System.Console.WriteLine("--------------task2 is complete-----------------------------------------");
        }


        //Create a new version of the "myRSAKey" key and print all versions of that key
        public static async Task task3()
        {
            System.Console.WriteLine("--------------task3 is complete-----------------------------------------");
        }


        //Use the key "myRSAKey" to encrypt and decrypt provided string using the algorithm RSAOAEP. Print encrypted result and the string you received after decryption
        public static async Task task4()
        {
            System.Console.WriteLine("--------------task4 is complete-----------------------------------------");
        }

        //Initiate self signed certificate creation with default policy named <yourname>_cert
        public static async Task task5()
        {
            System.Console.WriteLine("--------------task5 is complete-----------------------------------------");
        }

        //Check the status of the certificate you started to create above. Wait undtill certificate is created successfully. Create a new version of that certificate.
        public static async Task task5a()
        {          
            System.Console.WriteLine("--------------task5a is complete-----------------------------------------");
        }

        //Get the latest <yourname>_cert version and update it 
        public static async Task task5b()
        {
            System.Console.WriteLine("--------------task5a is complete-----------------------------------------");
        }

        //Create new self signed certificate , customize  this certificate policy to ensure that this certificate is valid for the next 3 month only
        public static async Task task6()
        {
            System.Console.WriteLine("--------------task6 is complete-----------------------------------------");
        }


        //Delete  "myRSAKey"
        public static async Task task7()
        {
            System.Console.WriteLine("--------------task7 is complete-----------------------------------------");
        }

        //Delete  certificates you created at task5 and task6
        public static async Task task8()
        {
            System.Console.WriteLine("--------------task8 is complete-----------------------------------------");
        }

        static async Task Main(string[] args)
        {

          task1().Wait();
          task2().Wait();
          task3().Wait();
          task4().Wait();
          task5().Wait();
          task6().Wait();
          task7().Wait();
        }
    }
}
