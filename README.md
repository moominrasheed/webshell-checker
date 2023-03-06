# webshell-checker
This is a Python script that can be used to check a list of URLs for web shells. The script uses the requests library to send HTTP requests to the URLs and search for common web shell signatures in the response.

To use the script, you need to have Python 3 installed on your system. You can run the script from the command line by passing the path to a text file containing a list of URLs as a command-line argument. For example:

Copy code
python3 check_urls.py urls.txt
where urls.txt is the path to the file containing the URLs to check.

The script uses multithreading to check the URLs in parallel, which can make the checking process faster. It also uses the tqdm library to display a progress bar during the checking process.

When the script finishes checking the URLs, it will create a file called done.txt in the same directory as the script. This file will contain a list of the URLs that were found to contain web shells.

It's important to note that using this script to check URLs that you do not have permission to access could be illegal and unethical. Always make sure to obtain proper authorization before conducting any security testing or scanning.


# For educational purposes only.
![alt text](https://raw.githubusercontent.com/moominrasheed/webshell-checker/main/demo.png)
