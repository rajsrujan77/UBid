Files in the directory:

    1. code - main.py: The main python script of the application.
    2. templates - file-upload.html: basic html script of the form.
    3. data - data.csv: Example data consisting of 2   columns - name and category.
	4. code - register: files used for registration
	
Jobs done by the API:

    Input:
    1. Upload the pdf file of tender document.
    2. Takes input: your 'name' and 'category' of the tender.

    Output:
    Gives all the names of the users in the same category.

Steps of use:

    1. Run the main.py from the terminal.
    2. The server gets started. Go to the address you get in the terminal from browser: default - '127.0.0.1:5000'.
    3. upload any pdf document of your wish. Enter your name. Enter your category.
    4. Once you click upload button in the browser check the 'uploads' folder in the root directory for your uploaded pdf.
    5. Check the terminal for the names of all the users in the category.

Objective:

1. The names given as output in the terminal would be the users to whom we send a notification once a tender is uploaded in his category.
2. This is the basic software which is our first step where a user uploads a tender with his details and we send a notification to bidders in that category.

Expectations:

Go through the working of the model and let us discuss all the needful for our software.