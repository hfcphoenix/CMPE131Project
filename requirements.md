## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete account
5. User home page (user can see messages of users they follow)
6. Send messages to followers
7. Multiple Sign Up Options (Email, Social Media) (Connect with any external API)
8. Post image with Message
9. Delete Post
10. Password Reset
11. Character Limit for messages
12. Users should be able to follow each other

## Non-functional Requirements
1. Optimized for 16:9 aspect ratio on chromium browsers
2. Having an anti-bot checking system
3. Dark Mode and Light Mode
4. Multilingual accessibility

## Use Cases

1. Send Messages to Followers

- **Pre-condition:** The user is logged in

- **Trigger:** user selects "send tweet/message"

- **Primary Sequence:**

  1. System has a text box prompt that users can enter a message into
  2. user can add and edit text inside the box
  3. System checks that the message is within the word limit
  4. user can press a send button
  5. System communicates with servers to upload the message
  6. System ensures the message can appear on user profile
  7. Followers will be able to see the message

- **Primary Postconditions:** A message appears that followers can read

- **Alternate Sequence:**

  1. The user is unable to send the message
  2. The message will no send to servers and followers cannot see the message

- **Alternate Sequence:**

  1. The servers fail to update
  2. Followers cannot see the message

2. Have multiple sign in options such as from email and social media by connecing an external API

- **Pre-condition:** The user has loaded the website and enters their username and password in the login section

- **Trigger:** Clicking the login button

- **Primary Sequence:**

  1. The user sees there is a section for logging in at the top right of the website.
  2. The user enters their username and password.
  3. The user clicks the login button.
  4. The website refreshes with the customized contents of the homepage after the login proccess is succesful.


- **Primary Postconditions:** The user is now logged in and the website loads their customized homepage.

- **Alternate Sequence:**

  1. The user sees there is a section for logging in at the top right of the website.
  2. The user enters their incorrect username or an incorrect password.
  3. The user clicks the login button.
  4. The webpage will show a page that shows that the username has entered an incorrect password or username.
  5. The user reenters their correct credentials.
  6. The website refreshes with the customized contents of the homepage after the login proccess is succesful.

- **Alternate Sequence:**

  1. The user clicks the Google login button
  2. A popup will show with the option to sign in to their Gmail
  3. The user enters their information
  4. The user clicks sign in
  5. The website refreshes with the customized contents of the homepage after the login proccess is succesful

3. Post image with message

- **Pre-condition:** The user is logged in

- **Trigger:** user selects "send tweet/message"

- **Primary Sequence:**

  1. System has a upload image prompt and text box
  2. users can upload multiple image files into the image prompt
  3. user can add and edit text inside a text box
  4. System checks that the message is within the word limit
  5. user can press a send button
  6. System communicates with servers to upload the images and message
  7. System ensures the image and message can appear on user profile
  8. Followers will be able to see the images and message

- **Primary Postconditions:** A message appears that followers can read

- **Alternate Sequence:**

  1. The user is unable to send the image
  2. The message will no send to servers and followers cannot see the image

- **Alternate Sequence:**

  1. The servers fail to update
  2. Followers cannot see the image

4. Delete Post
- **Pre-condition:** The user adds a post

- **Trigger:** user selects "delete post"

- **Primary Sequence:**

  1. When the user selects the menu next to the post, an option menu is printed 
  2. user selects "delete post"
  3. System checks for where the post is stored in the database and removes it from the store

- **Primary Postconditions:** A message appears reading "Successful Deletion"

- **Alternate Sequence:**

  1. The user is unable to delete their post
  2. The message will not delete from the database and followers still see the post

5. Password Reset
- **Pre-condition:** The user is logged in

- **Trigger:** user selects "change my password"

- **Primary Sequence:**

  1. user clicks on their profile and a menu drop down appears
  2. user selects "change my password"
  3. user is prompted to enter their old password followed by their new password
  4. System assigns a new hash for the new password and pairs it with the user's login information

- **Primary Postconditions:** A message appears reading "Successful Password Reset"

- **Alternate Sequence:**

  1. The user enters the same password as their old one
  2. The System will prompt to enter a new password

6. Users should be able to follow each other

- **Pre-condition:** The user is logged in

- **Trigger:** user clicks on "add friend" button

- **Primary Sequence:**

  1. Drop down box to search for users appears
  2. user types in name of friend he wants to add and hits search
  3. A list of matches for users appears on the screen
  4. user then finds the profile, and clicks the "send friend request" button to the right of the name
  5. System sends a friend request notification to the user that was chosen
  6. The user who recieved the friend request will get a notification on their home page
  7. They can click the notification and get the choice to accept or decline it

- **Primary Postconditions:** If the user accepted, they are now added as a friend and their posts will appear on the users home page

- **Alternate Sequence:**

  1. user enters and searches for a person they are already friends with
  2. When the user is found, the option to "send friend request" will be greyed out

- **Alternate Sequence:**

  1. user searches for someone to add that does not exist
  2. A notice saying "No user found" will appear to notify that name does not exist