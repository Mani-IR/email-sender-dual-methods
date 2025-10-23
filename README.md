# Email Sender Script

This Python script demonstrates two methods for sending emails: one using the built-in `smtplib` library with `email.mime` for composing multipart emails (including HTML and plain text), and another using the third-party `yagmail` library for simpler email sending with support for HTML, attachments, and more. The script is designed to send emails via Gmail's SMTP server using app passwords for authentication.

The `smtplib` method is fully implemented in the script, while the `yagmail` method is provided as an alternative at the end. Note that in the provided code, both are active, but you can comment out one to use the other exclusively.

## Requirements

- Python 3.x
- For the `yagmail` method: Install the `yagmail` library (see Installation section).
- A Gmail account with an app password generated (do not use your main password for security reasons). Instructions for generating an app password: Go to your Google Account > Security > App passwords > Select app (e.g., "Mail") and device > Generate.

**Important Security Note:** Never hardcode sensitive credentials like email passwords in production code. Use environment variables or secret managers instead.

## Installation

### Setting Up a Virtual Environment (venv)

It's recommended to use a virtual environment to isolate dependencies. Follow these steps:

1. Navigate to your project directory in the terminal.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install required dependencies (only needed for the `yagmail` method):
   ```
   pip install yagmail
   ```
5. Deactivate when done: `deactivate`

The `smtplib` method uses built-in libraries, so no additional installations are required.

To automate dependency installation, you can create a `requirements.txt` file with the following content:
```
yagmail
```
Then run `pip install -r requirements.txt` inside the activated venv.

## Usage

### Method 1: Using `smtplib` (Built-in Python Libraries)

This method creates a multipart email with both plain text and HTML versions, attaches them, and sends via SMTP. It's more verbose but doesn't require external libraries.

1. Update the sender email, recipient, subject, HTML content, and text content in the script.
2. Replace the app password in the `s.login()` call (e.g., `'bynh gmje oktn zoya'`).
3. Run the script:
   ```
   python email_sender.py  # Assuming the script is saved as email_sender.py
   ```

Example code snippet (as provided):
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(sender, recipient, subject, html_content, text_content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    part1 = MIMEText(text_content, 'plain')
    part2 = MIMEText(html_content, 'html')
    msg.attach(part1)
    msg.attach(part2)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(sender, 'bynh gmje oktn zoya')  # Replace with your app password
        s.send_message(msg)
        print("Email sent successfully!")

html_content = """
<html>
    <body>
        <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="500"/>
        <h1 style="color:blue;">This is the HTML Body of the Email</h1>
        <p>This email contains both plain text and HTML versions.</p>
        <p>Winter is coming!</p>
    </body>
</html>
"""
text_content = """
This is the plain text version of the email:   
Winter is coming!
Here's a list:
- Item 1
- Item 2
- Item 3
"""
send_html_email(
    "maniajorloo23333@gmail.com",
    "maniajorloo23333@gmail.com",
    "HTML Email Test",
    html_content,
    text_content,
)
```

This will send an email with HTML formatting (including an image) and a fallback plain text version.

### Method 2: Using `yagmail` (Third-Party Library)

This method simplifies email sending, allowing inline HTML, attachments, and mixed content in a list. It's easier for quick setups but requires installing `yagmail`.

1. Ensure `yagmail` is installed (see Installation).
2. Update the sender email, app password, recipient, subject, contents, and attachments in the script.
3. Run the script:
   ```
   python email_sender.py  # Assuming the script is saved as email_sender.py
   ```

Example code snippet (as provided):
```python
import yagmail

yag = yagmail.SMTP(
    "maniajorloo23333@gmail.com",
    "bynh gmje oktn zoya"  # Replace with your app password
)

contents = [
    "This is the body, and here is just text",
    "You can even send HTML with yagmail",
    "<h1>This is an HTML Header</h1><p>This is a paragraph in HTML.</p>",
    "You can also attach files",
]

attachments = [
    'download.jpg'  # Replace with your file path
]

yag.send(
    to="the.developer.web.68@gmail.com",
    subject='subject',
    contents=contents,
    attachments=attachments
)
```

This sends a mixed-content email with text, HTML, and an attachment.

## Comparison of the Two Methods

| Aspect              | `smtplib` Method                          | `yagmail` Method                          |
|---------------------|-------------------------------------------|-------------------------------------------|
| **Dependencies**   | Built-in (no installs needed)            | Requires `pip install yagmail`           |
| **Ease of Use**    | More verbose; manual MIME construction   | Simpler API; handles MIME automatically  |
| **Features**       | Supports plain text, HTML, multipart     | Supports text, HTML, attachments, embeds |
| **Customization**  | High (full control over MIME parts)      | Medium (list-based content, easy attachments) |
| **Error Handling** | Manual (try-except needed for robustness)| Built-in retries and better error messages|
| **Performance**    | Lightweight (no external libs)           | Slightly heavier due to dependency       |
| **Portability**    | Works anywhere Python is installed       | Requires installing `yagmail`            |

### Pros and Cons

**`smtplib` Pros:**
- No external dependencies—ideal for minimal environments or scripts that need to run on any Python setup.
- Full control over email structure, which is useful for complex emails (e.g., custom headers, multiple attachments).
- Built-in, so it's more secure in terms of supply chain (no third-party code).

**`smtplib` Cons:**
- Boilerplate code for MIME handling can be error-prone for beginners.
- Less intuitive for quick tasks like attaching files or embedding images.
- Requires manual handling of connections and errors.

**`yagmail` Pros:**
- Much simpler and readable code—great for rapid prototyping or non-expert users.
- Automatically handles HTML, attachments, and even OAuth (though app passwords are used here).
- Supports advanced features like CC/BCC, inline images, and retries out of the box.

**`yagmail` Cons:**
- Adds a dependency, which could introduce vulnerabilities or break if the library isn't maintained.
- Less flexible for very custom email formats.
- Slightly higher overhead for simple emails.

Choose `smtplib` for production or dependency-free scripts, and `yagmail` for ease and quick development.

## License

This script is provided as-is under the MIT License. Feel free to modify and use it!