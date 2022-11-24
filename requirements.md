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
4. multilingual accessibility

## Use Cases

6. Send Messages to Followers

- **Pre-condition:** The customer is logged in

- **Trigger:** Customer selects "send tweet/message"

- **Primary Sequence:**

  1. System has a text box prompt that customers can enter a message into
  2. Customer can add and edit text inside the box
  3. System checks that the message is within the word limit
  4. Customer can press a send button
  5. System communicates with servers to upload the message
  6. System ensures the message can appear on customer profile
  7. Followers will be able to see the message

- **Primary Postconditions:** A message appears that followers can read

- **Alternate Sequence:**

  1. The Customer is unable to send the message
  2. The message will no send to servers and followers cannot see the message

- **Alternate Sequence:**

  1. The servers fail to update
  2. Followers cannot see the message

8. Post image with message

- **Pre-condition:** The customer is logged in

- **Trigger:** Customer selects "send tweet/message"

- **Primary Sequence:**

  1. System has a upload image prompt and text box
  2. Customers can upload multiple image files into the image prompt
  3. Customer can add and edit text inside a text box
  4. System checks that the message is within the word limit
  5. Customer can press a send button
  6. System communicates with servers to upload the images and message
  7. System ensures the image and message can appear on customer profile
  8. Followers will be able to see the images and message

- **Primary Postconditions:** A message appears that followers can read

- **Alternate Sequence:**

  1. The Customer is unable to send the image
  2. The message will no send to servers and followers cannot see the image

- **Alternate Sequence:**

  1. The servers fail to update
  2. Followers cannot see the image

9. Delete Post
- **Pre-condition:** The Customer adds a post

- **Trigger:** Customer selects "delete post"

- **Primary Sequence:**

  1. When the Customer selects the menu next to the post, an option menu is printed 
  2. Customer selects "delete post"
  3. System checks for where the post is stored in the database and removes it from the store

- **Primary Postconditions:** A message appears reading "Successful Deletion"

- **Alternate Sequence:**

  1. The Customer is unable to delete their post
  2. The message will not delete from the database and followers still see the post

10. Password Reset
- **Pre-condition:** The customer is logged in

- **Trigger:** Customer selects "change my password"

- **Primary Sequence:**

  1. Customer clicks on their profile and a menu drop down appears
  2. Customer selects "change my password"
  3. Customer is prompted to enter their old password followed by their new password
  4. System assigns a new hash for the new password and pairs it with the Customer's login information

- **Primary Postconditions:** A message appears reading "Successful Password Reset"

- **Alternate Sequence:**

  1. The Customer enters the same password as their old one
  2. The System will prompt to enter a new password

12. Users should be able to follow each other

- **Pre-condition:** The customer is logged in

- **Trigger:** Customer clicks on "add friend" button

- **Primary Sequence:**

  1. Drop down box to search for users appears
  2. Customer types in name of friend he wants to add and hits search
  3. A list of matches for users appears on the screen
  4. Customer then finds the profile, and clicks the "send friend request" button to the right of the name
  5. System sends a friend request notification to the user that was chosen
  6. The user who recieved the friend request will get a notification on their home page
  7. They can click the notification and get the choice to accept or decline it

- **Primary Postconditions:** If the user accepted, they are now added as a friend and their posts will appear on the customers home page

- **Alternate Sequence:**

  1. Customer enters and searches for a person they are already friends with
  2. When the user is found, the option to "send friend request" will be greyed out

- **Alternate Sequence:**

  1. Customer searches for someone to add that does not exist
  2. A notice saying "No user found" will appear to notify that name does not exist