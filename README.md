# webshell-checker
This script is designed to check a list of URLs for the presence of certain keywords that are commonly associated with web shells or other malicious code.

Here's how to use the script:

1. Save the script to a file (e.g. check_urls.sh) on your computer.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script with the command bash check_urls.sh input_file, where "input_file" is the name of the file containing the list of URLs you want to check.
5. The script will output the status of each URL (OK, BAD, or ERROR) along with the URL itself. URLs that contain one of the specified keywords will be saved to a file called "done.txt".
6. When the script is finished, you can open "done.txt" to see a list of all the URLs that were flagged as containing suspicious content.

Note that the script requires the "curl" command-line tool to be installed on your system in order to make HTTP requests to the URLs. If you don't already have curl installed, you can install it using your operating system's package manager (e.g. sudo apt-get install curl on Ubuntu).


# For educational purposes only.
![alt text](https://raw.githubusercontent.com/moominrasheed/webshell-checker/main/demo.png)
