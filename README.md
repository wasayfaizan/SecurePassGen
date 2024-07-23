# SecurePassGen
 
  <p>This is a Python script that generates random passwords based on user-defined criteria and allows users to store and update their passwords securely.</p>

  <h2>Features</h2>
    <ul>
        <li>Generate random passwords with customizable length, inclusion of numbers, and special characters.</li>
        <li>Store passwords with associated usage places (e.g., Facebook, Gmail).</li>
        <li>Update existing stored passwords.</li>
        <li>Error handling for malformed stored passwords.</li>
    </ul>

   <h2>Requirements</h2>
    <p>Python 3.x</p>

  <h2>Usage</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre>
git clone https://github.com/yourusername/password-generator.git
cd password-generator
            </pre>
        </li>
        <li><strong>Run the script:</strong>
            <pre>
python3 password-generator.py
            </pre>
        </li>
        <li><strong>Follow the prompts:</strong>
            <ul>
                <li>Enter the desired password length.</li>
                <li>Specify whether to include numbers and special characters.</li>
                <li>Review the generated password.</li>
                <li>Confirm if you want to use and store the password.</li>
                <li>Specify the place where you will use the password.</li>
                <li>Optionally, update an existing password.</li>
            </ul>
        </li>
    </ol>

   <h2>Example</h2>
    <pre>
Enter the desired password length: 12
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes
Generated password: a1@Xz7$Bc9L
Do you like this password and would you like to use it? (yes/no): yes
Where will you use this password? Facebook
Password stored successfully.
Do you want to update an existing password? (yes/no): no
    </pre>

   <h2>File Structure</h2>
    <ul>
        <li><code>password-generator.py</code>: The main script file containing the password generation and storage logic.</li>
        <li><code>passwords.txt</code>: The file where passwords are stored in the format <code>place: password</code>.</li>
    </ul>

   <h2>Notes</h2>
   <ul>
        <li>The script handles errors for malformed lines in <code>passwords.txt</code> by skipping them.</li>
        <li>If <code>passwords.txt</code> does not exist, it will be created upon storing the first password.</li>
    </ul>

   
