import requests
import PyPDF2

# URL of the PDF file
url = "https://www.canada.ca/content/dam/ircc/migration/ircc/english/pdf/kits/forms/imm5645e.pdf"

# Download the PDF file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open the PDF file
    with open("imm5645e.pdf", "wb") as file:
        # Write the contents of the PDF file
        file.write(response.content)

    # Open the downloaded PDF file
    with open("imm5645e.pdf", "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(file)
        
        # Initialize an empty string to store the extracted text
        text = ""
        
        # Iterate through each page of the PDF
        for page_num in range(pdf_reader.numPages):
            # Extract text from the page
            page_text = pdf_reader.getPage(page_num).extractText()
            # Append the extracted text to the string
            text += page_text
        
        # Print the extracted text
        print(text)
else:
    print("Failed to download the PDF file.")



#jenishshekhada@Jenishs-MacBook-Air ~ % sudo brew services start httpd


# Warning: Taking root:admin ownership of some httpd paths:
#   /opt/homebrew/Cellar/httpd/2.4.58/bin
#   /opt/homebrew/Cellar/httpd/2.4.58/bin/httpd
#   /opt/homebrew/opt/httpd
#   /opt/homebrew/opt/httpd/bin
#   /opt/homebrew/var/homebrew/linked/httpd
# This will require manual removal of these paths using `sudo rm` on
# brew upgrade/reinstall/uninstall.
# Warning: httpd must be run as non-root to start at user login!
# ==> Successfully started `httpd` (label: homebrew.mxcl.httpd)