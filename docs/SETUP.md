# Setup


## Running the Script on Linux

To run the provided script on a Linux system, follow these steps:

1. **Open a Terminal**:
   - Launch the Terminal application on your Linux machine. You can usually find it in your system's applications menu or by searching for "Terminal."

2. **Navigate to the Script Directory**:
   - Use the `cd` command to navigate to the directory where your script (`run.sh`) is located. For example:

     ```bash
     cd /path/to/script/directory
     ```

3. **Make the Script Executable**:
   - If the script is not already marked as executable, you can use the `chmod` command to give it execution permissions:

     ```bash
     chmod +x run.sh
     ```

4. **Run the Script**:
   - Execute the script by providing your OpenAI API key as an argument:

     ```bash
     ./run.sh YOUR_API_KEY_HERE
     ```

   Replace `YOUR_API_KEY_HERE` with your actual OpenAI API key.

5. **Follow the Script Output**:
   - The script will set the `OPENAI_API_KEY` environment variable and execute `main.py`. Follow the output and any instructions provided by `main.py`.

---

## Running the Script on Windows


To run the provided script on a Windows system, follow these steps:

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.

2. **Navigate to the Script Directory**:
   - Use the `cd` command to navigate to the directory where your script (`run.bat`) is located. For example:

     ```batch
     cd C:\path\to\script\directory
     ```

3. **Run the Script**:
   - Execute the script by providing your OpenAI API key as an argument:

     ```batch
     run.bat YOUR_API_KEY_HERE
     ```

   Replace `YOUR_API_KEY_HERE` with your actual OpenAI API key.

4. **Follow the Script Output**:
   - The script will set the `OPENAI_API_KEY` environment variable and execute `app.py`. Follow the output and any instructions provided by `app.py`.

